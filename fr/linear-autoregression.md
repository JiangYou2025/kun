---
updated: "2026-06-11"
lang: fr
ref: linear-autoregression
permalink: /fr/linear-autoregression/
title: "Prévision autorégressive avec des modèles linéaires"
lead: "L'autorégression est l'idée la plus ancienne, et la plus centrale, de la prévision de séries temporelles : prédire linéairement la valeur suivante à partir de quelques valeurs passées. Cette page expose d'abord les mathématiques de l'autorégression (AR) et un petit exemple, puis montre que le « modèle linéaire » moderne n'en est que la généralisation à plusieurs pas en une seule fois — c'est précisément l'embryon du « noyau linéaire » de KUN présenté à la page suivante."
prev: math-ml-foundations
next: kun
math: true
---

## 1. L'autorégression : prédire le futur par le passé

L'hypothèse la plus naïve est aussi la plus profonde : **le futur d'une série est une combinaison linéaire de son propre passé.** C'est le **modèle autorégressif (AutoRegressive, AR)**.

Un modèle autorégressif d'ordre $$p$$, noté $$\text{AR}(p)$$, s'écrit :

$$x_t = c + \phi_1 x_{t-1} + \phi_2 x_{t-2} + \cdots + \phi_p x_{t-p} + \varepsilon_t$$

- $$x_{t-1}, \ldots, x_{t-p}$$ sont les $$p$$ dernières observations (la **fenêtre de rétrospection**) ;
- $$\phi_1, \ldots, \phi_p$$ sont les **poids** à apprendre, $$c$$ est le terme constant ;
- $$\varepsilon_t$$ est un bruit aléatoire imprévisible (bruit blanc).

Prédire, c'est laisser tomber le terme de bruit et faire la somme pondérée avec les poids appris :

$$\hat{x}_t = c + \phi_1 x_{t-1} + \cdots + \phi_p x_{t-p}$$

### En pratique : cliquez sur la série des taches solaires et voyez ce que « pense » le modèle

Vous vous souvenez des [taches solaires](../applications/geophysics/) ? C'est précisément avec elles que Yule a inventé l'autorégression en 1927. Ci-dessous, sur une série de type taches solaires, on **ajuste en temps réel** par moindres carrés un $$\text{AR}(12)$$ (les 12 dernières valeurs prédisent la suivante). **Cliquez sur n'importe quel point de la courbe** pour voir quelles données le modèle utilise pour le prédire, par quel poids chacune est multipliée et combien chacune contribue.

<div class="game" markdown="0">
<h3 style="margin-top:0">🌞 Cliquez sur un point : quelles 12 valeurs passées le modèle utilise-t-il, et comment les pondère-t-il ?</h3>
<p class="hint">Tous les points à droite de la ligne grise en pointillés sont cliquables. Points bleus = fenêtre historique utilisée pour cette prédiction, cercle jaune = valeur prédite, point plein = valeur réelle.</p>

<canvas id="ar-canvas" width="640" height="300" style="width:100%;max-width:640px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>
<div id="ar-info" style="margin-top:12px;font-size:.9rem"></div>

<style>
#ar-info table{border-collapse:collapse;width:100%;max-width:560px;font-size:.84rem;margin-top:8px}
#ar-info th,#ar-info td{padding:3px 8px;text-align:right;border-bottom:1px solid var(--border)}
#ar-info th:first-child,#ar-info td:first-child{text-align:left}
.wbar{display:inline-block;height:9px;border-radius:2px;vertical-align:middle}
</style>

