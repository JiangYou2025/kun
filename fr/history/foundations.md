---
updated: "2026-06-01"
layout: history
lang: fr
era: "Prologue · Sources interdisciplinaires (1900–aujourd'hui)"
permalink: /fr/history/foundations/
title: "Sources interdisciplinaires : mathématiques, physique, cybernétique et croisements modernes"
lead: "Les méthodes des séries temporelles ne sont pas nées de rien : elles résultent de la confluence de plusieurs courants — mathématiques, physique statistique, ingénierie du contrôle et des communications — et se prolongent jusqu'à la décision séquentielle et au calcul scientifique. Ce chapitre retrace ces sources discipline par discipline : chaque fil part des fondations du début du XXᵉ siècle, mais tous se prolongent jusqu'à aujourd'hui."
math: true
next: /history/01/
---

Dans la première moitié du XXᵉ siècle, trois domaines apparemment sans rapport se sont attaqués, chacun de son côté, aux « grandeurs qui évoluent aléatoirement dans le temps » : les mathématiciens cherchaient les fondements rigoureux et les théorèmes limites des processus stochastiques ; les physiciens décrivaient des systèmes poussés par des forces aléatoires, comme le mouvement brownien ; les ingénieurs des communications et du contrôle devaient prédire des signaux noyés dans le bruit et concevoir des boucles de rétroaction. Ils ont fini par se rejoindre dans un langage commun, celui des « processus stochastiques stationnaires », qui est devenu le socle de l'analyse des séries temporelles.

---

## I. Les mathématiciens : rendre rigoureux le « processus stochastique »

La statistique des débuts savait décrire les données, mais manquait de fondements probabilistes rigoureux : de quel droit peut-on estimer la moyenne et les corrélations d'un processus entier à partir d'**une seule** trajectoire observée ? Pour répondre, il fallait d'abord définir proprement ce qu'est un « processus stochastique ». Ce travail fut accompli par une lignée de mathématiciens, dont beaucoup étaient précisément motivés par **l'aléa de la finance et des jeux de hasard** — la finance mathématique et les processus stochastiques sont, dès l'origine, une seule et même histoire.

**Kolmogorov (1933) : axiomatisation et théorème ergodique.** Kolmogorov axiomatise les probabilités par la théorie de la mesure et pose ainsi les fondations des processus stochastiques ; ses **équations prospective et rétrospective** (équations de Kolmogorov *forward/backward*) étendent les chaînes de Markov discrètes aux processus de diffusion continus, dotant les processus en temps continu comme le mouvement brownien d'outils analytiques rigoureux. Combinées à la **théorie ergodique** (Birkhoff, von Neumann), elles fournissent la garantie décisive : pour un **processus stationnaire ergodique**, la moyenne temporelle converge vers la moyenne d'ensemble (l'espérance) :

$$ \lim_{T\to\infty}\frac{1}{T}\sum_{t=1}^{T} f(X_t) \;=\; \mathbb{E}\big[f(X)\big]\quad \text{(a.s.)} $$

À gauche, la moyenne empirique sur **l'unique** série dont nous disposons ; à droite, l'espérance théorique. Le théorème ergodique garantit leur égalité — c'est la condition mathématique fondamentale qui rend légitime l'estimation de l'autocorrélation, de la moyenne et de la variance à partir de données historiques. Sans lui, toute inférence statistique serait impossible.

**Markov : l'absence de mémoire, ossature de tout le reste.** La « propriété de Markov » proposée par **Markov** (1906) — le futur ne dépend que du présent, et non du passé plus lointain —

$$ \Pr(X_{t+1}\mid X_t, X_{t-1},\dots) = \Pr(X_{t+1}\mid X_t) $$

comprime un historique de grande dimension en un seul « état courant », les transitions étant ensuite enchaînées par l'**équation de Chapman–Kolmogorov** $$P_{t+s}=P_t\,P_s$$. Cette hypothèse d'« absence de mémoire » est l'ossature la plus profondément enfouie et la plus réutilisée des séries temporelles : elle porte les **modèles AR / espace d'état et le filtre de Kalman** ([chapitre 4](../04/)), les **modèles de Markov cachés (HMM)** de la parole et de l'étiquetage de séquences, les **processus de décision markoviens** de la décision séquentielle (voir l'apprentissage par renforcement à la section IV ci-dessous), ainsi que les méthodes **MCMC** du calcul bayésien moderne. Une seule phrase — « le futur ne regarde que le présent » — traverse le siècle qui suit.

