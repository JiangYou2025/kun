---
updated: "2026-06-04"
lang: fr
ref: prediction-in-action
permalink: /fr/prediction-in-action/
title: "Une prédiction réussie"
lead: "Quelle est l'essence d'une prédiction ? À partir des observations dont on dispose, trouver une loi, puis la prolonger là où l'on n'a encore rien vu. Cette page vous le fait vivre à travers un petit jeu de tir d'artillerie : ajuster les paramètres → ajuster la trajectoire → toucher la cible."
prev: forecasting
next: math-ml-foundations
---

## Prédire = ajuster + extrapoler

La page précédente nous a montré que la prédiction est partout. Mais comment prédit-on, concrètement ?

L'idée la plus simple tient en deux étapes :

1. **Ajuster (Fit)** : trouver une courbe qui passe au plus près des points de données déjà connus.
2. **Extrapoler (Extrapolate)** : prolonger cette courbe vers le futur pour obtenir les valeurs prédites.

C'est exactement comme un tir d'artillerie : vous observez la trajectoire de quelques obus, vous réglez la **position de départ** et l'**angle de tir** du canon pour que la courbe balistique épouse ces points observés, et vous finissez par toucher la cible au loin.

## 🎯 Tir d'artillerie : à vous de prédire la trajectoire