<script>
(function(){
  var canvas=document.getElementById('ar-canvas');
  if(!canvas) return;
  var ctx=canvas.getContext('2d');
  var info=document.getElementById('ar-info');
  var W=640,H=300,p=12,N=140;
  var ML=40,MR=14,MT=16,MB=26, PW=W-ML-MR, PH=H-MT-MB;
  var i,j,k,t;

  // 1) Générer une série de type taches solaires (déterministe, non négative, cycle d'environ 11 pas)
  var y=[];
  for(t=0;t<N;t++){
    var base=85+72*Math.sin(2*Math.PI*t/11)+24*Math.sin(2*Math.PI*t/5.5+1.0);
    var wig=16*Math.sin(t*1.7)*Math.cos(t*0.41)+10*Math.sin(t*0.9+0.5);
    var v=base+wig; if(v<0)v=0; y.push(v);
  }

  // 2) Résoudre le système linéaire par élimination de Gauss
  function solve(A,b){
    var nn=b.length,r,c,ii;
    for(c=0;c<nn;c++){
      var piv=c;
      for(r=c+1;r<nn;r++) if(Math.abs(A[r][c])>Math.abs(A[piv][c])) piv=r;
      var ta=A[c];A[c]=A[piv];A[piv]=ta; var tb=b[c];b[c]=b[piv];b[piv]=tb;
      var d=A[c][c]; if(Math.abs(d)<1e-9) d=d<0?-1e-9:1e-9;
      for(r=0;r<nn;r++){ if(r===c) continue; var f=A[r][c]/d; for(ii=c;ii<nn;ii++) A[r][ii]-=f*A[c][ii]; b[r]-=f*b[c]; }
    }
    var x=[]; for(ii=0;ii<nn;ii++) x.push(b[ii]/A[ii][ii]); return x;
  }

  // 3) Ajustement AR(p) par moindres carrés (avec ordonnée à l'origine + léger ridge pour stabiliser les poids)
  var n=p+1, A=[], bv=[];
  for(i=0;i<n;i++){ A.push(new Array(n).fill(0)); bv.push(0); }
  for(t=p;t<N;t++){
    var feat=[1]; for(k=1;k<=p;k++) feat.push(y[t-k]);
    for(i=0;i<n;i++){ for(j=0;j<n;j++) A[i][j]+=feat[i]*feat[j]; bv[i]+=feat[i]*y[t]; }
  }
  var md=0; for(i=1;i<n;i++) md+=A[i][i]; md/=p;
  for(i=1;i<n;i++) A[i][i]+=0.05*md;
  var coef=solve(A,bv);   // coef[0] = ordonnée à l'origine, coef[k] = poids du retard k

  function predict(tt){ var s=coef[0]; for(var kk=1;kk<=p;kk++) s+=coef[kk]*y[tt-kk]; return s; }

  var ymin=Math.min.apply(null,y), ymax=Math.max.apply(null,y), TAU=Math.PI*2;
  function X(idx){ return ML+PW*idx/(N-1); }
  function Y(val){ return MT+PH*(1-(val-ymin)/(ymax-ymin)); }

  var sel=N-1;

  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.4)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(X(p-0.5),MT);ctx.lineTo(X(p-0.5),MT+PH);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';ctx.fillText('≥ 12 valeurs passées requises',X(p)+4,MT+12);

    if(sel!==null){ ctx.fillStyle='rgba(129,140,248,0.13)';ctx.fillRect(X(sel-p),MT,X(sel-1)-X(sel-p),PH); }

    ctx.strokeStyle='#5eead4';ctx.lineWidth=2;ctx.beginPath();
    for(i=0;i<N;i++){ var xx=X(i),yy=Y(y[i]); if(i===0)ctx.moveTo(xx,yy); else ctx.lineTo(xx,yy); }
    ctx.stroke();
    for(i=0;i<N;i++){ ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(X(i),Y(y[i]),1.8,0,TAU);ctx.fill(); }

    if(sel!==null){
      for(k=1;k<=p;k++){ var id=sel-k; ctx.fillStyle='#818cf8';ctx.beginPath();ctx.arc(X(id),Y(y[id]),3.4,0,TAU);ctx.fill(); }
      ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(X(sel),Y(y[sel]),4,0,TAU);ctx.fill();
      var pv=predict(sel);
      ctx.strokeStyle='rgba(251,191,36,0.55)';ctx.setLineDash([2,3]);ctx.lineWidth=1.5;
      ctx.beginPath();ctx.moveTo(X(sel),Y(pv));ctx.lineTo(X(sel),Y(y[sel]));ctx.stroke();ctx.setLineDash([]);
      ctx.strokeStyle='#fbbf24';ctx.lineWidth=2;ctx.beginPath();ctx.arc(X(sel),Y(pv),5,0,TAU);ctx.stroke();
    }
  }

  function renderInfo(){
    if(sel===null){ info.innerHTML=''; return; }
    var pv=predict(sel), av=y[sel], maxc=0, kk, rows='';
    for(kk=1;kk<=p;kk++){ var cc=Math.abs(coef[kk]*y[sel-kk]); if(cc>maxc)maxc=cc; }
    for(kk=1;kk<=p;kk++){
      var w=coef[kk], val=y[sel-kk], contr=w*val;
      var bw=maxc>0?Math.round(Math.abs(contr)/maxc*64):0;
      var col=contr>=0?'#5eead4':'#ef4444';
      rows+='<tr><td>x<sub>t−'+kk+'</sub></td><td>'+w.toFixed(3)+'</td><td>'+val.toFixed(1)+'</td><td>'+contr.toFixed(1)+'</td><td><span class="wbar" style="width:'+bw+'px;background:'+col+'"></span></td></tr>';
    }
    info.innerHTML='<div>Prédiction du point <strong>t = '+sel+'</strong> : ŷ = ordonnée à l\'origine '+coef[0].toFixed(1)+' + Σ(poids × valeur passée) = <strong style="color:#fbbf24">'+pv.toFixed(1)+'</strong> · valeur réelle <strong style="color:#5eead4">'+av.toFixed(1)+'</strong> (erreur '+(pv-av>=0?'+':'')+(pv-av).toFixed(1)+')</div>'+
      '<table><thead><tr><th>Valeur passée utilisée</th><th>Poids w</th><th>Valeur x</th><th>Contribution w·x</th><th></th></tr></thead><tbody>'+rows+'</tbody></table>';
  }

  canvas.addEventListener('click',function(e){
    var rect=canvas.getBoundingClientRect();
    var cx=(e.clientX-rect.left)*(W/rect.width);
    var idx=Math.round((cx-ML)/PW*(N-1));
    if(idx<p)idx=p; if(idx>N-1)idx=N-1;
    sel=idx; draw(); renderInfo();
  });

  draw(); renderInfo();
})();
</script>
</div>

