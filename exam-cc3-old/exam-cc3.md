![PNS](http://caillau.perso.math.cnrs.fr/logo-pns.png)
## MAM3 - MI1
# Exam CC no. 3

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants.
Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 d'autre part.** 

# Exo 1 (5 points)
## 1.1
Soient $f$ et $g$ toutes deux dans $L^1(\mathbf{R})$. Montrer que leur produit de convolution est bien défini et appartient également à $L^1(\mathbf{R})$. En déduire une majoration de $\|f * g\|_1$.

**Réponse.** Comme

$$ \int_\mathbf{R} \left( \int_\mathbf{R} |f(x-t)g(t)|\ \mathrm{d}x \right) \mathrm{d}t
 = \|f\|_1 \int_\mathbf{R} |g(t)|\ \mathrm{d}t = \|f\|_1 \|g\|_1 < \infty,
$$

Tonelli implique que $\varphi(t,x)=f(x-t)g(t)$ appartient à $L^1(\mathbf{R}^2)$. Du coup, Fubini implique que l'intégrale

$$ \int_\mathbf{R} f(x-t)g(t)\ \mathrm{d}t $$

est bien définie p.p. tout $x \in \mathbf{R}$. Avec Tonelli et le calcul précédent, on voit que

$$ \begin{eqnarray*}
  \int_\mathbf{R} |f*g(x)|\ \mathrm{d}x & \leq & \int_\mathbf{R} \left( \int_\mathbf{R} |f(x-t)g(t)|\ \mathrm{d}t \right) \mathrm{d}x\\
  & = & \int_\mathbf{R} \left( \int_\mathbf{R} |f(x-t)g(t)|\ \mathrm{d}x \right) \mathrm{d}t\\
  & = & \|f\|_1 \|g\|_1.
\end{eqnarray*} $$

## 1.2
Soient $f$ dans $L^1(\mathbf{R})$ et $g$ dans $L^\infty(\mathbf{R})$. Montrer que leur produit de convolution est bien défini et appartient à $L^\infty(\mathbf{R})$. En déduire une majoration de $\|f*g\|_\infty$.

**Réponse.**

$$ \int_\mathbf{R} |f(x-t)g(t)|\ \mathrm{d}t \leq \|g\|_\infty \int_\mathbf{R} |f(x-t)|\ \mathrm{d}t = \|f\|_1 \|g\|_\infty $$

ce qui montre le caractère bien défini de la convolution et donne la majoration voulue.

# Exo 2 (8 points)
## 2.1
Soit $f$ dans $L^1(\mathbf{R})$ une fonction paire ($f(x)=f(-x)$ presque pour tout $x \in \mathbf{R}$). Montrer que $\hat{f}$ est également paire et que

$$ \hat{f}(\xi) = 2\int_0^\infty f(x)\cos(2\pi \xi x)\ \mathrm{d}x. $$

**Réponse.**

$$ \begin{eqnarray*}
  \int_\mathbf{R} e^{-2i\pi\xi x}f(x)\ \mathrm{d}x & = &
  \int_\mathbf{R_-} e^{-2i\pi\xi x}f(x)\ \mathrm{d}x + \int_\mathbf{R_+} e^{-2i\pi\xi x}f(x)\ \mathrm{d}x\\ & = & \int_\mathbf{R_+} e^{2i\pi\xi y}f(-y)|-1|\ \mathrm{d}y + \int_\mathbf{R_+} e^{-2i\pi\xi x}f(x)\ \mathrm{d}x,
\end{eqnarray*} $$

d'où le résultat voulu en utilisant la parité de $f$ et le fait que $\cos u=\mathrm{Re}(e^{\pm iu})$.

## 2.2
En déduire la transformée de Fourier de $\chi_{[-1,1]}$, la fonction caractéristique de $[-1,1]$.

**Réponse.**

$$ \widehat{\chi_{[-1,1]}}(\xi) = 2\mathrm{sinc}(2\pi\xi) $$

## 2.3
Montrer qu’il existe deux réels $a$ et $b$ tels que

$$ \chi_{[0,1]}(x) = \chi_{[-1,1]}(ax+b), $$

et en déduire la transformée de Fourier de $\chi_{[0,1]}$.

**Réponse.** Prendre $a=2$ et $b=-1$ (*cf.* $x \mapsto 2x-1$ envoie $[0,1]$ sur $[-1,1]$), de sorte que (effet translation / homothétie sur tranformée de Fourier)

$$ \widehat{\chi_{[0,1]}}(\xi) = e^{-i\pi\xi}\mathrm{sinc}(\pi\xi) $$

## 2.4
Montrer que le produit de convolution $\chi_{[0,1]} * \chi_{[0,2]}$ appartient à $L^1(\mathbf{R}) \cap L^\infty(\mathbf{R})$ et le calculer.

**Réponse.** On a

$$ \begin{eqnarray*}
  \chi_{[0,1]} * \chi_{[0,2]}(x) & = & \int_0^1 \chi_{[0,2]}(x-t)\ \mathrm{d}t\\
  & = & \int_{x-1}^x \chi_{[0,2]}(s)|-1|\ \mathrm{d}s
\end{eqnarray*} $$

en posant $s=x-t \in [x-1,x]$. En étudiant les positions relatives des intervalles $[x,x+1]$ et $[0,2]$, on voit qu'on a $5$ cas : 
- (i) si $x \leq 0$, la convolée vaut $0$
- (ii) si $x \in [0,1]$, la convolée vaut $\int_0^x \mathrm{d}s = x$
- (iii) si $x \in [1,2]$, la convolée vaut $\int_{x-1}^x \mathrm{d}s = 1$
- (iv) si $x \in [2,3]$, la convolée vaut $\int_{x-1}^2 \mathrm{d}s = 3-x$
- (v) si $x \geq 3$, la convolée vaut $0$.

## 2.5
Calculer la tranformée de Fourier $\widehat{\chi_{[0,1]} * \chi_{[0,2]}}$ de ce produit de convolution.

**Réponse.** En utilisant le fait que la transformée d'un produit de convolution est égale au produit des transformées, et que (homothétie ou translation)

$$ \widehat{\chi_{[0,2]}}(\xi) = 2e^{-2i\pi\xi}\mathrm{sinc}(2\pi\xi) $$

on a

$$ \widehat{\chi_{[0,1]} * \chi_{[0,2]}} =
2e^{-3i\pi\xi}\mathrm{sinc}(\pi\xi) \mathrm{sinc}(2\pi\xi). $$

# Exo 3 (7 points)
## 3.1
Soit $\alpha$ un réel, déterminer l’abscisse de convergence de la fonction $f:\mathbf{R}_+ \to \mathbf{R}$, $f(t)=te^{\alpha t}$, puis calculer sa transformée de Laplace.

**Réponse.**

$$ \mathscr{L}(te^{\alpha t})(s) = -\mathscr{L}(e^{\alpha t})'(s) = \frac{1}{(s-\alpha)^2},\quad \mathrm{Re}(s) > s_0 = \alpha. $$

## 3.2
On considère l’équation différentielle ordinaire suivante : trouver $y$ deux fois dérivable telle que

$$ y’’(t)-2y'(t)+y(t) = 0,\quad t \geq 0,\\
y(0)=1,\ y’(0)=0. $$

On admet qu’elle possède une unique solution, notée $y$. Montrer que, partout où elle est définie, la transformée de Laplace $\mathscr{L}y$ vérifie l’équation

$$ \mathscr{L}y(s) = \frac{A}{s-1} + \frac{B}{(s-1)^2} $$

avec $A$ et $B$ deux réels que l’on précisera.

**Réponse.** $A=1$, $B=-1$

## 3.3
En déduire la solution $y$ de l’équation différentielle.

**Réponse.** $y(t)=e^t-te^t$, $t \geq 0$
