---
updated: "2026-06-11"
layout: lecture
lang: fr
permalink: /fr/course/wave-types/
title: "Types d'ondes et prévision"
lead: "Presque toutes les séries temporelles réelles superposent plusieurs formes d'onde. Connaître ces formes de base — tendance, cycle, amortissement, rupture — permet de choisir le bon outil de prévision. Cette page vous fait décomposer les ondes vous-même grâce à des graphiques interactifs."
prev: /course/04/
next: /course/05/
---

## Pourquoi comprendre les formes d'onde ?

Dans le mini-jeu d'artillerie, vous avez ajusté la trajectoire avec une parabole. Mais dans la réalité, les données ont rarement une seule forme — cours boursiers, températures, consommation électrique, électrocardiogrammes sont presque tous le résultat d'une **superposition de plusieurs formes d'onde**.

Comprendre les formes d'onde, c'est comprendre le « squelette » des données. Si l'on voit juste le squelette, la prévision est déjà à moitié réussie.

## Six formes d'onde de base

<div class="game" markdown="0">
<h3 style="margin-top:0">🌊 Découvrir les formes d'onde de base</h3>
<p class="hint">Cliquez sur les étiquettes ci-dessous pour changer de type d'onde, et observez leur forme ainsi que leurs équivalents dans le monde réel.</p>

<div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px">
  <button class="wave-btn active" data-wave="sine">Sinusoïde</button>
  <button class="wave-btn" data-wave="trend">Tendance</button>
  <button class="wave-btn" data-wave="damped">Onde amortie</button>
  <button class="wave-btn" data-wave="square">Onde carrée</button>
  <button class="wave-btn" data-wave="composite">Onde composite</button>
  <button class="wave-btn" data-wave="noise">Bruit</button>
</div>

<canvas id="wave-canvas" width="560" height="260" style="width:100%;max-width:560px;border-radius:10px;border:1px solid var(--border);background:var(--surface)"></canvas>
<p id="wave-desc" style="margin-top:10px;font-size:.93rem;color:var(--muted)"></p>