**Bachelier (1900) : le point de départ de la finance mathématique.** Cinq ans avant Einstein, le mathématicien français **Louis Bachelier** modélise pour la première fois, dans sa thèse *Théorie de la spéculation*, le cours des actions par une **marche aléatoire / un mouvement brownien**, écrivant le prix comme une accumulation d'accroissements aléatoires indépendants :

$$ S_t = S_0 + \sigma W_t,\qquad W_t-W_s\sim\mathcal N(0,\,t-s) $$

Il en déduit que « la meilleure prévision du prix est le prix actuel » — c'est-à-dire l'ébauche de la **martingale** et de la future **hypothèse d'efficience des marchés** — et obtient des résultats étonnamment proches de la valorisation moderne des options. C'est à la fois **l'œuvre fondatrice de la finance mathématique** et le premier modèle mathématique du mouvement brownien (son pendant physique, Einstein, est présenté dans la section suivante).

**Lévy : accroissements indépendants et queues épaisses.** **Paul Lévy** étudie systématiquement les **processus à accroissements indépendants et stationnaires** (les **processus de Lévy**, dont le mouvement brownien et le processus de Poisson sont des cas particuliers), caractérise leur loi par la **fonction caractéristique** et donne la forme générale des **lois stables** :

$$ \log \mathbb{E}\,e^{i u X} = i\gamma u - \tfrac12\sigma^2 u^2 + \int_{\mathbb R}\big(e^{iux}-1-iux\,\mathbf 1_{|x|<1}\big)\,\nu(dx) $$

La mesure de sauts $$\nu$$ du dernier terme autorise des **queues épaisses** et des sauts brusques — ce qui explique pourquoi les rendements financiers réels ont des queues bien plus « grasses » que la loi normale et connaissent des variations extrêmes fréquentes, annonçant directement les modèles de volatilité [ARCH/GARCH des années 1980](../06/) et les diffusions à sauts. Lévy est aussi l'un des fondateurs de la théorie des **martingales**.

**Doob (1953) : la martingale, c'est le jeu équitable.** Dans *Stochastic Processes*, **Joseph Doob** fait de la **martingale** une théorie complète. Une martingale est un « jeu équitable » — l'espérance conditionnelle de l'instant suivant est exactement égale à la valeur présente :

$$ \mathbb{E}\big[X_{t+1}\mid \mathcal F_t\big] = X_t $$

Sa portée financière est profonde : si le prix actualisé est une martingale, **il n'existe pas d'arbitrage stable et prévisible**. La **décomposition de Doob** sépare toute suite en « tendance prévisible + martingale » — c'est la version probabiliste de la décomposition « signal + innovation imprévisible » des séries temporelles ; le **théorème d'arrêt optimal** devient, lui, l'outil de l'exercice des options américaines et de la décision séquentielle. La martingale devient ainsi le cœur mathématique de **l'hypothèse d'efficience des marchés** et de **l'évaluation sans arbitrage**.

**Itô (1944/1951) : le calcul stochastique.** Le calcul différentiel ordinaire échoue face au mouvement brownien — $$W_t$$ n'est dérivable nulle part et sa variation quadratique n'est pas nulle ($$d\langle W\rangle_t = dt$$). **Kiyoshi Itô** invente le **calcul stochastique** et énonce le célèbre **lemme d'Itô** : pour une diffusion $$dX_t=\mu\,dt+\sigma\,dW_t$$,

$$ df(X_t)=\Big(f_t+\mu f_x+\tfrac12\sigma^2 f_{xx}\Big)dt+\sigma f_x\,dW_t $$

Le terme supplémentaire $$\tfrac12\sigma^2 f_{xx}$$ (issu de la variation quadratique) marque la ligne de partage entre calcul stochastique et calcul classique. En l'appliquant au **mouvement brownien géométrique** $$dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$$, on obtient

$$ S_t=S_0\exp\!\Big[(\mu-\tfrac12\sigma^2)\,t+\sigma W_t\Big] $$

— le moteur de la **valorisation des options de Black–Scholes (1973)** et de presque tous les modèles financiers en temps continu.

**Khintchine : domaine temporel et domaine fréquentiel.** Khintchine établit ensuite le **théorème de Wiener–Khintchine** : l'autocovariance $$\gamma_k$$ d'un processus stationnaire et sa densité spectrale de puissance $$S(\omega)$$ forment une paire de transformées de Fourier :

$$ S(\omega)=\sum_{k=-\infty}^{\infty}\gamma_k\, e^{-i\omega k} $$

Il rend équivalentes la « structure de corrélation dans le domaine temporel » et la « répartition de l'énergie dans le domaine fréquentiel » : les périodes cachées dans une série apparaissent comme des pics dans le spectre $$S(\omega)$$. C'est la pierre angulaire théorique de l'**analyse spectrale** (périodogramme, analyse harmonique).

