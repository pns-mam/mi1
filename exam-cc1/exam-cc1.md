![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2025-26
# Exam CC no. 1

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants.
Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

# Exercice 1 (4 points)

## 1.1

Montrer que l'intégrale impropre ci-dessous est convergente et déterminer sa valeur :

$$ \int_1^{\infty} \frac{\mathrm{d}x}{1 + x^2} \cdot $$

**Réponse.** La fonction $f(x)=\frac{1}{1 + x^2}$ est positive continue bornée sur $[1,+\infty[$ donc elle est intégrable si $\int_1^{A} \frac{\mathrm{d}x}{1 + x^2}$ admet une limite finie quand $A\to \infty$. Or

$$ \int_1^{A} \frac{\mathrm{d}x}{1 + x^2} = \left[\arctan x\right]_1^A= \arctan A - \frac{\pi}{4} \xrightarrow[A\to \infty]{} \frac{\pi}{4}.$$

L'intégrale est donc convergente et vaut $\frac{\pi}{4}$.

## 1.2

En déduire que l'intégrale impropre ci-dessous est également convergente et déterminer sa valeur :

$$ \int_0^{\infty} \frac{e^t\ \mathrm{d}t}{1 + e^{2t}} \cdot $$

**Réponse.** La fonction $g(t)=\frac{e^t}{1 + e^{2t}}$ est positive continue bornée sur $[0,+\infty[$. On effectue sur l'ouvert $]0,A[$ le changement de variable $e^t=x$, de sorte que $e^t\,\mathrm{d}t= \mathrm{d}x$ et

$$ \int_0^{A}   \frac{e^t\ \mathrm{d}t}{1 + e^{2t}}= \int_1^{e^A} \frac{\mathrm{d}x}{1 + x^2} = \left[\arctan x\right]_1^{e^A}= \arctan e^A - \frac{\pi}{4} \xrightarrow[A\to \infty]{} \frac{\pi}{4}.$$

L'intégrale est donc convergente et vaut $\frac{\pi}{4}$.


# Exercice 2 (4 points)

Calculer

$$ \int_D \frac{xy\ \mathrm{d}x\mathrm{d}y}{1+y^2} $$

où $D := \lbrace (x,y) \in \mathbf{R}^2\ |\ 1 \leq x \leq 2,\ 0 \leq y \leq 1 \rbrace$.

# Exercice 3 (6 points)

## 3.1

Calculer la dérivée (la matrice jacobienne) de la fonction associée au changement de coordonnées sphériques : 

$$ \varphi(r,\theta,\varphi) := (r\cos\theta\sin\varphi, r\sin\theta\sin\varphi, r\cos\varphi). $$

## 3.2
En déduire la valeur de

$$ \int_D \frac{(x^2 + y^2)\,\mathrm{d}x\mathrm{d}y\mathrm{d}z}{\sqrt{x^2 + y^2 + z^2}} $$

où $D := \lbrace (x,y,z) \in \mathbf{R}^3\ |\ 1 \leq x^2+y^2+z^2 \leq 4 \rbrace$.

# Exercice 4 (6 points)

On considère la famille de parties de $[0, 2]$ suivante :

$$ \mathscr{A} := \lbrace [0, 1], [1, 2[ \rbrace. $$

## 4.1

Montrer que les tribus engendrées sur $[0, 2]$ par $\mathscr{A}$ et

$$ \tilde{\mathscr{A}} := \lbrace [0,1[, B, ]1, 2[ \rbrace $$

où $B \subset [0, 2]$ est une partie que l'on précisera, sont égales.

## 4.2

Donner, sans le justifier, le cardinal de la tribu $\mathscr{B}(\mathscr{A})$ engendrée par $\mathscr{A}$ sur $[0, 2]$.

## 4.3

Soit $(X,\mathscr{B})$ un espace mesurable, et soit $f : X \to [0,2]$ telle que $f^{-1}([0,1])$ et $f^{-1}([1,2[)$ appartiennent tous deux à $\mathscr{B}$. Que peut-on dire de $f$ ? 