<style>
.wave-btn{padding:6px 14px;border-radius:6px;border:1px solid var(--border);background:var(--surface-2);color:var(--text);cursor:pointer;font-size:.88rem;font-weight:500;transition:all .15s}
.wave-btn.active{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.wave-btn:hover{opacity:0.85}
</style>

<script>
(function(){
  var canvas=document.getElementById('wave-canvas');
  if(!canvas)return;
  var ctx=canvas.getContext('2d');
  var W=560,H=260,mid=H/2;
  var descEl=document.getElementById('wave-desc');
  var btns=document.querySelectorAll('.wave-btn');

  var waves={
    sine:{
      fn:function(x){return Math.sin(x*0.05)*80;},
      color:'#5eead4',
      desc:'📐 Sinusoïde — le signal périodique le plus élémentaire. La variation de température sur une journée, les marées, le courant alternatif sont approximativement sinusoïdaux. Période fixe, amplitude constante : c\'est la pierre angulaire de la transformée de Fourier, car tout signal périodique peut se décomposer en une somme de sinusoïdes. Pour prévoir une sinusoïde, il suffit de trouver sa fréquence et sa phase : c\'est le type « le plus facile à prévoir ».',
      pred:'✅ Très facile à prévoir : il suffit de déterminer la période et l\'amplitude'
    },
    trend:{
      fn:function(x){return -80+x*0.3+Math.sin(x*0.08)*12;},
      color:'#fbbf24',
      desc:'📈 Tendance — la valeur monte ou descend durablement dans le temps. La croissance du PIB, le réchauffement climatique, la performance des puces sous la loi de Moore présentent tous une tendance marquée. Une tendance peut être linéaire, exponentielle, voire logarithmique. La clé pour la prévoir est de juger si elle va se poursuivre ou s\'inverser.',
      pred:'⚠️ Difficulté moyenne : le moment où la tendance s\'inverse est la principale incertitude'
    },
    damped:{
      fn:function(x){return Math.sin(x*0.06)*80*Math.exp(-x*0.005);},
      color:'#f0abfc',
      desc:'🔔 Onde amortie — l\'amplitude des oscillations décroît avec le temps. Les répliques après un séisme, les oscillations amorties d\'un ressort, la décroissance de la concentration d\'un médicament dans le sang. Très courante dans les systèmes physiques. Pour la prévoir, il faut estimer à la fois la fréquence et le taux d\'amortissement.',
      pred:'⚠️ Difficulté moyenne : la fréquence est facile à trouver, le taux d\'amortissement exige une observation assez longue'
    },
    square:{
      fn:function(x){return Math.sign(Math.sin(x*0.04))*60;},
      color:'#fb923c',
      desc:'⬜ Onde carrée — bascule brusquement entre deux valeurs. Signaux marche/arrêt, roulement des équipes en usine (jour/nuit), cycle des feux de circulation. Sa particularité : le changement est instantané et la valeur reste constante entre deux bascules. Pour la prévoir, il faut repérer précisément les instants de bascule.',
      pred:'✅ Facile à prévoir si la période est fixe, difficile si les bascules sont irrégulières'
    },
    composite:{
      fn:function(x){return Math.sin(x*0.03)*35+Math.sin(x*0.12)*20+x*0.08-20+Math.sin(x*0.007)*30;},
      color:'#818cf8',
      desc:'🎼 Onde composite — superposition de plusieurs fréquences et d\'une tendance : c\'est la forme la plus courante des données réelles. Consommation électrique = cycle annuel + cycle hebdomadaire + cycle journalier + tendance de long terme + fluctuations aléatoires. Décomposer une onde composite est la technique centrale de l\'analyse des séries temporelles (transformée de Fourier, décomposition en ondelettes, décomposition STL, etc.).',
      pred:'⚠️ Il faut la décomposer, prévoir chaque composante séparément, puis recombiner'
    },
    noise:{
      fn:function(x){return (Math.sin(x*37.7)*43758.5453%1-0.5)*120;},
      color:'#ef4444',
      desc:'🎲 Bruit pur — entièrement aléatoire, sans régularité exploitable. Lancers de dés, mesures quantiques, micro-fluctuations des cours boursiers à haute fréquence. Le bruit pur est imprévisible — c\'est un théorème fondamental de la théorie de l\'information. Tout modèle qui prétend prévoir du bruit pur est en surapprentissage.',
      pred:'❌ Imprévisible : c\'est la limite théorique de la prévision'
    }
  };

  var curWave='sine';

  function draw(){
    ctx.clearRect(0,0,W,H);
    // grille
    ctx.strokeStyle='rgba(150,160,180,0.1)';ctx.lineWidth=1;
    for(var i=0;i<W;i+=50){ctx.beginPath();ctx.moveTo(i,0);ctx.lineTo(i,H);ctx.stroke();}
    for(var j=0;j<H;j+=40){ctx.beginPath();ctx.moveTo(0,j);ctx.lineTo(W,j);ctx.stroke();}
    // ligne médiane
    ctx.strokeStyle='rgba(150,160,180,0.3)';ctx.setLineDash([4,4]);
    ctx.beginPath();ctx.moveTo(0,mid);ctx.lineTo(W,mid);ctx.stroke();ctx.setLineDash([]);

    var w=waves[curWave];
    // partie connue (0-70%)
    var split=Math.floor(W*0.7);
    ctx.strokeStyle=w.color;ctx.lineWidth=2.5;ctx.beginPath();
    for(var x=0;x<split;x++){var y=mid-w.fn(x);if(x===0)ctx.moveTo(x,y);else ctx.lineTo(x,y);}
    ctx.stroke();

    // partie prévue (70-100%)
    ctx.setLineDash([5,4]);ctx.strokeStyle=w.color;ctx.lineWidth=2;ctx.globalAlpha=0.6;ctx.beginPath();
    for(var x2=split;x2<W;x2++){var y2=mid-w.fn(x2);if(x2===split)ctx.moveTo(x2,y2);else ctx.lineTo(x2,y2);}
    ctx.stroke();ctx.setLineDash([]);ctx.globalAlpha=1;

    // ligne de séparation
    ctx.strokeStyle='rgba(150,160,180,0.5)';ctx.setLineDash([3,3]);ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(split,0);ctx.lineTo(split,H);ctx.stroke();ctx.setLineDash([]);
    ctx.fillStyle='#9aa3b2';ctx.font='12px sans-serif';
    ctx.fillText('← Connu',split-62,18);ctx.fillText('Prévu →',split+8,18);

    descEl.innerHTML=w.desc+'<br><strong>'+w.pred+'</strong>';
  }

  btns.forEach(function(btn){
    btn.addEventListener('click',function(){
      btns.forEach(function(b){b.classList.remove('active');});
      btn.classList.add('active');
      curWave=btn.dataset.wave;
      draw();
    });
  });

  draw();
})();
</script>
</div>

## Des formes d'onde aux stratégies de prévision

Chaque forme d'onde appelle des outils de prévision différents :

| Forme d'onde | Difficulté de prévision | Méthodes adaptées | Exemples réels |
|------|---------|-----------|---------|
| Sinusoïde | ⭐ | Analyse de Fourier, ajustement trigonométrique | Marées, écart de température jour/nuit, courant alternatif |
| Tendance | ⭐⭐ | Régression linéaire, lissage exponentiel | PIB, croissance démographique, inflation |
| Onde amortie | ⭐⭐ | Modèles physiques paramétriques | Répliques sismiques, métabolisme des médicaments, vibrations d'un ressort |
| Onde carrée | ⭐⭐ | Détection de ruptures, HMM | Roulement des équipes, feux de circulation, marche/arrêt d'équipements |
| Onde composite | ⭐⭐⭐ | Décomposition + prévision séparée (STL, ondelettes) | Consommation électrique, ventes, température |
| Bruit pur | ⭐⭐⭐⭐⭐ | **Imprévisible** — on ne peut donner qu'une distribution de probabilité | Dés, bruit quantique |

## Données réelles = onde composite + bruit

Presque toutes les séries temporelles réelles mélangent **un signal (des formes d'onde prévisibles) + du bruit (une partie aléatoire imprévisible)**.

Prévoir revient, au fond, à trois étapes :

1. **Décomposer** : séparer les données en tendance, saisonnalité et résidu (bruit).
2. **Prévoir séparément** : prévoir chaque composante avec la méthode adaptée.
3. **Recombiner** : additionner les résultats des prévisions.

> Séparer « onde composite = signal + bruit » puis prévoir chaque partie, c'est précisément le sujet de la [leçon 4 · Composantes et décomposition](../04/) ; quant à la partie « stationnaire / imprévisible », elle relève de la [leçon 5 · Stationnarité](../05/).