> **Vous voyez le mécanisme ?** Le même jeu de poids $$w_1,\dots,w_{12}$$ **sert à tous les instants** — c'est la « loi apprise » par le modèle ; quand vous cliquez sur différents points, seules changent les 12 valeurs passées auxquelles il s'applique, si bien que la « décomposition des contributions » diffère d'un point à l'autre. Étendez cette unique somme pondérée pour produire « $$H$$ sorties à la fois » et vous obtenez le **modèle linéaire** présenté plus loin ; empilez-le ensuite en une hiérarchie en U et vous obtenez **KUN**.

### Le cas le plus simple : AR(1)

$$x_t = c + \phi\, x_{t-1} + \varepsilon_t$$

Un seul coefficient $$\phi$$ détermine le « caractère » de la série :

- **−1 < φ < 1** (c'est-à-dire |φ| inférieur à 1) : la série est **stationnaire** et sans cesse ramenée vers sa moyenne de long terme μ = c/(1−φ) — c'est le **retour à la moyenne** (taux d'intérêt, températures, stocks se comportent souvent ainsi).
- **φ = 1** : on obtient une **marche aléatoire** (valeur suivante = valeur précédente + bruit aléatoire), sans force de rappel ; c'est ainsi qu'on modélise souvent, en première approximation, le cours des actions.
- **φ > 1 ou φ < −1** (|φ| supérieur à 1) : la série diverge, ce qui est rare dans la réalité.

Transformons le « retour à la moyenne » en un **petit graphique interactif** pour voir de vos propres yeux une valeur ramenée pas à pas vers la diagonale 👇

<div class="game" markdown="0">
<h3 style="margin-top:0">🎯 Mini-jeu du retour à la moyenne : un clic, un pas — regardez-la regagner la diagonale</h3>
<p class="hint">Voici un AR(1) : <b>x' = c + φ·x</b> (moyenne de long terme μ = c/(1−φ) ; tous les jeux de paramètres ci-dessous donnent μ = 10). <strong>Chaque clic sur le graphique effectue une itération</strong> : le trait vertical rejoint la droite AR (= calcul de la valeur suivante), le trait horizontal revient sur la <b>diagonale y = x</b>. Cliquez plusieurs fois : la ligne brisée bleue converge vers l'intersection de la diagonale et de la droite AR — c'est μ. Cliquez sur <strong>« Changer de paramètres »</strong> pour essayer d'autres valeurs de φ : <b>plus φ est proche de 1, plus la remontée est lente</b> ; <b>si φ est négatif, la convergence se fait en spirale autour de μ</b>.</p>
<canvas id="cw-canvas" width="352" height="344" style="width:100%;max-width:352px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:pointer"></canvas>
<div style="margin-top:10px"><button id="cw-reset">Changer de paramètres</button> <span id="cw-info" style="font-size:.9rem;color:var(--muted)"></span></div>

<style>
#cw-reset{padding:5px 12px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;font-size:.86rem}
#cw-reset:hover{opacity:.85}
</style>

<script>
(function(){
  var cv=document.getElementById('cw-canvas'); if(!cv) return;
  var ctx=cv.getContext('2d'); var info=document.getElementById('cw-info');
  var W=352,H=344, ML=38,MR=14,MT=14,MB=30, PW=W-ML-MR, PH=H-MT-MB;
  var XMAX=20, TAU=Math.PI*2;
  // Un jeu de paramètres : μ vaut toujours 10, seul φ change — observez comment le chemin varie
  var PARAMS=[
    {c:4,  phi:0.6},   // vitesse moyenne, remontée monotone
    {c:7,  phi:0.3},   // convergence très rapide
    {c:1.5,phi:0.85},  // convergence très lente
    {c:13, phi:-0.3},  // légère spirale d'aller-retour
    {c:16, phi:-0.6}   // spirale marquée autour de μ
  ];
  var pidx=0, c=PARAMS[0].c, phi=PARAMS[0].phi, mu=c/(1-phi);
  function f(x){ return c+phi*x; }
  function gx(v){ return ML+PW*v/XMAX; }
  function gy(v){ return MT+PH*(1-v/XMAX); }
  var pts=[], steps=0;

  function status(){
    var cur=pts[pts.length-1][0];
    info.innerHTML='φ = '+phi.toFixed(2)+', c = '+c.toFixed(1)+' (μ = '+mu.toFixed(0)+') · pas '+steps+' : x = '+cur.toFixed(2)+', encore '+Math.abs(cur-mu).toFixed(2)+' de μ';
  }
  function draw(){
    ctx.clearRect(0,0,W,H);
    ctx.strokeStyle='rgba(150,160,180,0.25)';ctx.lineWidth=1;ctx.strokeRect(ML,MT,PW,PH);
    // Axes : axe x (bord inférieur), axe y (bord gauche) + graduations + origine O
    ctx.strokeStyle='rgba(150,160,180,0.7)';ctx.lineWidth=1.3;
    ctx.beginPath();
    ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(XMAX),gy(0));
    ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(0),gy(XMAX));
    ctx.stroke();
    ctx.fillStyle='#9aa3b2';ctx.font='10px sans-serif';
    for(var tk=5;tk<=XMAX;tk+=5){
      ctx.beginPath();ctx.moveTo(gx(tk),gy(0));ctx.lineTo(gx(tk),gy(0)+4);ctx.stroke();
      ctx.beginPath();ctx.moveTo(gx(0),gy(tk));ctx.lineTo(gx(0)-4,gy(tk));ctx.stroke();
      ctx.fillText(tk,gx(tk)-5,gy(0)+15);
      ctx.fillText(tk,gx(0)-20,gy(tk)+3);
    }
    ctx.fillStyle='#9aa3b2';ctx.beginPath();ctx.arc(gx(0),gy(0),2.6,0,TAU);ctx.fill();
    ctx.fillText('O',gx(0)-11,gy(0)+13);
    ctx.strokeStyle='rgba(150,160,180,0.75)';ctx.setLineDash([5,4]);ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(gx(0),gy(0));ctx.lineTo(gx(XMAX),gy(XMAX));ctx.stroke();ctx.setLineDash([]);
    ctx.strokeStyle='#818cf8';ctx.lineWidth=2;
    ctx.beginPath();ctx.moveTo(gx(0),gy(f(0)));ctx.lineTo(gx(XMAX),gy(f(XMAX)));ctx.stroke();
    ctx.fillStyle='#fbbf24';ctx.beginPath();ctx.arc(gx(mu),gy(mu),5,0,TAU);ctx.fill();
    ctx.strokeStyle='#5eead4';ctx.lineWidth=1.8;ctx.beginPath();
    for(var i=0;i<pts.length;i++){ var px=gx(pts[i][0]),py=gy(pts[i][1]); if(i===0)ctx.moveTo(px,py); else ctx.lineTo(px,py); }
    ctx.stroke();
    var last=pts[pts.length-1];
    ctx.fillStyle='#5eead4';ctx.beginPath();ctx.arc(gx(last[0]),gy(last[1]),4,0,TAU);ctx.fill();
    ctx.font='11px sans-serif';
    ctx.fillStyle='#9aa3b2';ctx.fillText('y = x',gx(XMAX)-32,gy(XMAX)+13);
    ctx.fillStyle='#818cf8';ctx.fillText('x → c+φx',gx(XMAX)-60,gy(f(XMAX))-6);
    ctx.fillStyle='#fbbf24';ctx.fillText('μ',gx(mu)+7,gy(mu)+4);
    ctx.fillStyle='#9aa3b2';ctx.fillText('x (actuel)',ML+PW/2-22,H-9);
    ctx.save();ctx.translate(12,MT+PH/2+26);ctx.rotate(-TAU/4);ctx.fillText("x' (suivant)",0,0);ctx.restore();
    ctx.fillStyle='#818cf8';ctx.font='12px sans-serif';ctx.fillText('φ = '+phi.toFixed(2),ML+6,MT+14);
  }
  var MAXSTEPS=14;
  function step(){
    if(steps>=MAXSTEPS) return;
    var x=pts[pts.length-1][0], fx=f(x);
    pts.push([x,fx]); pts.push([fx,fx]); steps++;
    draw(); status();
  }
  function reset(start){
    var x0=(start==null)?(2+Math.random()*16):start;
    pts=[[x0,x0]]; steps=0; draw(); status();
  }
  cv.addEventListener('click',step);
  document.getElementById('cw-reset').addEventListener('click',function(){
    pidx=(pidx+1)%PARAMS.length;
    c=PARAMS[pidx].c; phi=PARAMS[pidx].phi; mu=c/(1-phi);
    reset(17);
  });
  reset(17);
})();
</script>
</div>