Stationnarité, ergodicité, représentation spectrale : ces trois outils mathématiques font passer les séries temporelles de la « description empirique » à une « théorie des processus stochastiques qui permet l'inférence ».

**Des processus stochastiques à la finance mathématique, et retour aux séries temporelles.** Cette machinerie — la marche aléatoire de Bachelier, les queues épaisses de Lévy, la martingale de Doob, le calcul stochastique d'Itô — porte ses fruits dans les années 1970 avec la **finance mathématique** : mouvement brownien géométrique + lemme d'Itô donnent la **valorisation des options de Black–Scholes–Merton**, le processus d'Ornstein–Uhlenbeck donne le **modèle de taux de Vasicek**, et Harrison–Kreps–Pliska (1979–81) démontrent, grâce à la **mesure martingale équivalente**, que « absence d'arbitrage ⟺ existence d'une mesure sous laquelle les prix actualisés sont des martingales », posant le **théorème fondamental de l'évaluation des actifs**. De retour aux séries temporelles en temps discret, les mêmes idées réapparaissent dans un autre langage : **marche aléatoire / martingale → racines unitaires et tests d'efficience des marchés** (l'ADF et la cointégration du [chapitre 6](../06/)), **processus OU → retour à la moyenne de l'AR(1)**, **queues épaisses de Lévy → regroupement de la volatilité et ARCH/GARCH**, **mouvement brownien fractionnaire et dépendance de longue portée de Mandelbrot → modèles à mémoire longue ARFIMA**. Finance mathématique et séries temporelles sont deux branches d'un même arbre, celui des processus stochastiques.

