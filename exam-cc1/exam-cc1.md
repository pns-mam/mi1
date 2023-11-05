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

**Réponse.** La fonction $x\mapsto 1/ (x\ln^2 x)$ est positive, continue et bornée sur $[e,+\infty[$. L'intégrale est donc impropre uniquement parce que le domaine d'intégration est non borné à droite. En ce qui concerne la convergence, on peut reconnaître une intégrale de Bertrand

$$ \int_e^\infty \frac{\mathrm{d}x}{x^\alpha\ln^\beta x}\cdot $$

Ici $\alpha=1$, $\beta=2>1$, ce qui satisfait le critère de convergence des intégrales Bertrand. (Remarque : nous n'avons pas l'obligation d'utiliser ce critère car nous devons calculer l'intégrale de toute façon.)

Pour calculer l'intégrale, on calcule la limite

$$ \lim_{A\to \infty} \int_e^A \frac{\mathrm{d}x}{x\ln^2 x} \cdot $$

Pour ce calcul, on peut passer le changement (par exemple) par le changement de variable $u=\ln x$, de sorte que $\mathrm{d}u=\frac{\mathrm{d} x}{x}$ et 

$$
  \int_e^A\frac{\mathrm{d}x}{x\ln^2 x}=\int_1^{\ln A}\frac{\mathrm{d}u}{u^2}=\left[-\frac{1}{u}\right]_{1}^{\ln A}=1-\frac{1}{\ln A} \cdot
$$

Donc l'intégrale impropre est convergente et vaut $1$ :

$$ \lim_{A\to \infty} \int_e^A \frac{\mathrm{d}x}{x\ln^2 x}=\lim_{A\to \infty} 1-\frac{1}{\ln A}=1. $$


# Exercice 2 (4 points)
Calculer

$$ \int_D \frac{y\ \mathrm{d}x\mathrm{d}y}{1+x} $$

où $D := \lbrace (x,y) \in \mathbf{R}^2\ |\ 0 \leq x \leq 1,\ 1 \leq y \leq 3 \rbrace$.

**Réponse.** La fonction $f:D\to \mathbf{R}$ telle que $f(x,y)=y/(1+x)$ pour tout $(x,y)\in D$ est continue (fonction rationnelle sans pôle dans $D$). L'ensemble $D$ est compact car fermé et borné. La fonction $f$ étant continue, elle est intégrable sur $D$. (Par exemple $0\leq f\leq 3$ donc $\int_D |f(x,y)|\mathrm{d}x\mathrm{d}y\leq 3 \mu_L(D)=6$.) Comme la fonction $f$ est intégrable sur l'espace produit $D=[0,1]\times [1,3]$, le théorème de Fubini s'applique et 

$$
 \int_D \frac{y\ \mathrm{d}x\mathrm{d}y}{1+x} = \int_0^1\left(\int_1^3 \frac{y\ \mathrm{d}y}{1+x} \right)\mathrm{d}x= \int_0^1\left(\int_1^3y\ \mathrm{d}y \right) \frac{\mathrm{d}x}{1+x}=\left(\int_1^3y\ \mathrm{d}y \right)\left(\int_0^1 \frac{\mathrm{d}x}{1+x}\right).
$$

Comme $\int_1^3y\ \mathrm{d}y=\left[\frac{y^2}{2}\right]_1^3=4$ et $\int_0^1 \frac{\mathrm{d}x}{1+x}=\left[\ln (1+x)\right]_0^1=\ln 2$, on en déduit

$$
\int_D \frac{y\ \mathrm{d}x\mathrm{d}y}{1+x}=4 \ln 2.
$$

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

**Réponse.** On a $[0,2] = [0,1[ \cup [1,2]$ et $[1,3] = [1,2] \cup ]2,3]$, donc
$\mathscr{A} \subset \mathscr{B}(\tilde{\mathscr{A}})$,
et $\mathscr{B}(\mathscr{A}) \subset \mathscr{B}(\tilde{\mathscr{A}})$.
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