### Ce n'est en fait qu'une régression linéaire

Prenez la fenêtre de rétrospection comme variables explicatives et la valeur suivante comme cible : l'AR devient une **régression linéaire** standard, qui prédit $$x_t$$ à partir de $$(x_{t-1}, \ldots, x_{t-p})$$. En **faisant glisser pas à pas** cette fenêtre le long de la série, on obtient une à une les lignes d'exemples d'entraînement — $$(x_1,\ldots,x_p)\to x_{p+1}$$, $$(x_2,\ldots,x_{p+1})\to x_{p+2}$$, et ainsi de suite.

Les paramètres se calculent alors directement par **moindres carrés** (la statistique classique utilise aussi les **équations de Yule–Walker**, les deux approches étant équivalentes). C'est exactement le « trouver la meilleure loi par optimisation » de l'[étape 4](../math-ml-foundations/), appliqué aux séries temporelles sous la forme d'un premier modèle concret.

## 2. Du pas unique aux pas multiples : le modèle linéaire

L'AR classique ne prédit **qu'un pas à la fois**. Pour prédire $$H$$ pas dans le futur, l'approche traditionnelle est **récursive** : on prédit $$\hat{x}_{t}$$, puis on le réinjecte comme s'il s'agissait d'une vraie valeur pour prédire $$\hat{x}_{t+1}$$… mais l'erreur de chaque pas **s'accumule de proche en proche**.