**Les nouvelles mathématiques du XXIᵉ siècle : chemins, signatures et rugosité.** L'analyse stochastique ne s'est pas arrêtée là. La **formule de Feynman–Kac** (Kac, 1949, inspirée de l'**intégrale de chemin** de Feynman) écrit la solution d'une EDP parabolique comme une espérance sur des chemins aléatoires, faisant de l'EDP de Black–Scholes et de l'évaluation par martingale les deux faces d'une même pièce ; le **calcul de Malliavin** (1976) développe des outils pour « dériver par rapport à l'aléa », afin de caractériser la densité des solutions d'EDS et de calculer les sensibilités de couverture (les « grecques »). Au XXIᵉ siècle, la **théorie des chemins rugueux (*rough paths*, 1998) de Terry Lyons** fournit un cadre rigoureux aux équations différentielles pilotées par des signaux extrêmement irréguliers ; son objet central est la **signature** du chemin — une suite de tenseurs d'intégrales itérées :

$$ S(X)_{0,t} = \Big(\,1,\ \int dX,\ \iint dX\otimes dX,\ \iiint dX\otimes dX\otimes dX,\ \dots\Big) $$

Elle code une trajectoire en une **caractéristique universelle** : toute fonctionnelle du chemin peut être approchée linéairement par la signature. Ce fil nourrit aujourd'hui directement l'apprentissage automatique sur séries temporelles — le **noyau de signature** et les **Neural CDE / équations différentielles rugueuses neuronales** (Kidger, Salvi, Cass, Oberhauser et al., années 2020) l'utilisent pour traiter élégamment les séries à **échantillonnage irrégulier et valeurs manquantes** ; et la **volatilité rugueuse** (*rough volatility*, Gatheral–Jaisson–Rosenbaum, 2014–2018) a découvert que la trajectoire de la volatilité des marchés est un **mouvement brownien fractionnaire** d'exposant de Hurst $$H<\tfrac12$$, ramenant à l'avant-garde de la modélisation financière les intuitions de Mandelbrot, vieilles d'un demi-siècle, sur les queues épaisses et la mémoire longue. De la marche aléatoire de Bachelier à la signature de Lyons, ce fil mathématique des processus stochastiques continue de fournir sans relâche de nouveaux outils aux séries temporelles d'aujourd'hui.

---

## II. Les physiciens : dynamique stochastique, chaos et lois d'échelle

Comment décrire par une équation un système **sans cesse perturbé par des forces aléatoires**, mais doté d'une tendance intrinsèque à revenir vers l'équilibre (une particule en suspension, une tension électrique dans le bruit thermique) ?

Après la marche aléatoire des prix de Bachelier (voir la section précédente), Einstein et Smoluchowski (1905) établissent la théorie du mouvement brownien, qui correspond mathématiquement au **processus de Wiener** (accroissements gaussiens indépendants $$W_t-W_s\sim\mathcal N(0,\,t-s)$$). Langevin (1908) écrit une équation comportant un terme de frottement et une force aléatoire :

$$ m\frac{dv}{dt} = -\gamma\, v + \eta(t) $$

Ornstein et Uhlenbeck (1930) la reformulent en une équation différentielle stochastique à retour à la moyenne :

$$ dX_t = -\theta X_t\, dt + \sigma\, dW_t $$

$$-\theta X_t$$ est la force de rappel déterministe qui ramène $$X$$ vers sa moyenne, $$\sigma\,dW_t$$ la perturbation aléatoire. En la discrétisant avec un pas $$\Delta$$, on obtient exactement l'**AR(1)**, le modèle le plus familier des statisticiens :

$$ X_t = \phi X_{t-1} + \varepsilon_t,\qquad \phi=e^{-\theta\Delta} $$

Autrement dit, le « frottement + bruit thermique » du physicien et l'« autorégression » du statisticien sont **deux langages pour une même chose**. Plus $$\phi$$ est proche de 1, plus le retour est lent et la mémoire longue.

Ce fil mène directement aux modèles de taux d'intérêt en finance (Vasicek) et aux stratégies de retour à la moyenne du *pairs trading*, et fait des équations différentielles stochastiques l'outil standard des séries temporelles en temps continu.

Mais **après 1930**, l'apport des physiciens aux séries temporelles dépasse de loin le seul « retour à la moyenne ». Ils ont apporté trois visions du monde entièrement nouvelles : le **chaos déterministe**, les **lois d'échelle et la mémoire longue**, et **l'idée de traiter un système dynamique comme un opérateur linéaire**.

**Chaos déterministe : apparence aléatoire, cœur déterministe.** En 1963, le météorologue **Edward Lorenz** découvre, dans un modèle simplifié de convection, que trois équations parfaitement déterministes

$$ \dot x=\sigma(y-x),\qquad \dot y=x(\rho-z)-y,\qquad \dot z=xy-\beta z $$

peuvent produire des trajectoires **qui ne se répètent jamais et sont extrêmement sensibles aux conditions initiales** — « un battement d'ailes de papillon au Brésil peut-il provoquer une tornade au Texas ? ». Deux trajectoires voisines s'écartent exponentiellement selon $$|\delta(t)|\approx|\delta_0|\,e^{\lambda t}$$ ($$\lambda$$ étant le plus grand exposant de Lyapunov), ce qui fixe un **horizon fondamental** à la prévision : même avec un modèle parfait, l'erreur est amplifiée exponentiellement. Le chaos apporte aux spécialistes des séries temporelles une prise de conscience bouleversante — **une série d'apparence aléatoire peut cacher un système déterministe de faible dimension**, et non un processus stochastique.

**Reconstruire tout le système à partir d'une seule série : le plongement de Takens.** En 1981, le **théorème de plongement par retards** de **Floris Takens** livre une conclusion stupéfiante : à partir de la seule observation **univariée** $$x_t$$, on construit les coordonnées retardées

$$ \mathbf y_t=\big(x_t,\,x_{t-\tau},\,x_{t-2\tau},\dots,x_{t-(m-1)\tau}\big) $$

et, pourvu que la dimension de plongement $$m$$ soit assez grande ($$m>2d$$, où $$d$$ est la dimension de l'attracteur), $$\mathbf y_t$$ est **difféomorphe** à l'attracteur du système d'origine — une simple série scalaire conserve intégralement la géométrie d'un système dynamique multidimensionnel. De là naît toute l'**analyse non linéaire des séries temporelles** : **Grassberger–Procaccia (1983)** estiment la **dimension de corrélation** grâce à l'intégrale de corrélation $$C(r)\sim r^{D_2}$$ pour juger si un système est de faible dimension ; on estime directement à partir des données les **exposants de Lyapunov** pour mesurer l'intensité du chaos ; **Farmer–Sidorowich (1987)** et **Sugihara–May (1990)** font de la **prévision non linéaire** par plus proches voisins locaux, et s'en servent pour distinguer « chaos » et « bruit pur ». Ce courant rencontre de front les réseaux de neurones lors de la **compétition de prévision de séries temporelles de Santa Fe en 1992**, et devient l'une des sources de la prévision non linéaire moderne.

**Lois d'échelle et mémoire longue : bruit en 1/f et fractales.** Les physiciens ont très tôt constaté l'omniprésence, dans la nature, de **corrélations de longue portée** et de l'**invariance d'échelle**. L'hydrologue **Hurst (1951)** découvre dans les niveaux du Nil que l'étendue normalisée vérifie $$\mathbb E[R(n)/S(n)]\sim n^{H}$$ ; $$H>\tfrac12$$ signale une **mémoire longue** bien au-delà de l'hypothèse d'indépendance — c'est le point de départ empirique du **mouvement brownien fractionnaire** de Mandelbrot (covariance $$\propto|t|^{2H}+|s|^{2H}-|t-s|^{2H}$$). Le **bruit en 1/f**, omniprésent en physique (densité spectrale $$S(f)\sim f^{-\beta}$$), en est le visage fréquentiel. **Peng et al. (1994)** proposent l'**analyse des fluctuations redressées (DFA)** : $$F(n)\sim n^{\alpha}$$, qui reste l'outil standard pour extraire les corrélations de longue portée du rythme cardiaque, de l'ADN ou des séries financières, et qui fournit l'intuition physique des modèles à **mémoire longue ARFIMA** et de la différenciation fractionnaire du [chapitre 6](../06/).

**Éconophysique : le marché comme système de mécanique statistique.** Dans les années 1990, **Mantegna et Stanley**, entre autres, fondent l'**éconophysique**, qui étudie les séries financières avec les lois d'échelle, les lois de puissance et les phénomènes critiques de la mécanique statistique, et caractérise les **queues épaisses** des rendements, le **regroupement de la volatilité** et la **multifractalité** ; **Bouchaud** et d'autres modélisent le marché dans le langage des particules en interaction et des systèmes désordonnés. Ces travaux rejoignent [GARCH](../06/) par un autre chemin, mais cherchent à répondre au « pourquoi ».

**Linéariser les systèmes dynamiques non linéaires : l'opérateur de Koopman.** Le dernier fil remonte à l'intuition de **Koopman (1931)** : plutôt que de suivre l'état non linéaire, observer l'opérateur **linéaire** qui agit sur les **fonctions d'observation**, $$(\mathcal K g)(x)=g(F(x))$$. Resté en sommeil pendant des décennies, il est ravivé par **Mezić (2005)** et mis en pratique par la **décomposition en modes dynamiques (DMD, Schmid 2010)** — qui extrait des **modes cohérents et leurs fréquences** de séries temporelles de grande dimension (fluides, vidéos, réseaux de capteurs), ramenant la « prévision non linéaire » à un « problème spectral linéaire » ; elle est aujourd'hui combinée à l'apprentissage profond (autoencodeurs de Koopman).

Ce que les physiciens ont légué aux séries temporelles, c'est une vision du monde très différente de celle des statisticiens : une série n'est pas forcément l'échantillon d'un processus stochastique ; elle peut aussi être **la projection d'un chaos déterministe**, **la loi d'échelle d'un système critique**, ou **l'observation en basse dimension d'une dynamique de grande dimension**.

---

## III. Cybernétique et ingénierie des communications : du filtrage aux espaces d'état profonds

La conduite de tir antiaérienne de la Seconde Guerre mondiale exigeait de **prédire en temps réel** la position future d'un avion à partir d'échos radar bruités — un problème d'ingénierie de prédiction et de filtrage optimal dans le bruit.

Dans *Cybernetics* (1948), Norbert Wiener unifie rétroaction, information et prédiction sous le nom de « cybernétique » et donne, dans le domaine fréquentiel, le **filtre linéaire optimal de Wiener** (solution de Wiener–Hopf) :

$$ H(\omega) = \frac{S_{xy}(\omega)}{S_{xx}(\omega)} $$

$$S_{xx}$$ est la densité spectrale de l'entrée (signal + bruit), $$S_{xy}$$ l'interspectre entre l'entrée et la cible. Cette formule conçoit le filtre à partir du « rapport d'énergie entre signal et bruit à chaque fréquence » : on conserve les bandes à fort rapport signal sur bruit et l'on atténue celles où domine le bruit — c'est la source du traitement du signal moderne.

La même année que Wiener, la **théorie de l'information** de **Shannon (1948)** introduit l'entropie, la capacité d'un canal et le **théorème d'échantillonnage de Nyquist–Shannon**, fixant les limites informationnelles du triptyque « signal — bruit — prédiction ». Ses descendants directs sont le **codage par prédiction linéaire (LPC)** — la compression de la parole par un modèle AR (Itakura, Atal, années 1970) — et l'**algorithme de Viterbi (1967)** : un décodage optimal par programmation dynamique sur les modèles de Markov cachés et les codes convolutifs, qui reste un pilier de la reconnaissance vocale et des communications.

Les ingénieurs développent ensuite l'**identification des systèmes** (*system identification*, Åström, Ljung et d'autres, années 1970–80) : ajuster directement un modèle dynamique (ARX, ARMAX) à partir de données d'entrée-sortie, ce qui rejoint par un autre chemin l'approche de Box–Jenkins des statisticiens. De fait, Box lui-même venait du génie chimique et du contrôle qualité, et le sous-titre de son célèbre ouvrage est justement *Forecasting and **Control***.

Mais l'apport de la cybernétique aux séries temporelles ne s'est pas arrêté dans les années 1980 — bien au contraire, **nombre des avancées les plus récentes portent son empreinte**.

**Filtrage non linéaire et non gaussien : de l'EKF au filtre particulaire.** Le filtre de Kalman suppose un système linéaire et gaussien ; la réalité n'est souvent ni l'un ni l'autre. Les ingénieurs ont d'abord linéarisé localement avec le **filtre de Kalman étendu (EKF)** et le **filtre de Kalman sans parfum (UKF, Julier–Uhlmann 1997)**, puis le **filtrage particulaire / Monte-Carlo séquentiel** (Gordon–Salmond–Smith 1993) a approché une loi a posteriori **quelconque** par un nuage d'échantillons pondérés, s'affranchissant complètement de l'hypothèse gaussienne ; le **filtre de Kalman d'ensemble (EnKF, Evensen 1994)** et le **4D-Var** sont devenus le cœur de l'**assimilation de données** en prévision numérique du temps — intégrer en temps réel des dizaines de millions d'observations dans l'état du modèle —, ce qui rejoint précisément la prévision spatio-temporelle de la section V ci-dessous.

**Contrôler par la prévision : la commande prédictive (MPC).** Dans les années 1970–80, l'industrie introduit la **MPC** (DMC, Cutler–Ramaker 1980) : à chaque pas, on utilise un modèle dynamique pour **prédire un horizon futur**, on résout la séquence de commandes optimale, on n'applique que la première, puis on recommence en glissant l'horizon. Elle insère directement la « prévision de séries temporelles » dans une décision en boucle fermée et domine encore aujourd'hui le génie chimique, l'énergie et la robotique ; l'**identification par sous-espaces (N4SID, Van Overschee–De Moor 1994)** estime, elle, les matrices d'espace d'état directement à partir des données.

**Les années 2000 : un pont entre deux époques.** Au XXIᵉ siècle, contrôle et traitement du signal continuent de repousser les frontières des séries temporelles : les **réseaux à états échoïques / le calcul par réservoir (Jaeger 2001 ; Jaeger–Haas 2004)** utilisent un « réservoir » dynamique aléatoire et figé, plus une couche de lecture linéaire, pour prédire des séries chaotiques à un coût d'entraînement très faible, injectant l'intuition des systèmes dynamiques dans les réseaux récurrents ; l'**acquisition comprimée** (*compressed sensing*, Donoho, Candès–Romberg–Tao, 2006) démontre qu'un signal parcimonieux peut être reconstruit exactement à partir d'un nombre d'échantillons bien inférieur à celui de Nyquist, transformant l'acquisition et le débruitage des signaux ; le **MCMC particulaire (Andrieu–Doucet–Holenstein, 2010)** intègre le Monte-Carlo séquentiel dans le MCMC et rend praticable l'inférence des paramètres des modèles à espace d'état non linéaires. Ces travaux prolongent la tradition d'estimation d'état de Kalman et du filtrage particulaire, et préparent la vague suivante des « espaces d'état profonds ».

**Le retour de la cybernétique : les modèles à espace d'état profonds (S4, Mamba).** La « nouveauté » la plus frappante est la résurrection des idées de la cybernétique au sein de l'apprentissage profond. **HiPPO (Gu et al., 2020)** dérive, par projection polynomiale optimale, une équation d'état en temps continu capable de compresser en ligne un long historique, $$\dot{\mathbf x}(t)=A\mathbf x(t)+B u(t)$$ ; **S4 (2021)** discrétise ce **modèle linéaire à espace d'état (SSM)** pour en faire une couche profonde calculable efficacement par FFT, et dépasse le Transformer sur les bancs d'essai de **séquences très longues** ; **Mamba (2023)** introduit en outre la **sélectivité** (les matrices $$A,B,C$$ varient avec l'entrée) et un balayage en temps linéaire, devenant l'un des piliers de la modélisation des longues séquences. L'espace d'état écrit par Kalman en 1960 revient, après un détour de soixante ans, à l'avant-garde des séries temporelles — à ceci près que, cette fois, les matrices ne sont plus déduites de la physique : elles sont **apprises** par descente de gradient.

