![PNS](http://caillau.perso.math.cnrs.fr/logo-pns.png)
## MAM3
# Mathématiques de l'ingénieur.e 1
# 2023-24

# Exam CC no. 3

**Durée 2H. Documents non autorisés. Tous les exercices sont indépendants. Le barème indicatif est précisé pour chaque exercice. Rendre sur deux copies séparées les exos 1 et 2 d'une part, 3 et 4 d'autre part.**

## Exercice 1 (5 points)
Soient $f$ dans $L^p(\mathbf{R})$ et $g$ dans $L^q(\mathbf{R})$ avec $p$, $q$ dans $[1,\infty]$ conjugués ($1/p+1/q = 1$).

### 1.1
On se fixe $x$ dans $\mathbf{R}$ ; montrer que l'application $h : t \mapsto f(x-t)$ est encore dans $L^p(\mathbf{R})$.

### 1.2
Soit $x$ dans $\mathbf{R}$ ; à l'aide du théorème de Hölder, montrer que le produit de convolution

$$ f * g(x) = \int_{\mathbf{R}} f(x-t)g(t)\ \mathrm{d}t $$

est bien défini.

### 1.3
En déduire que ce produit appartient à $L^\infty(\mathbf{R})$ et donner une majoration de sa norme dans cet espace.

## Exercice 2 (5 points)
Soit $f : \mathbf{R}^2 \to \mathbf{R}$ mesurable et positive. On note $D$ le disque de centre $(0,0)$ et de rayon $1$.

### 2.1
Montrer que

$$ I := \int_D \frac{f(x,y)}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y = \lim_{n \to \infty} \int_{D_n} \frac{f(x,y)}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y $$ 

où, pour $n \geq 1$,

$$ D_n := \lbrace (x,y) \in \mathbf{R}^2\ |\ 1/n^2 \leq x^2+y^2 \leq 1 \rbrace. $$

### 2.2
On suppose désormais $f$ à symétrie radiale, c'est à dire telle qu'il existe $g : \mathbf{R} \to \mathbf{R}$ telle que, quel que soit $\theta \in [0,2\pi]$,

$$ f(r\cos\theta,r\sin\theta) = g(r). $$

Montrer que

$$ I = 2\pi \int_0^1 g(r)\ \mathrm{d}r. $$

### 2.3
Application : déterminer

$$ \int_D \frac{\mathrm{d}x \mathrm{d}y}{(x^2+y^2)^{3/4}} \cdot $$

## Exercice 3 (5 points)

## 3.1
Soit $f$ dans $L^1(\mathbf{R})$ une fonction impaire ($f(-x)=-f(x)$ presque pour tout $x \in \mathbf{R}$). Montrer que $\hat{f}$ est également impaire et que

$$ \hat{f}(\xi) = -2i\int_0^\infty f(x)\sin(2\pi \xi x)\ \mathrm{d}x. $$

## 3.2
En déduire la transformée de Fourier de $f : \mathbf{R} \to \mathbf{R}$, $f(t) = t e^{-|t|}$.

## 3.3
Pour la fonction $f$ définie au 3.2, justifier que le produit de convolution $f * f$ est bien défini et déterminer $\widehat{f * f}$.

## Exercice 4 (5 points)

### 4.1
Donner l'abscisse de convergence et la transformée de Laplace de la fonction $t \mapsto e^{it}$, $t \geq 0$. En déduire les transformées de Laplace des fonctions $\cos t$ et $\sin t$.

### 4.2
On considère l’équation différentielle ordinaire suivante : trouver $y$ deux fois dérivable telle que

$$ y’’(t) + y(t) = 1,\quad t \geq 0, $$

$$ y(0)=0,\quad y’(0)=-1. $$

On admet qu’elle possède une unique solution, notée $y$. Montrer que, partout où elle est définie, la transformée de Laplace $\mathscr{L}y$ vérifie l’équation

$$ \mathscr{L}y(s) = \frac{A}{s} + \frac{B}{s^2+1} + \frac{Cs}{s^2+1} $$

avec $A$, $B$ et $C$ des réels que l’on précisera.

## 4.3
En déduire la solution $y$ de l’équation différentielle.