L'approche moderne est plus directe : **prédire d'un seul coup tout le segment futur**. C'est ce qu'on appelle le « **modèle linéaire** » : **une seule couche linéaire** (matrice de poids $$W$$, biais $$b$$) envoie en une fois la fenêtre de rétrospection de longueur $$L$$, $$x_{t-L+1:t}$$, sur le futur de longueur $$H$$, $$\hat{x}_{t+1:t+H}$$ :

$$\hat{x}_{t+1:t+H} \;=\; W\,x_{t-L+1:t} + b, \qquad W \in \mathbb{R}^{H \times L},\; b \in \mathbb{R}^{H}$$

L'entrée est formée de $$L$$ valeurs passées, la sortie de $$H$$ valeurs futures, et $$W$$ est une matrice de poids $$H \times L$$. Développée pour chaque instant futur, elle donne $$H$$ sommes pondérées côte à côte :

$$\hat{x}_{t+h} \;=\; \sum_{i=1}^{L} W_{h,i}\,x_{t-L+i} + b_h, \qquad h = 1, 2, \dots, H$$

Chaque $$\hat{x}_{t+h}$$ est **une somme pondérée de toute la fenêtre de rétrospection** — c'est précisément la « version agrandie » de la somme pondérée de l'AR : l'AR classique n'en est que le cas particulier $$H=1$$ (une seule ligne de sortie) et $$L=p$$.