Les idées centrales que la cybernétique a léguées aux séries temporelles — **espace d'état + filtrage récursif** (synthétisés par Kalman au [chapitre 4](../04/)), **rétroaction et mise à jour en ligne**, **décision en boucle fermée fondée sur la prévision** — ont fait passer les séries temporelles de « l'ajustement hors ligne » à « temps réel, adaptatif et contrôlable ». Et un pas de plus au-delà de la « rétroaction », c'est la **décision** : que faire alors que la série n'est pas encore terminée ? C'est le sujet de la section suivante.

---

## IV. Décision séquentielle : arrêt optimal et apprentissage par renforcement

Les trois premières sections portaient sur la **prévision** — estimer le futur à partir du passé. Mais les séries temporelles soulèvent aussi une autre question : alors que la séquence n'est pas encore terminée, **quand agir, et quelle action choisir**, de façon optimale ? Ce fil de la « décision séquentielle » traverse lui aussi les mathématiques, le contrôle et l'informatique.

**Wald (1945) : analyse séquentielle et arrêt optimal.** Pour le contrôle qualité de la Seconde Guerre mondiale, **Abraham Wald** propose l'**analyse séquentielle** et le **test séquentiel du rapport de probabilités (SPRT)** : au lieu de fixer la taille d'échantillon à l'avance, on décide à chaque nouvelle observation « accepter / rejeter / observer encore une fois ». C'est l'ouverture du problème de l'**arrêt optimal** (*optimal stopping*) — avec la martingale de Doob et l'**enveloppe de Snell**, on peut démontrer « où s'arrêter » pour maximiser le gain espéré. L'**exercice des options américaines** en finance et la **détection de ruptures** en surveillance industrielle en sont les descendants directs.

