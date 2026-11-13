![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2026-27
# Exam CC no. 1

**Durée 2H00. Documents et objets connectés non autorisés. Tous les exercices sont indépendants. Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

# Exercice 1 (4 points)

## 1.1

Montrer que l'intégrale impropre ci-dessous est convergente et déterminer sa valeur (on note $e = \exp(1)$)

$$ \int_e^{\infty} \frac{\mathrm{d}x}{x\ln^2x} \cdot $$

**Réponse.** La fonction $x\mapsto 1/(x\ln^2x)$ est continue sur $[e,\infty[$ et $x\mapsto -1/\ln x$ en est une primitive. Pour $A\ge e$,
$$ \int_e^A \frac{\mathrm{d}x}{x\ln^2x} = \left[-\frac{1}{\ln x}\right]_e^A = 1-\frac{1}{\ln A}\xrightarrow[A\to\infty]{}1, $$
donc l'intégrale converge et vaut $1$.

## 1.2

En déduire, à l'aide d'un changement de variable approprié, que l'intégrale impropre ci-dessous est également convergente et déterminer sa valeur :

$$ \int_0^{1/e} \frac{\mathrm{d}x}{x\ln^2 x} \cdot $$

**Réponse.** On pose $x=1/t$ (difféomorphisme $C^1$ décroissant de $]e,\infty[$ sur $]0,1/e[$, $\mathrm{d}x=-\mathrm{d}t/t^2$). Comme $\ln^2x=\ln^2t$, on a $\dfrac{\mathrm{d}x}{x\ln^2x}=-\dfrac{\mathrm{d}t}{t\ln^2t}$ et, pour $0<\varepsilon<1/e$,
$$ \int_\varepsilon^{1/e}\frac{\mathrm{d}x}{x\ln^2x}=\int_e^{1/\varepsilon}\frac{\mathrm{d}t}{t\ln^2t}\xrightarrow[\varepsilon\to0^+]{}1 $$
d'après 1.1. L'intégrale converge donc et vaut $1$.

# Exercice 2 (5 points)


## 2.1
Calculer la dérivée (la matrice jacobienne) de la fonction associée au changement de variables

$$ \varphi(x, y) = (x + y, y). $$

**Réponse.**
$$ \varphi'(x,y)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad \det\varphi'(x,y)=1. $$
La matrice est constante et inversible : $\varphi$ est un $C^1$-difféomorphisme de $\mathbf{R}^2$ (de réciproque $(u,v)\mapsto(u-v,v)$).

## 2.2
Soit $D$ le domaine du plan défini par :
$$D = \{(x, y) \in \mathbf{R}^2 \mid 0 \le x \le 1, \, 0 \le y \le 1 - x\}.$$

À l'aide du changement de variable précédent, calculer

$$ \int_D \frac{x+y}{1+(x+y)^2} \, \mathrm{d}x\,\mathrm{d}y. $$

**Réponse.** Avec $(u,v)=\varphi(x,y)$, on a $(x,y)\in D\iff x=u-v\ge0,\ y=v\ge0,\ x+y=u\le1$, c'est-à-dire $\varphi(D)=\{0\le v\le u\le1\}$. Comme $|\det\varphi'|=1$, puis par Fubini,
$$ \int_D\frac{x+y}{1+(x+y)^2}\,\mathrm{d}x\,\mathrm{d}y=\int_0^1\frac{u}{1+u^2}\left(\int_0^u\mathrm{d}v\right)\mathrm{d}u=\int_0^1\frac{u^2}{1+u^2}\,\mathrm{d}u=\bigl[u-\arctan u\bigr]_0^1=1-\frac{\pi}{4}. $$

# Exercice 3 (5 points)

## 3.1

Calculer la dérivée (la matrice jacobienne) de la fonction associée au changement de coordonnées cylindriques : 

$$ \varphi(r,\theta,z) := (r\cos\theta,r\sin\theta,z). $$

**Réponse.**
$$ \varphi'(r,\theta,z)=\begin{pmatrix}\cos\theta&-r\sin\theta&0\\ \sin\theta&r\cos\theta&0\\ 0&0&1\end{pmatrix},\qquad \det\varphi'(r,\theta,z)=r\cos^2\theta+r\sin^2\theta=r. $$

## 3.2
En déduire la valeur de

$$ \int_D \frac{zx^2\,\mathrm{d}x\mathrm{d}y\mathrm{d}z}{\sqrt{x^2 + y^2}} $$

où $D := \lbrace (x,y,z) \in \mathbf{R}^3\ |\ 1 \leq x^2+y^2 \leq 4,\ 2 \leq z \leq 3 \rbrace$.

**Réponse.** $D$ est l'image par $\varphi$ de $[1,2]\times[0,2\pi]\times[2,3]$ (au bord près, de mesure nulle). Sur $D$, $\sqrt{x^2+y^2}=r$ et $x^2=r^2\cos^2\theta$, donc l'intégrande vaut $z\,r\cos^2\theta$, et avec le jacobien $r$ :
$$ \int_D\frac{zx^2}{\sqrt{x^2+y^2}}\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z=\int_2^3z\,\mathrm{d}z\int_1^2r^2\,\mathrm{d}r\int_0^{2\pi}\cos^2\theta\,\mathrm{d}\theta=\frac52\cdot\frac73\cdot\pi=\frac{35\pi}{6}. $$

# Exercice 4 (6 points)
On considère la famille de parties de $[0,3]$ suivante :

$$ \mathscr{A} := \lbrace [0,1], [0, 2] \rbrace. $$

## 4.1
Montrer que les tribus engendrées sur $[0,3]$ par $\mathscr{A}$ et

$$ \tilde{\mathscr{A}} := \lbrace [0,1], ]1,2] \rbrace $$

sont égales.

**Réponse.** Les tribus sont stables par différence et par réunion. D'une part $]1,2]=[0,2]\setminus[0,1]\in\mathscr{B}(\mathscr A)$, donc $\tilde{\mathscr A}\subset\mathscr{B}(\mathscr A)$ et $\mathscr{B}(\tilde{\mathscr A})\subset\mathscr{B}(\mathscr A)$. D'autre part $[0,2]=[0,1]\cup\,]1,2]\in\mathscr{B}(\tilde{\mathscr A})$, donc $\mathscr A\subset\mathscr{B}(\tilde{\mathscr A})$ et $\mathscr{B}(\mathscr A)\subset\mathscr{B}(\tilde{\mathscr A})$. D'où l'égalité.

## 4.2
Donner, sans le justifier, le cardinal de la tribu $\mathscr{B}(\mathscr{A})$ engendrée sur $[0,3]$ par $\mathscr{A}$.

**Réponse.** $\operatorname{card}\mathscr B(\mathscr A)=2^3=8$ (la tribu est engendrée par la partition $[0,1]$, $]1,2]$, $]2,3]$).

## 4.3
Soit $(X,\mathscr{B})$ un espace mesurable, et soit $f : X \to [0,3]$ telle que $f^{-1}([0,1])$ et $f^{-1}(]1,2])$ appartiennent tous deux à $\mathscr{B}$. Que peut-on dire de $f$ ? 

**Réponse.** $\{A\subset[0,3]\mid f^{-1}(A)\in\mathscr B\}$ est une tribu (l'image réciproque commute avec complémentaire et réunion dénombrable) qui contient $\tilde{\mathscr A}$, donc contient $\mathscr{B}(\tilde{\mathscr A})=\mathscr B(\mathscr A)$ d'après 4.1. Ainsi $f$ est mesurable de $(X,\mathscr B)$ dans $([0,3],\mathscr B(\mathscr A))$ ; en particulier $f^{-1}(]2,3])\in\mathscr B$ aussi.
