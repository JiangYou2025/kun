---
updated: "2026-06-03"
lang: fr
ref: forecasting
permalink: /fr/forecasting/
title: "Qu'est-ce que la prévision ?"
lead: "Prévoir, c'est se servir du passé que l'on connaît pour deviner l'avenir que l'on ignore encore. Cette page vous aide à vous forger une intuition à l'aide de figures, d'un petit jeu et de quelques cas réels — les méthodes et les formules se trouvent dans le cours d'introduction."
prev: time-series
next: prediction-in-action
---

En une phrase : **la prévision (*forecasting*), c'est regarder un morceau d'histoire et prolonger le tracé vers ce qui ne s'est pas encore produit.**

## Que fait une prévision ?

<figure class="fig" markdown="0">
<svg viewBox="0 0 720 300" role="img" aria-label="Déduire l'avenir à partir du passé">
  <defs>
    <marker id="ah-f" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill="var(--muted)"/>
    </marker>
  </defs>
  <rect x="404" y="34" width="286" height="214" fill="color-mix(in srgb,var(--accent-2) 8%,transparent)"/>
  <line x1="52" y1="248" x2="694" y2="248" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <line x1="52" y1="248" x2="52" y2="28" stroke="var(--muted)" stroke-width="1.5" marker-end="url(#ah-f)"/>
  <text x="688" y="270" fill="var(--muted)" font-size="14" text-anchor="end">temps →</text>
  <text x="44" y="34" fill="var(--muted)" font-size="14" text-anchor="end">valeur</text>
  <!-- bande d'incertitude -->
  <polygon points="404,150 466,124 528,110 590,114 652,100 652,132 590,146 528,142 466,156 404,150"
    fill="color-mix(in srgb,var(--accent-2) 16%,transparent)"/>
  <!-- historique (trait plein) -->
  <polyline fill="none" stroke="var(--accent)" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"
    points="70,210 120,196 170,202 220,176 270,184 320,158 370,166 404,150"/>
  <g fill="var(--accent)">
    <circle cx="70" cy="210" r="3.5"/><circle cx="120" cy="196" r="3.5"/><circle cx="170" cy="202" r="3.5"/>
    <circle cx="220" cy="176" r="3.5"/><circle cx="270" cy="184" r="3.5"/><circle cx="320" cy="158" r="3.5"/>
    <circle cx="370" cy="166" r="3.5"/><circle cx="404" cy="150" r="4"/>
  </g>
  <!-- prévision (pointillés) -->
  <polyline fill="none" stroke="var(--accent-2)" stroke-width="2.6" stroke-dasharray="6 4" stroke-linejoin="round" stroke-linecap="round"
    points="404,150 466,140 528,126 590,130 652,116"/>
  <!-- maintenant -->
  <line x1="404" y1="34" x2="404" y2="248" stroke="var(--accent-2)" stroke-width="1.2" stroke-dasharray="3 3"/>
  <text x="404" y="28" fill="var(--text)" font-size="13" text-anchor="middle">maintenant</text>
  <text x="228" y="288" fill="var(--accent)" font-size="13" text-anchor="middle">regard en arrière · le passé connu</text>
  <text x="548" y="288" fill="var(--accent-2)" font-size="13" text-anchor="middle">prévision · pas encore arrivé</text>
</svg>
<figcaption class="figcap">À gauche, le trait plein représente <strong>l'historique connu</strong>, jusqu'à « maintenant » ; à droite, les pointillés sont la prévision du modèle pour <strong>l'avenir</strong>. La zone ombrée s'élargit vers la droite parce que plus on regarde loin, moins on est sûr — une bonne prévision donne une <strong>fourchette</strong>, pas seulement une ligne.</figcaption>
</figure>

## À vous de jouer : faites une prévision

Pas de formule pour l'instant : essayez d'abord à l'intuition.