**Robbins (1952) : le bandit manchot à plusieurs bras.** La « conception séquentielle d'expériences » de **Herbert Robbins** introduit le **bandit à plusieurs bras** (*multi-armed bandit*) : arbitrer entre « exploiter le meilleur connu » et « explorer l'inconnu » afin de minimiser le **regret** cumulé ; l'**indice de Gittins (1979)** fournit la stratégie optimale dans les cas solubles. C'est précisément le noyau théorique de l'apprentissage en ligne, des tests A/B et des systèmes de recommandation.

**Bellman (1957) : programmation dynamique et processus de décision markoviens.** **Richard Bellman** généralise la décision séquentielle en **processus de décision markovien (MDP)**, résolu par la **programmation dynamique** ; son cœur est l'**équation d'optimalité de Bellman** :

$$ V^*(s)=\max_{a}\Big[\,r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)\,V^*(s')\,\Big] $$

Elle décompose récursivement « l'optimum à long terme » en « récompense immédiate + optimum futur actualisé » ; c'est le socle commun de la commande optimale et de l'apprentissage par renforcement — et elle repose directement sur l'hypothèse d'absence de mémoire de **Markov** vue à la section I.

**Apprentissage par renforcement : de TD à AlphaGo.** Lorsque le modèle d'environnement $$P$$ est inconnu, l'**apprentissage par différence temporelle (TD, 1988)** de **Sutton et Barto** et le **Q-learning de Watkins (1989)** permettent à un agent d'approcher $$V^*$$ et $$Q^*$$ directement à partir de l'expérience, par **amorçage** (*bootstrapping*) ; avec des réseaux profonds comme approximateurs de fonctions, **DQN (2015)** sur Atari et **AlphaGo (2016)** au jeu de go ont lancé l'**apprentissage par renforcement profond**. Pour les séries temporelles, le RL fait passer de la « prévision » à la « décision » : exécution d'ordres, réapprovisionnement des stocks, tarification dynamique, voire **ajustement fin des modèles de prévision eux-mêmes** par RL.

---

## V. Quand la série temporelle devient un champ : EDP, simulation et opérateurs neuronaux

Lorsqu'on généralise la série temporelle unidimensionnelle à un **champ qui évolue dans le temps** (champ de température, champ de vitesse, surface de prix), ce ne sont plus des EDO/EDS qui le décrivent, mais des **équations aux dérivées partielles (EDP)**. La plus célèbre est l'**équation de Navier–Stokes**, qui décrit les fluides :

$$ \frac{\partial \mathbf u}{\partial t}+(\mathbf u\cdot\nabla)\mathbf u=-\frac1\rho\nabla p+\nu\nabla^2\mathbf u+\mathbf f $$

Météo, océans, turbulence, contraintes dans les structures — ces dynamiques spatio-temporelles se résolvent traditionnellement par **simulation numérique** : différences finies, éléments finis, méthodes spectrales, c'est-à-dire le cœur de la CFD et de la CAO / simulation d'ingénierie. Mais plus le maillage est fin, plus le calcul est coûteux.

L'apprentissage automatique ouvre une nouvelle voie : les **réseaux de neurones informés par la physique (PINN, Raissi 2019)** inscrivent directement le résidu de l'EDP dans la fonction de perte et ajustent la solution par un réseau ; les **opérateurs neuronaux** (*neural operators*) — **DeepONet (Lu, 2019)** et l'**opérateur neuronal de Fourier (FNO, Li, 2020)** — vont plus loin et apprennent une **application de fonctions vers fonctions** $$\mathcal G:a\mapsto u$$ (paramètres / conditions initiales et aux limites ↦ solution) ; une fois entraînés, ils déroulent toute une évolution spatio-temporelle bien plus vite qu'un solveur numérique. L'aboutissement en est la **prévision météorologique pilotée par les données** : **FourCastNet (2022)**, **GraphCast (2023)** et **Pangu-Weather** produisent avec un seul réseau des prévisions à moyen terme égales, voire supérieures, à celles des modèles numériques traditionnels — il s'agit au fond de **prévision de séries temporelles spatio-temporelles à l'échelle du globe**.

Ce fil rejoint la trame principale de ce livre au [chapitre 10](../10/) : l'idée de **noyaux hiérarchiques, multi-échelles et interchangeables** de KUN s'inscrit dans la même lignée que la volonté des opérateurs neuronaux de traiter des structures spatio-temporelles multi-échelles.

---

## La confluence des courants

| Source | Figures représentatives | Contributions | Héritage pour les séries temporelles |
|------|----------|------|----------------------|
| Mathématiques | Bachelier, Kolmogorov, Lévy, Doob, Itô, Lyons | Marche aléatoire, axiomatisation des probabilités, martingales, calcul stochastique, représentation spectrale, chemins rugueux et signatures | Stationnarité, inférence possible, efficience des marchés / absence d'arbitrage, finance en temps continu, caractéristiques universelles des séquences |
| Physique | Einstein, Langevin, Uhlenbeck, Lorenz, Takens, Hurst | Mouvement brownien, équations différentielles stochastiques, chaos déterministe, plongement par retards, lois d'échelle | Modèles en temps continu, sens physique de l'AR(1), prévision par dynamique non linéaire, corrélations de longue portée |
| Contrôle / communications | Shannon, Wiener, Kalman, Gordon, Gu | Théorie de l'information, filtrage optimal / non linéaire, espace d'état, MPC, SSM profonds | Estimation récursive, assimilation de données, commande prédictive, S4/Mamba |
| Décision séquentielle | Wald, Robbins, Bellman, Sutton·Barto | Arrêt optimal, bandits à plusieurs bras, programmation dynamique, apprentissage par renforcement | Tests séquentiels, détection de ruptures, prévision orientée décision |
| Spatio-temporel / calcul scientifique | Navier–Stokes, Raissi, Lu, Li | EDP, simulation numérique, PINN, opérateurs neuronaux | Prévision spatio-temporelle, prévision de la météo et des fluides pilotée par les données |

> La rigueur des mathématiques, la dynamique stochastique et le chaos des physiciens, le filtrage et la rétroaction des ingénieurs, le « quand agir » de la décision séquentielle, jusqu'au calcul scientifique qui généralise la série en champ — ces courants ont ensemble porté les méthodes de séries temporelles du siècle suivant. Entrons maintenant dans la trame principale de la statistique avec [l'autorégression des années 1920](../01/).