<div class="game" markdown="0">
  <h3 style="margin-top:0">Réglez le canon et touchez la cible !</h3>
  <p class="hint">L'écran montre des <strong>points observés bleus</strong> (données balistiques connues) et une <strong>cible rouge</strong> (l'objectif). Faites glisser les curseurs pour régler la <strong>position horizontale</strong> et l'<strong>angle de tir</strong> du canon. La ligne d'aide ne montre que la première moitié de la trajectoire : où tombe la seconde moitié, c'est à vous d'en juger ! 5 niveaux au total, avec un bruit de plus en plus fort.</p>

  <canvas id="art-canvas" width="560" height="260" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface);cursor:crosshair"></canvas>

  <div style="display:flex;flex-wrap:wrap;gap:18px;margin:14px 0;align-items:center">
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">Position horizontale du canon x₀</span>
      <input type="range" id="art-x0" min="0" max="100" value="0" step="1" style="width:100%">
      <span id="art-x0-val" style="font-size:.85rem;font-weight:600">0</span>
    </label>
    <label style="flex:1;min-width:220px">
      <span style="font-size:.9rem;color:var(--muted)">Angle de tir θ</span>
      <input type="range" id="art-angle" min="15" max="80" value="45" step="0.5" style="width:100%">
      <span id="art-angle-val" style="font-size:.85rem;font-weight:600">45°</span>
    </label>
  </div>
  <div class="bar2" style="display:flex;gap:12px;align-items:center;flex-wrap:wrap">
    <button id="art-fire" type="button" style="padding:8px 24px;font-size:1rem;font-weight:600;border-radius:6px;background:var(--accent);color:var(--bg);border:none;cursor:pointer">🚀 Feu !</button>
    <span id="art-msg" style="font-size:.95rem"></span>
    <span id="art-score" style="margin-left:auto;font-size:.9rem;color:var(--muted)"></span>
  </div>

  <script>
  (function(){
    var canvas=document.getElementById('art-canvas');
    if(!canvas)return;
    var ctx=canvas.getContext('2d');
    var W=560,H=260,g=9.8,V0=80;
    var x0S=document.getElementById('art-x0'),angleS=document.getElementById('art-angle');
    var x0V=document.getElementById('art-x0-val'),angleV=document.getElementById('art-angle-val');
    var fireBtn=document.getElementById('art-fire'),msgEl=document.getElementById('art-msg'),scoreEl=document.getElementById('art-score');

    // Chaque niveau : x0 et angle réels (vitesse fixe V0, hauteur = 0)
    var levels=[
      {x0:10, angle:50, name:'Niveau 1 · Données précises',   nObs:7, noise:1},
      {x0:25, angle:42, name:'Niveau 2 · Léger bruit',   nObs:6, noise:4},
      {x0:5,  angle:62, name:'Niveau 3 · Bruit plus fort',   nObs:5, noise:10},
      {x0:35, angle:35, name:'Niveau 4 · Données éparses',   nObs:3, noise:12},
      {x0:15, angle:55, name:'Niveau 5 · Bruit extrême',   nObs:3, noise:22}
    ];
    var cur=0,total=0,fired=false,sc=1;
    var GND=H-26; // y du sol en pixels

    function rad(d){return d*Math.PI/180;}

    // Parabole partant de x0, angle a, vitesse V0, y0 = 0
    function traj(x0,a){
      var r=rad(a),vx=V0*Math.cos(r),vy=V0*Math.sin(r),pts=[];
      for(var i=0;i<=500;i++){
        var t=i*0.04;
        var x=x0+vx*t, y=vy*t-0.5*g*t*t;
        if(y<0&&i>0){pts.push({x:x,y:0});break;}
        pts.push({x:x,y:y});
      }
      return pts;
    }

    function genLv(){
      var lv=levels[cur], real=traj(lv.x0,lv.angle);
      var nObs=lv.nObs||5, noise=lv.noise||2;
      var n=Math.floor(real.length*0.55),obs=[];
      for(var i=0;i<nObs;i++){
        var idx=Math.floor((i+0.5)*n/nObs);
        var p=real[idx];
        obs.push({x:p.x,y:p.y+(Math.random()-0.5)*noise});
      }
      var last=real[real.length-1];
      // Mise à l'échelle automatique : toute la trajectoire et la cible restent à l'écran
      var maxX=0,maxY=0;
      real.forEach(function(p){if(p.x>maxX)maxX=p.x;if(p.y>maxY)maxY=p.y;});
      maxX=Math.max(maxX,last.x)*1.15; // 15 % de marge pour les décalages du joueur
      maxY=maxY*1.2;
      sc=(W-50)/maxX;
      var scY=(H-50)/maxY;
      if(scY<sc) sc=scY;
      return {obs:obs,target:{x:last.x,y:0},real:real,name:lv.name,maxX:maxX};
    }
    var lv=genLv();

    function sx(x){return 25+x*sc;}
    function sy(y){return GND-y*sc;}

    function draw(ut,showR){
      ctx.clearRect(0,0,W,H);
      ctx.save();ctx.beginPath();ctx.rect(0,0,W,H);ctx.clip();

      // Sol
      ctx.fillStyle='rgba(94,234,212,0.05)';ctx.fillRect(0,GND,W,H-GND);
      ctx.strokeStyle='#262b38';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,GND);ctx.lineTo(W,GND);ctx.stroke();
      ctx.fillStyle='#9aa3b2';ctx.font='11px sans-serif';
      ctx.fillText('Distance →',W-62,H-4);

      // Points observés
      lv.obs.forEach(function(p){
        ctx.beginPath();ctx.arc(sx(p.x),sy(p.y),5,0,Math.PI*2);
        ctx.fillStyle='#5eead4';ctx.fill();
        ctx.strokeStyle='#0f1117';ctx.lineWidth=1.5;ctx.stroke();
      });

      // Cible (au sol)
      var tx=sx(lv.target.x),ty=GND;
      ctx.beginPath();ctx.arc(tx,ty,12,0,Math.PI*2);ctx.fillStyle='rgba(239,68,68,0.15)';ctx.fill();
      ctx.strokeStyle='#ef4444';ctx.lineWidth=2.5;ctx.stroke();
      ctx.beginPath();ctx.arc(tx,ty,3,0,Math.PI*2);ctx.fillStyle='#ef4444';ctx.fill();
      ctx.fillStyle='#ef4444';ctx.font='bold 10px sans-serif';ctx.fillText('Cible',tx+14,ty-4);

      // Canon (au sol)
      var cx0=parseFloat(x0S.value),ca=rad(parseFloat(angleS.value));
      var cannonX=sx(cx0);
      // Affût
      ctx.fillStyle='#e6e8ee';ctx.fillRect(cannonX-6,GND-6,12,6);
      // Tube
      ctx.beginPath();ctx.moveTo(cannonX,GND-3);
      ctx.lineTo(cannonX+Math.cos(ca)*24,GND-3-Math.sin(ca)*24);
      ctx.strokeStyle='#e6e8ee';ctx.lineWidth=3;ctx.stroke();

      // Aperçu en pointillés (première moitié seulement)
      if(!ut){
        var pv=traj(cx0,parseFloat(angleS.value));
        var half=Math.floor(pv.length/2);
        ctx.setLineDash([5,4]);ctx.strokeStyle='#818cf8';ctx.lineWidth=1.5;ctx.beginPath();
        for(var hi=0;hi<half;hi++){if(hi===0)ctx.moveTo(sx(pv[hi].x),sy(pv[hi].y));else ctx.lineTo(sx(pv[hi].x),sy(pv[hi].y));}
        ctx.stroke();ctx.setLineDash([]);
        if(half>0){var hp=pv[half-1];ctx.fillStyle='#818cf8';ctx.font='bold 16px sans-serif';ctx.fillText('?',sx(hp.x)+6,sy(hp.y)-2);}
      }

      // Trajectoire après le tir (trait plein)
      if(ut){
        ctx.strokeStyle='#818cf8';ctx.lineWidth=2.5;ctx.beginPath();
        ut.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();
        var lp=ut[ut.length-1];
        ctx.beginPath();ctx.arc(sx(lp.x),sy(lp.y),5,0,Math.PI*2);ctx.fillStyle='#818cf8';ctx.fill();
      }

      // Trajectoire réelle (la réponse)
      if(showR){
        ctx.setLineDash([3,3]);ctx.strokeStyle='#5eead4';ctx.lineWidth=1.5;ctx.beginPath();
        lv.real.forEach(function(p,i){if(i===0)ctx.moveTo(sx(p.x),sy(p.y));else ctx.lineTo(sx(p.x),sy(p.y));});
        ctx.stroke();ctx.setLineDash([]);
      }

      ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
      ctx.fillText('Niveau '+(cur+1)+'/'+levels.length+' : '+lv.name,40,16);
      ctx.restore();
    }

    function fitErr(){
      var t=traj(parseFloat(x0S.value),parseFloat(angleS.value)),err=0;
      lv.obs.forEach(function(o){var m=Infinity;t.forEach(function(p){var d=Math.hypot(p.x-o.x,p.y-o.y);if(d<m)m=d;});err+=m;});
      return err/lv.obs.length;
    }

    function upd(){
      x0V.textContent=x0S.value;
      angleV.textContent=angleS.value+'°';
      if(!fired)draw(null,false);
    }
    x0S.addEventListener('input',upd);
    angleS.addEventListener('input',upd);

    function doFire(){
      if(fired)return;fired=true;
      var t=traj(parseFloat(x0S.value),parseFloat(angleS.value));
      var lp=t[t.length-1],dist=Math.abs(lp.x-lv.target.x),fe=fitErr();
      draw(t,true);
      var hs=Math.max(0,100-Math.round(dist)),fs=Math.max(0,100-Math.round(fe*3));
      var rs=Math.round(hs*0.6+fs*0.4);total+=rs;
      var hm=dist<5?'🎯 En plein dans le mille !':dist<15?'👍 Tout près !':dist<30?'Pas mal, il s\'en faut de peu.':'💥 Assez loin du compte.';
      msgEl.innerHTML=hm+' Écart au point d\'impact : '+Math.round(dist)+', erreur d\'ajustement : '+Math.round(fe)+'. Ce niveau : <b>'+rs+'/100</b>';
      if(cur<levels.length-1){
        fireBtn.textContent='Niveau suivant →';
        fireBtn.onclick=function(){cur++;lv=genLv();fired=false;msgEl.innerHTML='';fireBtn.textContent='🚀 Feu !';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }else{
        var avg=Math.round(total/levels.length);
        scoreEl.innerHTML='🏆 Score total <b>'+total+'/'+(levels.length*100)+'</b>, moyenne '+avg;
        fireBtn.textContent='Recommencer';
        fireBtn.onclick=function(){cur=0;total=0;lv=genLv();fired=false;msgEl.innerHTML='';scoreEl.innerHTML='';fireBtn.textContent='🚀 Feu !';fireBtn.onclick=doFire;x0S.value=0;angleS.value=45;upd();};
      }
    }
    fireBtn.onclick=doFire;
    upd();
  })();
  </script>
