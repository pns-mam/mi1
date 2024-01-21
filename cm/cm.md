![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)
## MAM3 - MI1
# Mathématiques de l'ingénieur.e 1 
# 2023-24

## Ch. 1 - Tribus, mesures

### 1. Tribus et applications mesurables
- déf. tribu, espace mesurable
- ex. tribus grossière et discrète
- déf. prop. : tribu engendrée
- ex. boréliens sur la droite (génération par $\{ ]-\infty,a[,\ a \in \mathbf{R} \}$) et la droite achevée
- déf. application mesurable
- prop. : mesurabilité de la composée d'applications mesurables
- ex. fonctions caractéristiques
- prop. : mesurabilité dans le cas d'une tribu engendrée sur le codomaine 
- cor. : mesurabilité des applications continues, continues par morceaux (sur une partition mesurable)
- cor. : mesurabilité de $f+g$, $f \times g$, $\inf_n f_n$, $\sup_n f_n$, $\lim_n \inf f_n$,
$\lim_n \sup f_n$

### 2. Mesures
- déf. mesure
- ex. Dirac, comptage, Lebesgue ($\mu_L([a,b[) := b-a$)  
- prop. : monotonie, $\mu(A \cup B)+\mu(A \cap B) = \mu(A)+\mu(B)$,
$\mu(B\setminus A)=\mu(B)-\mu(A)$ si $A \subset B$ et $\mu(A) \lt \infty$, continuité intérieure et extérieure
- ex. $\mu_L(\mathbf{Q})=0$, $\mu_L(\mathbf{R}\setminus \mathbf{Q})=\infty$, $\mu_L([a,b])$
- th. : complétion d'une tribu et prolongement de la mesure

## Ch. 2 - Intégration et convergence

### 1. Cas des fonctions mesurables positives
- déf. fonction simple mesurable ou "étagée" (et forme canonique)
- déf. intégrale d'une fonction étagée positive
- déf. intégrale d'une fonction mesurable positive
- rem. : approximation des fonctions positives mesurables par des fonctions étagées
- prop. : si $f$ est mesurable et positive, $\int_X f\mathrm{d}\mu=0 \iff f=0$ $\mu$-p.p.

### 2. Cas des fonctions intégrables
- déf. intégrabilité, et intégrale associée
- prop. : monotonie, positivité, linéarité, $|\int_X f\mathrm{d}\mu| \leq \int_X |f|\mathrm{d}\mu$

### 3. Résultats de convergence
- th. de convergence monotone
- th. de convergence dominée
- th. fondamental du calcul différentiel

### 4. Intégrales à paramètre
- th. de continuité
- th. de dérivabilité

## Ch. 3 - Espaces L^p
- prop. : inégalités de Hölder et Minkowski pour $1 < p < \infty$
- déf. espaces $\mathscr{L}^p(X,\mathscr{B},\mu)$ et $L^p(X,\mathscr{B},\mu)$ pour $p \in [1,\infty]$
- prop. : inégalité de Hölder (bis)
- prop. : relations d'inclusion en mesure finie
- prop. : densité de $\mathscr{C}^0([a,b],\mathbf{R})$ dans $L^p([a,b])$ pour $p \in [1,\infty[$
- th. de Riesz-Fischer

## Ch. 4 - Intégration produit
- déf. tribu produit
- déf. prop. : mesure produit (cas $\sigma$-fini)
- th. de Tonelli
- th. de Fubini
- complétion d'une mesure produit

## Ch. 5 - Transformée de Fourier

### 1. Transformée de Fourier L^1
- th. déf. : transformée de Fourier
$\hat{f}(\xi):=\int_{\mathbf{R}} f(x)e^{-2i\pi\xi x}\,\mathrm{d}x$
- prop. : effet des translations et homothéties
- lemme de Riemann-Lebesgue ($\hat{f} \in \mathscr{C}_0(\mathbf{R}))$
- prop. : dérivation et transformée de Fourier
- th. déf. : transformée de Fourier inverse
- rem. : transformée de Fourier-Plancherel sur $L^2(\mathbf{R})$

### 2. Convolution
- th. déf. : convolution $L^1(\mathbf{R})$
- prop. : commutativité
- prop. : $\widehat{f * g} = \hat{f} * \hat{g}$
- prop. : convolution $L^p(\mathbf{R}) * L^q(\mathbf{R})$ avec $1/p+1/q=1+1/r$

### 3. Transformée de Laplace
- déf. : abscisse de sommabilité d'une fonction mesurable,
$s_0 := \inf \lbrace \sigma \in \mathbf{R}\ |\ e^{-\sigma t}f \in L^1(\mathbf{R}_+) \rbrace$
- déf. : transformée de Laplace
$\mathscr{L}f(s) := \int_0^\infty e^{-st}f(t)\ \mathrm{d}t$, $\text{Re}(s) > s_0$
- rem. : lien avec transformée de Fourier
- prop. : dérivation et transformée de Laplace
- rem. : holomorphie de la transformée de Laplace (Morera)
- prop. : $\mathscr{L} (f * g) = \mathscr{L} f \cdot \mathscr{L}g$
- rem. : injectivité et transformée inverse