<div class="game" markdown="0">
  <h3 style="margin-top:0">🎯 Devinez la valeur suivante</h3>
  <p class="hint">La zone d'observation montre d'abord <strong>un cycle complet</strong>, puis <strong>un demi-cycle</strong>. Repérez la régularité, puis cliquez (ou touchez) <strong>à droite</strong> de « maintenant » pour indiquer où tombera, selon vous, la valeur suivante. <strong>5 questions en tout</strong>, avec une note à la fin.</p>
  <svg id="fc-svg" viewBox="0 0 560 280" role="img" aria-label="Petit jeu : devinez la valeur suivante">
    <line x1="34" y1="248" x2="540" y2="248" stroke="var(--muted)" stroke-width="1.3"/>
    <line x1="34" y1="248" x2="34" y2="20" stroke="var(--muted)" stroke-width="1.3"/>
    <g id="fc-dyn"></g>
  </svg>
  <p class="verdict" id="fc-verdict"></p>
  <div class="bar2">
    <button id="fc-next" type="button">Question suivante →</button>
    <span class="score" id="fc-score"></span>
  </div>
  <script>
  (function(){
    var NS='http://www.w3.org/2000/svg';
    var svg=document.getElementById('fc-svg'); if(!svg) return;
    var dyn=document.getElementById('fc-dyn');
    var verdict=document.getElementById('fc-verdict');
    var btn=document.getElementById('fc-next');
    var scoreEl=document.getElementById('fc-score');
    var xs=[40,85,130,175,220,265,310,355,400], nowX=424, futX=460, top=28, bot=240;
    // chaque h = « un cycle complet (6 points) + un demi-cycle (3 points) » = 9 points ; t est la valeur de la phase suivante
    var rounds=[
      {h:[190,200,150,95,90,140, 190,200,150],   t:95,  n:'Ventes quotidiennes d\'un bar à thé'},
      {h:[200,130,85,150,110,80, 200,130,85],     t:150, n:'Fréquentation horaire'},
      {h:[95,92,98,110,185,195, 95,92,98],         t:110, n:'Visites d\'un site web'},
      {h:[140,132,145,158,150,138, 140,132,145],   t:158, n:'Température d\'une salle serveurs'},
      {h:[200,175,188,150,165,120, 138,90,110],    t:70,  n:'Cours d\'une action'}
    ];
    var MAX=5;
    var idx=0, answered=false, played=0, totErr=0;
    function el(tag,a){var e=document.createElementNS(NS,tag);for(var k in a)e.setAttribute(k,a[k]);return e;}
    function val(y){return Math.round((bot-y)/2);}
    function guide(){return 'Cliquez à droite de « maintenant » pour deviner où tombera la valeur suivante. ('+MAX+' questions en tout)';}
    function render(){
      answered=false; btn.disabled=true; while(dyn.firstChild) dyn.removeChild(dyn.firstChild);
      var r=rounds[idx];
      var pts=xs.map(function(x,i){return x+','+r.h[i];}).join(' ');
      dyn.appendChild(el('polyline',{points:pts,fill:'none',stroke:'var(--accent)','stroke-width':2.6,'stroke-linejoin':'round','stroke-linecap':'round'}));
      xs.forEach(function(x,i){dyn.appendChild(el('circle',{cx:x,cy:r.h[i],r:3.6,fill:'var(--accent)'}));});
      dyn.appendChild(el('line',{x1:nowX,y1:top,x2:nowX,y2:bot,stroke:'var(--accent-2)','stroke-width':1,'stroke-dasharray':'4 3'}));
      var nl=el('text',{x:nowX+4,y:top+12,fill:'var(--muted)','font-size':12}); nl.textContent='maintenant'; dyn.appendChild(nl);
      var q=el('text',{x:futX,y:140,fill:'var(--muted)','font-size':24,'text-anchor':'middle',id:'fc-q'}); q.textContent='?'; dyn.appendChild(q);
      var lab=el('text',{x:40,y:18,fill:'var(--muted)','font-size':13}); lab.textContent='Scénario '+(played+1)+'/'+MAX+' : '+r.n; dyn.appendChild(lab);
    }
    function pt(evt){var p=svg.createSVGPoint();var s=evt.touches&&evt.touches[0]?evt.touches[0]:evt;p.x=s.clientX;p.y=s.clientY;return p.matrixTransform(svg.getScreenCTM().inverse());}
    function answer(evt){
      if(answered || played>=MAX) return;
      var p=pt(evt);
      if(p.x < nowX-12) return;
      if(evt.cancelable) evt.preventDefault();
      var uy=Math.max(top,Math.min(bot,p.y)), r=rounds[idx];
      var q=document.getElementById('fc-q'); if(q) q.parentNode.removeChild(q);
      dyn.appendChild(el('line',{x1:xs[xs.length-1],y1:r.h[r.h.length-1],x2:futX,y2:uy,stroke:'var(--accent-2)','stroke-width':2,'stroke-dasharray':'5 4'}));
      dyn.appendChild(el('circle',{cx:futX,cy:uy,r:6,fill:'none',stroke:'var(--accent-2)','stroke-width':2.4}));
      dyn.appendChild(el('circle',{cx:futX,cy:r.t,r:5,fill:'var(--accent)'}));
      dyn.appendChild(el('line',{x1:futX,y1:uy,x2:futX,y2:r.t,stroke:'#fbbf24','stroke-width':2.4}));
      var tl=el('text',{x:futX+12,y:r.t+4,fill:'var(--accent)','font-size':12}); tl.textContent='valeur réelle'; dyn.appendChild(tl);
      var ul=el('text',{x:futX+12,y:uy+4,fill:'var(--accent-2)','font-size':12}); ul.textContent='votre prévision'; dyn.appendChild(ul);
      var err=Math.abs(val(uy)-val(r.t)), pct=Math.round(100*err/Math.max(1,val(r.t)));
      var msg=pct<=5?'Prévision parfaite !':pct<=15?'Très précis !':pct<=30?'Pas mal.':'Un peu à côté.';
      answered=true; played++; totErr+=pct;
      if(played<MAX){
        verdict.innerHTML='Question '+played+' : écart de <b>'+pct+' %</b>. '+msg+' Cliquez sur « Question suivante » pour continuer.';
        scoreEl.textContent='Progression '+played+'/'+MAX+' · erreur moyenne actuelle '+Math.round(totErr/played)+' %';
        btn.textContent='Question suivante →'; btn.dataset.mode='next'; btn.disabled=false;
      } else {
        finish(pct,msg);
      }
    }
    function finish(lastPct,lastMsg){
      var avg=Math.round(totErr/MAX), sc=Math.max(0,100-avg), pass=avg<=20;
      verdict.innerHTML='Question '+MAX+' : écart de <b>'+lastPct+' %</b>.<br>'+(pass
        ? '🎉 <b>Réussi !</b> Erreur moyenne sur les 5 questions : '+avg+' %, score <b>'+sc+'/100</b>. Vous avez déjà une bonne intuition de ce qu\'est une prévision : vous pouvez poursuivre la lecture.'
        : '🔁 <b>Encore un essai.</b> Erreur moyenne sur les 5 questions : '+avg+' %, score <b>'+sc+'/100</b> — cliquez sur « Recommencer » et observez encore un peu les régularités avant de valider.');
      scoreEl.textContent='Score final '+sc+'/100';
      btn.textContent='Recommencer'; btn.dataset.mode='reset'; btn.disabled=false;
    }
    function next(){ idx=(idx+1)%rounds.length; render(); verdict.innerHTML=guide(); }
    function reset(){ idx=0; played=0; totErr=0; scoreEl.textContent=''; render(); verdict.innerHTML=guide(); btn.textContent='Question suivante →'; btn.dataset.mode='next'; }
    svg.addEventListener('click',answer);
    svg.addEventListener('touchstart',answer,{passive:false});
    btn.addEventListener('click',function(){ if(btn.dataset.mode==='reset') reset(); else next(); });
    reset();
  })();
  </script>