</div>

## Quel rapport avec la prévision de séries temporelles ?

Ce que vous venez de faire est, sur le fond, exactement ce que fait la prévision de séries temporelles :

| Tir d'artillerie | Prévision de séries temporelles |
|---------|------------|
| Points observés bleus | Données historiques (le passé connu) |
| Régler la position et l'angle | Régler les paramètres du modèle (poids, hyperparamètres) |
| La parabole passe par les points observés | Le modèle s'ajuste aux données historiques |
| La parabole se prolonge jusqu'à la cible | Le modèle extrapole vers le futur |
| Toucher la cible | Une prévision exacte |

**Trois idées clés :**

- **Juste assez de paramètres.** Deux curseurs (position, angle) suffisent à décrire une parabole. Il en va de même pour les modèles de séries temporelles : trop de paramètres mènent au « surapprentissage » — parfait sur les données d'entraînement, catastrophique sur de nouvelles données.
- **L'étendue des observations compte.** Si tous les points observés sont tassés près du départ, il est difficile de deviner où l'obus retombera au loin. De même, un historique trop court ou trop monotone rend la prévision peu fiable.
- **Plus on extrapole loin, plus c'est difficile.** Plus la cible est éloignée, plus un petit écart d'angle se transforme en énorme erreur au point d'impact. Il en va de même pour l'avenir : prévoir le lendemain est bien plus facile que prévoir le mois prochain.

> Vous venez de régler les paramètres à l'œil et à la main. Mais qu'est-ce qui garantit que cette courbe est la bonne ? La page suivante pose les fondations **mathématiques et d'apprentissage automatique** de la prédiction : décrire une loi par une fonction, trouver automatiquement la meilleure courbe par optimisation, et juger par la généralisation si l'on a trop appris.
