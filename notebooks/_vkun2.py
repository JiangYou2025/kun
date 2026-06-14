from functools import reduce
prod=lambda xs: reduce(lambda a,b:a*b, xs, 1)
import numpy as np, torch, torch.nn as nn
torch.manual_seed(0)

class Kernel(nn.Module):
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__()
        self.input_shape=tuple(input_shape); self.output_shape=tuple(output_shape)
        self.input_dim=input_dim; self.output_dim=output_dim

class LinearKernel(Kernel):
    def __init__(self, input_shape, output_shape, input_dim, output_dim, **kw):
        super().__init__(input_shape, output_shape, input_dim, output_dim, **kw)
        self.fc=nn.Linear(prod(input_shape)*input_dim, prod(output_shape)*output_dim)
    def forward(self,x):
        x=x.reshape(-1, prod(self.input_shape)*self.input_dim)
        x=self.fc(x)
        return x.reshape(-1, *self.output_shape, self.output_dim)

KERNEL_MAP={'linear':LinearKernel}

class KernelWrapper(nn.Module):
    def __init__(self, kernel_cls, input_shape, output_shape, input_dim, output_dim, mode='encode', unet_skip=True, **kw):
        super().__init__()
        self.input_shape=tuple(input_shape); self.output_shape=tuple(output_shape)
        self.input_dim=input_dim; self.output_dim=output_dim
        self.mode=mode; self.unet_skip=unet_skip; self._skip_saved=None
        kcls=KERNEL_MAP[kernel_cls] if isinstance(kernel_cls,str) else kernel_cls
        self.kernel=kcls(input_shape, output_shape, input_dim, output_dim, **kw)
    def forward(self,x):
        x=x.reshape(-1, *self.input_shape, self.input_dim)
        if self.unet_skip and self.mode=='encode': self._skip_saved=x
        x=self.kernel(x)
        x=x.reshape(-1, *self.output_shape, self.output_dim)
        if self.unet_skip and self.mode=='decode': x=x+self._skip_saved
        return x

def two_factors(L):
    a=int(round(L**0.5))
    while L%a: a-=1
    return (L//a, a)

class SimpleKUNet(nn.Module):
    def __init__(self, L, H, C, kernel='linear', hidden_dim=32, latent_dim=64, unet_skip=True):
        super().__init__()
        assert H==L, 'simple 2-layer KUN assumes H==L'
        k1,k2=two_factors(L); self.k1,self.k2,self.C,self.L=k1,k2,C,L
        self.enc1=KernelWrapper(kernel,(k1,),(1,),C,hidden_dim,mode='encode',unet_skip=unet_skip)
        self.enc2=KernelWrapper(kernel,(k2,),(1,),hidden_dim,latent_dim,mode='encode',unet_skip=unet_skip)
        self.dec1=KernelWrapper(kernel,(1,),(k2,),latent_dim,hidden_dim,mode='decode',unet_skip=unet_skip)
        self.dec2=KernelWrapper(kernel,(1,),(k1,),hidden_dim,C,mode='decode',unet_skip=unet_skip)
    def forward(self,x):
        B=x.shape[0]; k1,k2,C=self.k1,self.k2,self.C
        e1=self.enc1(x.reshape(B*k2,k1,C)).reshape(B,k2,-1)
        z=self.enc2(e1)
        self.dec1._skip_saved=self.enc2._skip_saved
        self.dec2._skip_saved=self.enc1._skip_saved
        d1=self.dec1(z).reshape(B*k2,1,-1)
        d2=self.dec2(d1)
        return d2.reshape(B,self.L,C)

for L in [32,64,128,256]:
    print('L=',L,'factors',two_factors(L))
    m=SimpleKUNet(L,L,2); x=torch.randn(4,L,2); y=m(x); assert y.shape==(4,L,2),y.shape
    y.sum().backward(); print('  forward/backward ok', tuple(y.shape))

# quick train sanity on a sine
L=32; n=4000; t=np.arange(n)
data=np.stack([np.sin(2*np.pi*t/13),np.cos(2*np.pi*t/17)],1).astype('float32')
def mw(d,L,H):
    X,Y=[],[]
    for i in range(len(d)-L-H+1): X.append(d[i:i+L]); Y.append(d[i+L:i+L+H])
    return np.array(X,'float32'),np.array(Y,'float32')
X,Y=mw(data,L,L); k=int(len(X)*0.8); Xtr,Ytr,Xte,Yte=X[:k],Y[:k],X[k:],Y[k:]
m=SimpleKUNet(L,L,2); opt=torch.optim.Adam(m.parameters(),1e-3); lf=nn.MSELoss()
Xt=torch.from_numpy(Xtr); Yt=torch.from_numpy(Ytr)
for ep in range(30):
    for i in range(0,len(Xt),64):
        opt.zero_grad(); loss=lf(m(Xt[i:i+64]),Yt[i:i+64]); loss.backward(); opt.step()
m.eval()
with torch.no_grad(): pred=m(torch.from_numpy(Xte)).numpy()
print('SimpleKUNet test RMSE %.4f'%np.sqrt(((pred-Yte)**2).mean()))
print('ALL OK')
