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

**Réponse.** Si $p$ est fini, on change de variable pour écrire

$$ \int_{\mathbf{R}} |f(x-t)|^p\ \mathrm{d}t = \int_{\mathbf{R}} |f(y)|^p\ \mathrm{d}y < \infty $$

Si $p=\infty$,

$$|f(x-t)| \leq \Vert f \Vert_\infty \text{ p.p. } t. $$ 

### 1.2
Soit $x$ dans $\mathbf{R}$ ; à l'aide du théorème de Hölder, montrer que le produit de convolution

$$ f * g(x) := \int_{\mathbf{R}} f(x-t)g(t)\ \mathrm{d}t $$

est bien défini.

**Réponse.** Avec la notation de la question précédente, pour tout $x$ on a

$$ \int_{\mathbf{R}} |f(x-t)g(t)|\ \mathrm{d}t \leq \Vert h \Vert_p \Vert g \Vert_q \leq \Vert f \Vert_p \Vert g \Vert_q < \infty, $$

de sorte que le produit de convolution est bien défini.

### 1.3
En déduire que ce produit appartient à $L^\infty(\mathbf{R})$ et donner une majoration de sa norme dans cet espace.

**Réponse.** La question précédente montre que, pour tout $x$ on a 

$$ |\int_{\mathbf{R}} f(x-t)g(t)\ \mathrm{d}t | \leq \int_{\mathbf{R}} |f(x-t)g(t)|\ \mathrm{d}t \leq \Vert f \Vert_p \Vert g \Vert_q < \infty, $$

donc que $f * g$ est bornée et que $\Vert f * g \Vert_\infty \leq \Vert f \Vert_p \Vert g \Vert_q$.

## Exercice 2 (5 points)
Soit $f : \mathbf{R}^2 \to \mathbf{R}$ mesurable et positive. On note $D$ le disque de centre $(0,0)$ et de rayon $1$.

### 2.1
Montrer que

$$ I := \int_D \frac{f(x,y)}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y = \lim_{n \to \infty} \int_{D_n} \frac{f(x,y)}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y $$ 

où, pour $n \geq 1$,

$$ D_n := \lbrace (x,y) \in \mathbf{R}^2\ |\ 1/n^2 \leq x^2+y^2 \leq 1 \rbrace. $$

**Réponse.** Par convergence monotone,

$$ \int_{\mathbf{R}^2} \frac{f(x,y)\chi_{|D_n}}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y \to I,\quad n \to \infty. $$ 

### 2.2
On suppose désormais $f$ à symétrie radiale, c'est à dire telle qu'il existe $g : \mathbf{R} \to \mathbf{R}$ telle que, quel que soit $\theta \in [0,2\pi]$,

$$ f(r\cos\theta,r\sin\theta) = g(r). $$

Montrer que

$$ I = 2\pi \int_0^1 g(r)\ \mathrm{d}r. $$

**Réponse.** On passe en polaires sur $D_n$ pour obtenir, après simplification par $r$, Fubini, puis à nouveau convergence monotone (et unicité de la limite),

$$ \int_{D_n} \frac{f(x,y)}{\sqrt{x^2+y^2}}\ \mathrm{d}x\mathrm{d}y = \int_{[1/n,1] \times [0,2\pi]} g(r)\ \mathrm{d}r\mathrm{d}\theta = 2\pi\int_{[1/n,1]} g(r)\ \mathrm{d}r \to 2\pi \int_0^1 g(r)\ \mathrm{d}r = I,\quad n \to \infty. $$ 

### 2.3
Application : déterminer

$$ \int_D \frac{\mathrm{d}x \mathrm{d}y}{(x^2+y^2)^{3/4}} \cdot $$

**Réponse.**

$$ \int_D \frac{\mathrm{d}x \mathrm{d}y}{(x^2+y^2)^{3/4}} = 2\pi\int_0^1 \frac{\mathrm{d}r}{\sqrt{r}} = 4\pi $$

## Exercice 3 (5 points)

## 3.1
Soit $f$ dans $L^1(\mathbf{R})$ une fonction impaire ($f(-x)=-f(x)$ presque pour tout $x \in \mathbf{R}$). Montrer que $\hat{f}$ est également impaire et que

$$ \hat{f}(\xi) = -2i\int_0^\infty f(x)\sin(2\pi \xi x)\ \mathrm{d}x. $$

**Réponse.**

En passant par le changement de variables u=-x sur le domaine $]-\infty,0]$, on obtient par imparité de $f$:

$$
 \hat{f}(\xi)=\int_0^\infty f(x)e^{-2i\pi\xi x}\mathrm{d} x+\int_0^\infty f(-u)e^{2i\pi\xi u}\mathrm{d} u=\int_0^\infty f(x)\left(e^{-2i\pi\xi x}-e^{-2i\pi\xi x}\right)\mathrm{d}x
$$

Avec $e^{-2i\pi\xi x}-e^{-2i\pi\xi x}=-2i\sin(2\pi \xi x)$, on obtient le résultat annoncé.

## 3.2
En déduire la transformée de Fourier de $f : \mathbf{R} \to \mathbf{R}$, $f(t) = t e^{-|t|}$.

**Réponse.**

Comme $f$ est impaire, 3.1 s'applique.

$$
\hat{f}(\xi)=-2i\int_0^\infty  x e^{-x}\sin(2\pi \xi x)\ \mathrm{d}x=-2i \mathrm{Im}\left(\int_0^\infty  x e^{-x}e^{2i\pi \xi x}\ \mathrm{d}x\right)
$$

Par intégration par partie,

$$
\int_0^\infty  x e^{(-1+2i\pi \xi) x}\ \mathrm{d}x = - \int_0^\infty   \frac{e^{(-1+2i\pi \xi) x}}{-1+2i\pi \xi }\ \mathrm{d}x =  \frac{1}{(-1+2i\pi \xi )^2}
$$

Puis $  \dfrac{1}{(-1+2i\pi \xi )^2}=  \dfrac{(-1-2i\pi \xi )^2}{|-1+2i\pi \xi |^4}$ et $\mathrm{Im}\left( \dfrac{1}{(-1+2i\pi \xi )^2}\right)= \dfrac{4\pi \xi}{(1+4\pi^2\xi^2)^2}$, d'où $\hat{f}(\xi)=\dfrac{-8i\pi \xi}{(1+4\pi^2\xi^2)^2}$.

## 3.3
Pour la fonction $f$ définie au 3.2, justifier que le produit de convolution $f * f$ est bien défini et déterminer $\widehat{f * f}$.

**Réponse.**

Rappel de cours, si $f\in L^1(\mathbf{R})$, $f * f$ est bien défini et $f * f \in L^1(\mathbf{R})$. De plus, $\widehat{f * f}=(\hat f)^2$
donc 

$$
\widehat{f * f}=\dfrac{-64\pi^2\xi^2}{(1+4\pi^2\xi^2)^4}.
$$

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