La comparaison montre qu'il s'agit d'une seule et même idée à deux échelles :

| | AR classique | Modèle linéaire |
|---|---|---|
| Entrée | Les $$p$$ dernières valeurs | Les $$L$$ dernières valeurs (fenêtre de rétrospection) |
| Sortie | **1** valeur (le pas suivant) | **$$H$$** valeurs (tout le segment futur) |
| Nature | Application linéaire de dimension $$1$$ | Application linéaire $$L \to H$$ |
| Multi-pas | Récursif, l'erreur s'accumule | Sortie multiple directe, sans accumulation |

En une phrase : **le modèle linéaire est une autorégression vectorisée, à sorties multiples.** Il suffit d'étendre la somme pondérée de l'AR, de « calculer un nombre » à « calculer toute une rangée de nombres d'un coup ».

Mais au juste, quel écart y a-t-il entre « la récursion accumule l'erreur » et « la sortie multiple directe ne l'accumule pas » ? Cliquez pour voir 👇

<div class="game" markdown="0">
<h3 style="margin-top:0">🔮 Cliquez sur un instant : comparez « récursif pas à pas » et « sortie multiple directe »</h3>
<p class="hint"><strong>Cliquez sur la courbe pour choisir un point de départ t</strong> : les deux modèles utilisent les <b>L = 16</b> valeurs qui le précèdent et prédisent <b>H = 18</b> pas en avant : <span style="color:#818cf8;font-weight:600">bleu = sortie multiple directe</span> (une couche linéaire calcule tout le segment d'un coup), <span style="color:#f59e0b;font-weight:600">orange = récursif pas à pas</span> (on prédit un pas, on le réinjecte comme vraie valeur, puis on prédit le suivant), <span style="color:#5eead4;font-weight:600">cyan = futur réel</span>. Observez comme l'orange dérive de plus en plus à mesure qu'on avance.</p>

<canvas id="ms-canvas" width="640" height="320" style="width:100%;max-width:640px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>
<div id="ms-info" style="margin-top:10px;font-size:.9rem;color:var(--muted)"></div>

<script>
(function(){
  var cv=document.getElementById('ms-canvas'); if(!cv) return;
  var ctx=cv.getContext('2d'); var info=document.getElementById('ms-info');
  var W=640,CH=320, ML=42,MR=12,MT=16,MB=28, PW=W-ML-MR, PH=CH-MT-MB;
  var N=170, L=16, H=18, TAU=Math.PI*2;
  var i,j,k,t,h;

  // Une série à deux périodes incommensurables + une composante irrégulière : la période 23 dépasse L = 16, le modèle à un pas ne peut pas l'ajuster parfaitement
  var y=[];
  for(t=0;t<N;t++){
    var b=52+26*Math.sin(TAU*t/23)+13*Math.sin(TAU*t/9+0.6);
    var irr=7*Math.sin(t*0.7)*Math.cos(t*0.27)+5*Math.sin(t*1.3+0.4);
    y.push(b+irr);
  }

  function solve(A,b){
    var nn=b.length,r,c,ii;
    for(c=0;c<nn;c++){
      var piv=c;
      for(r=c+1;r<nn;r++) if(Math.abs(A[r][c])>Math.abs(A[piv][c])) piv=r;
      var ta=A[c];A[c]=A[piv];A[piv]=ta; var tb=b[c];b[c]=b[piv];b[piv]=tb;
      var d=A[c][c]; if(Math.abs(d)<1e-9) d=d<0?-1e-9:1e-9;
      for(r=0;r<nn;r++){ if(r===c) continue; var fa=A[r][c]/d; for(ii=c;ii<nn;ii++) A[r][ii]-=fa*A[c][ii]; b[r]-=fa*b[c]; }
    }
    var x=[]; for(ii=0;ii<nn;ii++) x.push(b[ii]/A[ii][ii]); return x;
  }
  function fit(rows,tgt,m){   // moindres carrés avec léger ridge
    var A=[],bv=[],r,a,ii;
    for(a=0;a<m;a++){ A.push(new Array(m).fill(0)); bv.push(0); }
    for(r=0;r<rows.length;r++){ var fr=rows[r],tv=tgt[r];
      for(a=0;a<m;a++){ for(ii=0;ii<m;ii++) A[a][ii]+=fr[a]*fr[ii]; bv[a]+=fr[a]*tv; } }
    var md=0; for(a=1;a<m;a++) md+=A[a][a]; md/=(m-1);
    for(a=1;a<m;a++) A[a][a]+=0.04*md;
    return solve(A,bv);
  }

  // AR(L) à un pas — utilisé pour la récursion
  var rA=[],tA=[];
  for(t=L;t<N;t++){ var fr=[1]; for(k=1;k<=L;k++) fr.push(y[t-k]); rA.push(fr); tA.push(y[t]); }
  var coefAR=fit(rA,tA,L+1);

  // Sortie multiple directe — un modèle linéaire entraîné par horizon (= une ligne de la matrice W)
  var coefDir=[];
  for(h=1;h<=H;h++){
    var rows=[],tg=[];
    for(t=L-1;t+h<N;t++){ var fr=[1]; for(i=0;i<L;i++) fr.push(y[t-L+1+i]); rows.push(fr); tg.push(y[t+h]); }
    coefDir.push(fit(rows,tg,L+1));
  }

  function recursive(o){
    var hist=[]; for(k=0;k<L;k++) hist.push(y[o-k]);   // hist[0] = y[o] (retard 1)
    var out=[];
    for(h=0;h<H;h++){ var s=coefAR[0]; for(k=1;k<=L;k++) s+=coefAR[k]*hist[k-1];
      out.push(s); hist.unshift(s); hist.pop(); }
    return out;
  }
  function direct(o){
    var out=[];
    for(h=1;h<=H;h++){ var c=coefDir[h-1],s=c[0]; for(i=0;i<L;i++) s+=c[i+1]*y[o-L+1+i]; out.push(s); }
    return out;
  }

  var ymin=Math.min.apply(null,y), ymax=Math.max.apply(null,y), pad=(ymax-ymin)*0.08;
  ymin-=pad; ymax+=pad;
  function X(idx){ return ML+PW*idx/(N-1); }
  function Y(v){ return MT+PH*(1-(v-ymin)/(ymax-ymin)); }

  var o=Math.round(N*0.5);

  function draw(){
    ctx.clearRect(0,0,W,CH);
    ctx.fillStyle='rgba(129,140,248,0.10)';ctx.fillRect(X(o-L+1),MT,X(o)-X(o-L+1),PH);
    ctx.strokeStyle='rgba(150,160,180,0.6)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(X(o),MT);ctx.lineTo(X(o),MT+PH);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';
    ctx.fillText('départ t',X(o)+4,MT+11);
    ctx.fillText('fenêtre L='+L,X(o-L+1)+2,MT+PH-5);

    ctx.strokeStyle='#5eead4';ctx.lineWidth=2;ctx.beginPath();
    for(i=0;i<N;i++){ var xx=X(i),yy=Y(y[i]); if(i===0)ctx.moveTo(xx,yy); else ctx.lineTo(xx,yy); }
    ctx.stroke();

    var dr=direct(o), rc=recursive(o);
    function fc(arr,col){
      ctx.strokeStyle=col;ctx.lineWidth=2;ctx.setLineDash([5,3]);ctx.beginPath();
      ctx.moveTo(X(o),Y(y[o]));
      for(h=1;h<=H;h++) ctx.lineTo(X(o+h),Y(arr[h-1]));
      ctx.stroke();ctx.setLineDash([]);
      for(h=1;h<=H;h++){ ctx.fillStyle=col;ctx.beginPath();ctx.arc(X(o+h),Y(arr[h-1]),2.2,0,TAU);ctx.fill(); }
    }
    fc(dr,'#818cf8'); fc(rc,'#f59e0b');

    var maeD=0,maeR=0;
    for(h=1;h<=H;h++){ var tv=y[o+h]; maeD+=Math.abs(dr[h-1]-tv); maeR+=Math.abs(rc[h-1]-tv); }
    maeD/=H; maeR/=H;
    info.innerHTML='Point de départ <strong style="color:var(--text)">t='+o+'</strong>, erreur moyenne sur les <strong style="color:var(--text)">H='+H+'</strong> pas suivants : '+
      '<span style="color:#818cf8;font-weight:600">directe '+maeD.toFixed(2)+'</span> vs '+
      '<span style="color:#f59e0b;font-weight:600">récursive '+maeR.toFixed(2)+'</span>'+
      (maeR>maeD?' → la récursive est plus grande, et dérive de plus en plus (l\'erreur s\'accumule de proche en proche)':'');
  }

  cv.addEventListener('click',function(e){
    var rect=cv.getBoundingClientRect();
    var cx=(e.clientX-rect.left)*(W/rect.width);
    var idx=Math.round((cx-ML)/PW*(N-1));
    if(idx<L-1)idx=L-1; if(idx>N-1-H)idx=N-1-H;
    o=idx; draw();
  });
  draw();
})();
</script>
</div>

Ne sous-estimez pas une structure aussi simple : avec une seule couche linéaire, on fait jeu égal, voire mieux, avec des modèles bien plus complexes sur plusieurs bancs d'essai de séries longues (voir la [leçon 10](../course/10/) du cours), ce qui a conduit tout le domaine à redécouvrir que **l'application linéaire est en soi une référence (baseline) extrêmement solide**.

## 3. Vers KUN

À ce stade, la puissance de l'autorégression linéaire est manifeste, mais elle a aussi un plafond : **une seule couche linéaire ne voit qu'une seule échelle**. Les séries réelles cachent souvent à la fois une tendance de long terme, des cycles de moyen terme et des détails de haute fréquence (multi-échelle).

**KUN (Kernel U-Net)**, présenté à la page suivante, prend justement l'« application linéaire » vue ici comme un **noyau interchangeable**, puis l'empile en une hiérarchie en U — la même idée se trouve ainsi généralisée à plusieurs échelles. Autrement dit, **vous maîtrisez déjà la brique la plus élémentaire de KUN**.

---

**Termes clés (Key terms) :** autorégression AR(p), AR(1) et retour à la moyenne, marche aléatoire, moindres carrés / Yule–Walker, fenêtre de rétrospection, multi-pas récursif vs direct, modèle linéaire, noyau linéaire.