</div>

Après quelques parties, vous remarquerez sans doute que **dès qu'un cycle complet apparaît dans l'historique, la valeur suivante se déduit souvent en le recopiant** : prendre « la valeur de même phase dans le cycle précédent » comme prévision, c'est la méthode la plus simple qui soit — et l'une des plus difficiles à battre (la **méthode naïve saisonnière**). Ce n'est que lorsque la tendance se complique et que la régularité s'estompe (comme pour le cours de l'action) que la devinette devient vraiment difficile.

## La prévision est partout

La même idée — « deviner l'avenir à partir du passé » — appliquée à des données différentes devient une décision que chaque secteur prend tous les jours :

<div class="cards" markdown="0">
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🌦️</div>
    <h3>Météo · climat</h3>
    <p>Un orage non annoncé peut paralyser l'évacuation des eaux d'une ville, clouer les avions au sol et détruire les récoltes ; une seule catastrophe coûte souvent plusieurs milliards. Les prévisionnistes s'appuient sur des modèles numériques de prévision du temps et sur les échos radar pour prévoir, de 6 à 72 heures à l'avance, les quantités de pluie et les zones touchées ; ils émettent ensuite des alertes, mettent en route les stations de pompage et organisent le déroutement des vols. Ce dispositif anticipé épargne chaque année à une ville moyenne plusieurs milliards de yuans de dégâts liés à la météo — à l'échelle nationale, de 0,1 % à 0,3 % du PIB.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">⚡</div>
    <h3>Électricité · énergie</h3>
    <p>Sur un réseau électrique, l'offre et la demande doivent s'équilibrer à chaque seconde ; au moindre déséquilibre, c'est la disjonction à grande échelle, voire l'effondrement du réseau entier — la grande panne du Texas en 2021 a causé près de 200 milliards de dollars de pertes économiques. Les opérateurs utilisent des modèles de prévision de la charge pour anticiper, 24 heures à l'avance, la pointe de consommation et les courbes de production éolienne et photovoltaïque ; ils planifient en conséquence le démarrage et l'arrêt des centrales thermiques, les créneaux de charge et de décharge du stockage et les échanges entre régions. Une prévision précise évite les délestages et fait économiser chaque année des dizaines de millions de yuans de combustible de modulation à un réseau provincial.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📦</div>
    <h3>Ventes · stocks</h3>
    <p>Trop de stock, et la trésorerie dort dans l'entrepôt ; pas assez, et le best-seller est en rupture, les clients partent — le commerce de détail mondial perd chaque année plus de 1 100 milliards de dollars à cause d'erreurs de stock. Les équipes supply chain s'appuient sur des modèles de séries temporelles pour prévoir les ventes de chaque référence (SKU) sur les 1 à 4 semaines à venir ; elles passent ensuite leurs commandes à l'avance, répartissent les transferts entre entrepôts et calent le rythme des promotions. Chaque point de précision gagné améliore la rotation des stocks de 2 % à 3 % et libère directement des dizaines de millions de fonds de roulement.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🚗</div>
    <h3>Trafic · mobilité</h3>
    <p>Les embouteillages des heures de pointe font perdre chaque année des centaines d'heures de trajet par habitant ; à Pékin seulement, le coût de la congestion dépasse 100 milliards de yuans. Les centres de gestion du trafic exploitent les données de circulation historiques et en temps réel pour prévoir, 30 minutes à l'avance, l'évolution du flux sur chaque tronçon ; ils ajustent ensuite la durée des feux, ouvrent des voies réversibles et diffusent des consignes de délestage. Ces mesures anticipées réduisent le temps de trajet moyen de 10 % à 15 % et améliorent chaque jour les déplacements de millions de personnes.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">🏥</div>
    <h3>Santé · épidémies</h3>
    <p>Lors d'une épidémie, dès que les lits de réanimation et les respirateurs viennent à manquer, la mortalité grimpe en flèche — pendant la COVID-19, les systèmes de santé de plusieurs pays ont ainsi été submergés. Les épidémiologistes utilisent des séries temporelles et des modèles de type SIR pour prévoir l'évolution des cas sur les 2 à 4 semaines suivantes ; ils mobilisent en conséquence du personnel soignant, redistribuent les respirateurs et montent des hôpitaux de campagne. Une prévision juste deux semaines à l'avance permet aux hôpitaux de faire face sereinement plutôt que de subir l'afflux, et réduit de 20 % à 30 % la mortalité des cas graves.</p>
  </div>
  <div class="card">
    <div style="font-size:2.2rem;text-align:center;margin-bottom:4px">📈</div>
    <h3>Finance · risque</h3>
    <p>Quand survient un « cygne noir », une institution qui n'a pas maîtrisé ses positions peut être liquidée en une journée — la faillite de Lehman Brothers en 2008 a fait s'évaporer 22 000 milliards de dollars de capitalisation mondiale. Les équipes de gestion des risques utilisent des modèles de volatilité comme GARCH ou la VaR pour estimer le risque de queue et la probabilité de pertes extrêmes ; elles réduisent alors le levier à l'avance, achètent des options de couverture et ajustent les niveaux de marge. Une bonne prévision du risque permet de contenir la perte maximale dans des limites supportables lors des marchés extrêmes, et d'éviter d'être balayé du jour au lendemain.</p>
  </div>
</div>

## Et « comment prévoir », alors ?

Cette page veut seulement vous faire <strong>voir et comprendre, en jouant, ce qu'est une prévision</strong>. Le « comment » — le flux de travail complet, les références à battre impérativement, des modèles classiques à l'apprentissage profond, et la façon de <strong>mesurer honnêtement la qualité d'une prévision</strong> — est rassemblé dans le cours d'introduction :

<div class="note" markdown="1">
- Pour les méthodes et les formules : le [cours d'introduction aux séries temporelles](../course/), en particulier la [leçon 2 · préparation des données](../course/02/) (découpage, backtesting, prévention des fuites), la [leçon 4 · visualisation](../course/04/) (analyser les résultats, examiner les résidus) et la [leçon 3 · modèles linéaires](../course/03/), qui couvrent justement « mesurer la qualité » et « battre d'abord la référence ».
- Pour expérimenter une prévision par vous-même : passez à la page suivante, [Une prévision réussie](../prediction-in-action/) — un jeu de tir d'artillerie pour comprendre l'ajustement et l'extrapolation.
- Pour vous lancer directement avec un modèle moderne : allez à [Utiliser KUN](../kun/).
</div>
