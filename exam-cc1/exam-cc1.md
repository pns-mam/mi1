![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2023-24
# Exam CC no. 1

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants.
Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

# Exercice 1 (4 points)
Montrer que l'intégrale impropre ci-dessous est convergente et déterminer sa valeur :

$$ \int_e^{\infty} \frac{\mathrm{d}x}{x\ln^2 x} \cdot $$

NB. $e$ désigne le nombre d'Euler ($\ln e=1$)

**Réponse.**

# Exercice 2 (4 points)
Calculer

$$ \int_D \frac{y\ \mathrm{d}x\mathrm{d}y}{1+x} $$

où $D := \lbrace (x,y) \in \mathbf{R}^2\ |\ 0 \leq x \leq 1,\ 1 \leq y \leq 3 \rbrace$.

**Réponse.**

# Exercice 3 (6 points)
## 3.1
Calculer la dérivée (= la matrice jacobienne) de la fonction associée au changement de coordonnées cylindriques : 

$$ \varphi(r,\theta,z) := (r\cos\theta, r\sin\theta,z). $$

**Réponse.**

$$ \varphi'(r,\theta,z) = \left\[ \begin{array}{ccc}
  \cos\theta & -r\sin\theta & 0\\
  \sin\theta & r\cos\theta & 0\\
  0 & 0 & 1 \end{array} \right\] $$

## 3.2
En déduire la valeur de

$$ \int_D \frac{z\ \mathrm{d}x\mathrm{d}y\mathrm{d}z}{\sqrt{x^2+y^2}} $$

où $D := \lbrace (x,y,z) \in \mathbf{R}^3\ |\ 1 \leq x^2+y^2 \leq 4,\ 0 \leq z \leq 1 \rbrace$.

**Réponse.** On a $|\det \varphi'(r,\theta,z)| = r$, ce qui permet d'appliquer la formule de changement de variable, puis Fubini : 

$$ \begin{eqnarray*}
  \int_D \frac{z\ \mathrm{d}x\mathrm{d}y\mathrm{d}z}{\sqrt{x^2+y^2}}
  &=& \int_{[1,2] \times [0,2\pi] \times [0,1]} \frac{z\ r\mathrm{d}r\mathrm{d}\theta\mathrm{d}z}{r},\\
  &=& 2\pi \int_0^1 z\ \mathrm{d}z,\\
  &=& \pi.
\end{eqnarray*} $$

# Exercice 4 (6 points)
On considère la famille de parties de $\mathbf{R}$ suivante :

$$ \mathscr{A} := \lbrace [0,2], [1, 3] \rbrace. $$

## 4.1
Montrer que les tribus engendrées sur $\mathbf{R}$ par $\mathscr{A}$ et

$$ \tilde{\mathscr{A}} := \lbrace [0,1[, [1,2], ]2, 3] \rbrace $$

sont égales.

**Réponse.** On a $\mathscr{A} \subset \tilde{\mathscr{A}}$,
donc $\mathscr{B}(\mathscr{A}) \subset \mathscr{B}(\tilde{\mathscr{A}})$.
Réciproquement, $[1,2] = [0,2] \cap [1,3]$ doit appartenir à $\mathscr{B}(\mathscr{A})$, de même que $[0,1[ = [0,2] \backslash [1,2]$ et $]2,3] = [1,3] \backslash [1,2]$; donc $\tilde{\mathscr{A}} \subset \mathscr{B}(\mathscr{A})$, et $\mathscr{B}(\tilde{\mathscr{A}}) \subset \mathscr{B}(\mathscr{A})$.

## 4.2
Donner, sans le justifier, le cardinal de la tribu $\mathscr{B}(\mathscr{A})$ engendrée par $\mathscr{A}$.

**Réponse.** Le même raisonnement montre que la tribu engendrée par $\tilde{\mathscr{A}} \cup \complement_{\mathbf{R}} [0,3]$ est encore identique. S'agissant d'une tribu engendrée par une partition (de $\mathbf{R}$) en $4$ parties, elle contient $2^4 = 16$ parties.

## 4.3
Soit $(f_n)_n$ une suite d'applications de $X$ dans $\overline{\mathbf{R}}$. Soit $a$ un réel, exprimer

$$ (\inf_n f_n)^{-1}([-\infty,a[). $$

**Réponse.** Pour $x \in X$, comme $\inf_n f_n(x) < a$ si et seulement s'il existe $n \in \mathbf{N}$ tel que $f_n(x) < a$ (sinon $a$ serait un minorant de l'ensemble $\lbrace f_n(x),\ x \in X \rbrace$, inférieur ou égal au plus grand des minorants), on a 

$$ (\inf_n f_n)^{-1}([-\infty,a[) = \bigcup_{n \in \mathbf{N}} f_n^{-1}([-\infty,a[). $$

## 4.4
On munit $X$ d'une tribu $\mathscr{T}$, on munit $\overline{\mathbf{R}}$ de sa tribu borélienne $\mathscr{B}_{\overline{\mathbf{R}}}$, et on suppose les $f_n$ mesurables. Déduire de la question précédente que la fonction $\inf_n f_n$ est également mesurable.

**Réponse.** Comme l'ensemble de parties $\lbrace [-\infty,a[, a \in \mathbf{R} \rbrace$ engendre la tribu borélienne de $\overline{\mathbf{R}}$, il suffit de montrer que l'image réciproque de chacun de ces ensembles est mesurable. Or, d'après la question précédente, cette image réciproque s'écrit comme réunion dénombrable d'ensembles mesurables (chaque $f_n$ étant supposée mesurable), donc est mesurable. 