---

**Termes clés (*Key terms*) :** stationnarité · théorème ergodique · propriété de Markov · martingale · processus de Lévy et queues épaisses · calcul stochastique / lemme d'Itô · mouvement brownien géométrique · hypothèse d'efficience des marchés · intégrale de chemin / Feynman–Kac · chemins rugueux et signature de chemin · volatilité rugueuse · théorème de Wiener–Khintchine · processus de Wiener · processus d'Ornstein–Uhlenbeck · équation de Langevin · chaos déterministe · exposant de Lyapunov · plongement par retards de Takens · dimension de corrélation · corrélations de longue portée / exposant de Hurst · DFA · bruit en 1/f · éconophysique · opérateur de Koopman / DMD · filtre de Wiener · identification des systèmes · théorie de l'information / théorème d'échantillonnage (Shannon) · algorithme de Viterbi · filtrage particulaire / SMC · Kalman d'ensemble / assimilation de données · commande prédictive (MPC) · réseaux à états échoïques / calcul par réservoir · acquisition comprimée · MCMC particulaire · modèles à espace d'état profonds (HiPPO / S4 / Mamba) · processus de décision markovien · analyse séquentielle / arrêt optimal · bandit à plusieurs bras · programmation dynamique / équation de Bellman · apprentissage par renforcement · équations aux dérivées partielles / Navier–Stokes · réseaux de neurones informés par la physique (PINN) · opérateurs neuronaux (DeepONet / FNO) · prévision météorologique pilotée par les données
