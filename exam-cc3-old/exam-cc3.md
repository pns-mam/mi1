![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2024-25
# Exam CC no. 3

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants. Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

# Exercice 1 (7 points)

## 1.1

Soit $A > 0$, montrer que

$$ I_A := \int_0^A \frac{\sin x\,\mathrm{d}x}{x} $$

est bien définie.

## 1.2

Montrer que

$$ I_A = \int_0^A \sin x \left( \int_0^\infty e^{-tx}\,\mathrm{d}t \right) \mathrm{d}x. $$

## 1.3

Montrer qu'on peut appliquer le théorème de Fubini pour calculer $I_A$.

## 1.4

En déduire que

$$ I_A = C + \textrm{Im} \int_0^\infty \frac{e^{A(i-t)}}{i-t}\,\mathrm{d}t $$

où $C$ est une constante que l'on précisera.

## 1.5

Montrer que

$$ \left| \int_0^\infty \frac{e^{A(i-t)}}{i-t}\,\mathrm{d}t \right| \leq \frac{1}{A} $$

et en déduire que $I_A$ possède une limite que l'on précisera quand $A$ tend vers l'infini.

# Exercice 2 (5 points)

## 2.1 

Soit $f_n(x) := (-1)^n e^{-2^n x}$, $x \geq 0$, $n \geq 0$. Montrer que

$$ \sum_{n \geq 0} \int_0^\infty |f_n(x)|\,\mathrm{d}x < \infty. $$

## 2.2

En déduire que l'intégrale ci-dessous est bien définie : 

$$ \int_0^\infty \sum_{n \geq 0} f_n(x)\,\mathrm{d}x. $$

## 2.3

Déterminer la valeur de cette intégrale.

# Exercice 3 (5 points)

## 3.1 

Montrer que le produit de convolution des deux fonctions caractéristiques $\chi_{[0,1]} * \chi_{[0,2]}$ est bien défini, puis le calculer.

**Réponse.** Les fonctions  $\chi_{[0,1]}$ et  $\chi_{[0,2]}$ sont bornées et à support contenu dans $[0,2]$, donc de classe $L^1(\mathbf{R})$. Par conséquent $ $\chi_{[0,1]} * \chi_{[0,2]}\in L^1(\mathbf{R})$ est bien défini.

$$\chi_{[0,1]} * \chi_{[0,2]}(x)= \int_{-\infty}^\infty \chi_{[0,1]}(y) \chi_{[0,2]}(x-y)dy=\int_0^1 \chi_{[0,2]}(x-y)dy$$

Or $\chi_{[0,2]}(x-y)\neq 0$ si et seulement si $y\in [x-2,x]$. On a donc 5 cas:

* $x<0$ : $\int_0^1 \chi_{[0,2]}(x-y)dy = 0$
* $0\leq x <1$ : $\int_0^1 \chi_{[0,2]}(x-y)dy = \int_0^x dy = x$
* $1\leq x<2$ : $\int_0^1 \chi_{[0,2]}(x-y)dy = \int_0^1 dy = 1$
* $2\leq x<2$ : $\int_0^1 \chi_{[0,2]}(x-y)dy = \int_{x-2}^1 dy = 3-x$
* $x\geq 0$ : $\int_0^1 \chi_{[0,2]}(x-y)dy = 0$

  
## 3.2

Soit $a > 0$, déterminer la transformée de Fourier de $\chi_{[0,a]}$.

**Réponse.** $\chi_{[0,a]}$ est de classe $L^1$.

$$\hat{\chi}_{[0,a]}(\xi) = \int _{0}^a e^{-2i\pi \xi x} dx =
\begin{cases}
     \frac{1-e^{-2i\pi \xi a}}{2i \pi \xi}& \text{ si } \xi\neq 0 
     \\
    a & \text{ sinon.}
\end{cases}
$$

Remarque, une formule possible sans disjonction est : $\hat{\chi}_{[0,a]}(\xi)=a e^{-i\pi \xi a}\textrm{sinc}(\pi \xi a)$.

## 3.3

Déterminer la transformée de Fourier de $\chi_{[0,1]} * \chi_{[0,2]}$.

**Réponse.** On sait que $\widehat{\chi_{[0,1]} * \chi_{[0,2]}}(\xi)=\hat{\chi}_{[0,1]}(\xi)\hat{\chi} _{[0,2]}(\xi)$. De part la question précedente :

$$
\widehat{\chi _{[0,1]} * \chi _{[0,2]}}(\xi) =
\begin{cases}
     \frac{e^{-2i\pi \xi}+e^{-4i\pi \xi}-e^{-6i\pi \xi}-1}{4 \pi^2 \xi^2}& \text{ si } \xi\neq 0, 
     \\
    2 & \text{sinon;}
\end{cases}
$$

ou encore, $\widehat{\chi _{[0,1]} * \chi _{[0,2]}}(\xi) = 2 e^{-i\pi \xi}e^{-2i\pi \xi}\textrm{sinc}(2\pi \xi)\textrm{sinc}(\pi \xi)$


# Exercice 4 (4 points)

## 4.1

Soient $m$ et $\sigma$ deux réels, $\sigma > 0$, et soit

$$ I = \frac{1}{\sigma\sqrt{2\pi}} \int_{\mathbf{R}} e^{-(x-m)^2/(2\sigma^2)}\,\mathrm{d}x. $$

Effectuer le changement de variable $x = \varphi(y) := \sigma y + m$ dans cette intégrale, puis en déduire sa valeur. 

[**Indication** : on pourra retrouver cette valeur à l'aide du théorème de Fubini.]


**Réponse.** En effectuant le changement de variable indiqué, on trouve $I=\frac{1}{\sqrt{2\pi}}  \int_{\mathbf{R}}  e^{-y^2/2}\,\mathrm{d}y.$ En changeant une nouvelle fois de variable pour $z=y/\sqrt{2}$, on obtient alors $I=\frac{1}{\sqrt{\pi}} \int_{\mathbf{R}} e^{-z^2}\,\mathrm{d}z$. On reconnais alors l'intégrale de Gauss, d'où $I=1$.

## 4.2

Soit $X$ une variable aléatoire à valeurs dans $\mathbf{R}$ de densité

$$ f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-(x-m)^2/(2\sigma^2)}. $$

On pose $Y = \varphi^{-1}(X)$, donner l'espérance de $Y$.

**Réponse.** $\mathbf{E}(Y)=\int_{\mathbf{R}} \varphi^{-1}(x) f(x) \,\mathrm{d}x$. Par le changement de variable $x=\varphi(y)$, on trouve $\mathbf{E}(Y)=\frac{1}{\sqrt{2\pi}}\int_{\mathbf{R}} y  e^{-y^2/2} \,\mathrm{d}y=0$.
