![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)
## MAM3
# Mathématiques de l'ingénieur.e 1
# 2025-26
# Exam CC no. 3
**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants. Le barème prévisionnel est indiqué pour chaque exercice.**
**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.**

# Exercice 1 (4 points)
Soient $f$ et $g$ dans $L^1(\mathbf{R})$.

## 1.1
Montrer que $\hat{f}g$ et $f\hat{g}$ sont encore dans $L^1(\mathbf{R})$.

**Réponse.** Pour $f \in L^1(\mathbf{R})$, sa transformée de Fourier $\hat{f} \in \mathcal{C}_0(\mathbf{R})$, donc $\hat{f}$ est bornée. Comme $g \in L^1(\mathbf{R})$, on en déduit $\hat{f}g \in L^1(\mathbf{R})$. De même, $f\hat{g} \in L^1(\mathbf{R})$.

## 1.2
À l'aide du théorème de Fubini, montrer que
$$\int_\mathbf{R} \hat{f}g\,\mathrm{d}x = \int_\mathbf{R} f\hat{g}\,\mathrm{d}x.$$

**Réponse.** Par définition, $\hat{f}(x) = \int_\mathbf{R} f(y)e^{-2i\pi xy}\,\mathrm{d}y$. Donc :

$$\int_\mathbf{R} \hat{f}(x)g(x)\,\mathrm{d}x = \int_\mathbf{R} \left(\int_\mathbf{R} f(y)e^{-2i\pi xy}\,\mathrm{d}y\right)g(x)\,\mathrm{d}x$$

Pour appliquer Fubini, vérifions l'intégrabilité de $|f(y)g(x)e^{-2i\pi xy}| = |f(y)||g(x)|$ sur $\mathbf{R}^2$ :

$$\int_{\mathbf{R}^2} |f(y)||g(x)|\,\mathrm{d}x\,\mathrm{d}y = \left(\int_\mathbf{R} |f(y)|\,\mathrm{d}y\right)\left(\int_\mathbf{R} |g(x)|\,\mathrm{d}x\right) = \|f\|_{L^1}\|g\|_{L^1} < \infty$$

Le théorème de Fubini permet donc d'intervertir les intégrations :

$$\int_\mathbf{R} f(y)\left(\int_\mathbf{R} g(x)e^{-2i\pi xy}\,\mathrm{d}x\right)\,\mathrm{d}y = \int_\mathbf{R} f(y)\hat{g}(y)\,\mathrm{d}y$$

# Exercice 2 (6 points)

## 2.1
Soit $f_n(x) := (-1)^n\frac{x^n}{n+1}$, $x \in \mathbf{R}$, $n \geq 0$. Montrer que

$$ \sum_{n \geq 0} \int_0^1 |f_n(x)|\,\mathrm{d}x < \infty. $$

**Réponse.** On calcule :

$$\int_0^1 |f_n(x)|\,\mathrm{d}x = \int_0^1 \frac{x^n}{n+1}\,\mathrm{d}x = \frac{1}{n+1}\left[\frac{x^{n+1}}{n+1}\right]_0^1 = \frac{1}{(n+1)^2}$$

Donc :

$$\sum_{n \geq 0} \int_0^1 |f_n(x)|\,\mathrm{d}x = \sum_{n \geq 0} \frac{1}{(n+1)^2} < \infty$$

## 2.2
En déduire que l'intégrale ci-dessous est bien définie :

$$ \int_0^1 \sum_{n \geq 0} f_n(x)\,\mathrm{d}x. $$

**Réponse.** D'après la question 2.1, $\sum_{n \geq 0} \int_0^1 |f_n(x)|\,\mathrm{d}x < \infty$. Par le théorème de Tonelli, on peut intervertir somme et intégrale, ce qui garantit que $\sum_{n \geq 0} f_n$ est intégrable sur $[0,1]$, donc que $\int_0^1 \sum_{n \geq 0} f_n(x)\,\mathrm{d}x$ est bien définie.

## 2.3
Déterminer la valeur de cette intégrale.

**Réponse.** Par interversion somme-intégrale :

$$\int_0^1 \sum_{n \geq 0} f_n(x)\,\mathrm{d}x = \sum_{n \geq 0} \int_0^1 (-1)^n\frac{x^n}{n+1}\,\mathrm{d}x = \sum_{n \geq 0} \frac{(-1)^n}{(n+1)^2} = \frac{\pi^2}{12}$$

## 2.4
En déduire la valeur de l'intégrale

$$ \int_0^1 \frac{\ln(1+x)}{x}\mathrm{d}x. $$

**Réponse.** Pour $|x| < 1$, la série de terme général $\frac{(-1)^n x^{n+1}}{n+1}$ converge simplement vers $\ln(1+x)$, de sorte que $\sum_{n \geq 0} f_n(x) = \frac{\ln(1+x)}{x}$ sur $]0,1]$. Par conséquent :
$$\int_0^1 \frac{\ln(1+x)}{x}\,\mathrm{d}x = \int_0^1 \sum_{n \geq 0} f_n(x)\,\mathrm{d}x = \frac{\pi^2}{12}$$

# Exercice 3 (4 points)

## 3.1
Soit $a > 0$. Déterminer la transformée de Fourier de $h_a(x) := e^{-a|x|}$, $x \in \mathbf{R}$. 

**Réponse.** La fonction $h_a$ étant paire, sa transformée de Fourier vaut :
$$\hat{h}_a(\xi) = \int_\mathbf{R} e^{-a|x|}e^{-2i\pi\xi x}\,\mathrm{d}x = 2\int_0^\infty e^{-ax}\cos(2\pi\xi x)\,\mathrm{d}x$$
Comme $\cos(2\pi\xi x) = \text{Re}(e^{2i\pi\xi x})$, on a :
$$\int_0^\infty e^{-ax}\cos(2\pi\xi x)\,\mathrm{d}x = \text{Re}\left(\int_0^\infty e^{-(a-2i\pi\xi)x}\,\mathrm{d}x\right) = \text{Re}\left(\frac{1}{a-2i\pi\xi}\right)$$
$$= \frac{a}{a^2+4\pi^2\xi^2} \cdot$$

## 3.2
Soit $\beta \in \mathbf{R}$. À l'aide de la question précédente, montrer que
$$ e^{-|\beta|} = \frac{2}{\pi} \int_0^\infty \frac{\cos(\beta y)}{1+y^2}\mathrm{d}y. $$

**Réponse.** Par la formule d'inversion de Fourier, pour $a = 1$ :
$$e^{-|\beta|} = h_1(\beta) = \int_\mathbf{R} \hat{h}_1(\xi)e^{2i\pi\xi\beta}\,\mathrm{d}\xi = \int_\mathbf{R} \frac{2}{1+4\pi^2\xi^2}e^{2i\pi\xi\beta}\,\mathrm{d}\xi$$
Par parité :
$$= 2\int_0^\infty \frac{2}{1+4\pi^2\xi^2}\cos(2\pi\xi\beta)\,\mathrm{d}\xi$$
En posant $y = 2\pi\xi$, on a :
$$= 2\int_0^\infty \frac{2}{1+y^2}\cos(\beta y)\frac{\mathrm{d}y}{2\pi} = \frac{2}{\pi}\int_0^\infty \frac{\cos(\beta y)}{1+y^2}\,\mathrm{d}y$$

# Exercice 4 (6 points)

## 4.1
Soit $\lambda > 0$ et soit
$$ f_\lambda(x) := \lambda e^{-\lambda x} \chi_{[0,+\infty[}(x),\quad x \in \mathbf{R}. $$
Montrer que $f_\lambda \in L^1(\mathbf{R})$ et que
$$ \int_{\mathbf{R}} f_\lambda\,\mathrm{d}x = 1. $$

**Réponse.** On a :
$$\int_\mathbf{R} |f_\lambda(x)|\,\mathrm{d}x = \int_0^\infty \lambda e^{-\lambda x}\,\mathrm{d}x = \lambda\left[-\frac{e^{-\lambda x}}{\lambda}\right]_0^\infty = \lambda \cdot \frac{1}{\lambda} = 1 < \infty$$
Donc $f_\lambda \in L^1(\mathbf{R})$ et $\int_\mathbf{R} f_\lambda\,\mathrm{d}x = 1$.

## 4.2
Soient $\lambda$ et $\mu$ strictement positifs, $\lambda \neq \mu$, déterminer le produit de convolution $f_\lambda * f_\mu$.

**Réponse.** Pour $x < 0$, $f_\lambda * f_\mu(x) = 0$ car les supports ne se chevauchent pas. Pour $x \geq 0$ :
$$f_\lambda * f_\mu(x) = \int_0^x \lambda e^{-\lambda y} \cdot \mu e^{-\mu(x-y)}\,\mathrm{d}y = \lambda\mu e^{-\mu x}\int_0^x e^{(\mu-\lambda)y}\,\mathrm{d}y$$
$$= \lambda\mu e^{-\mu x}\left[\frac{e^{(\mu-\lambda)y}}{\mu-\lambda}\right]_0^x = \frac{\lambda\mu}{\mu-\lambda}e^{-\mu x}(e^{(\mu-\lambda)x}-1)$$
$$= \frac{\lambda\mu}{\mu-\lambda}(e^{-\lambda x} - e^{-\mu x})$$
Donc :
$$f_\lambda * f_\mu(x) = \frac{\lambda\mu}{\mu-\lambda}(e^{-\lambda x} - e^{-\mu x})\chi_{[0,+\infty[}(x)$$

## 4.3
Soit $\lambda > 0$, et soient $X$ et $Y$ deux variables aléatoires indépendantes de même loi, toutes deux de densité $f_\lambda$. Déterminer la densité de la loi de $X + Y$.

**Réponse.** La densité de $X + Y$ est donnée par $f_\lambda * f_\lambda$. Pour $x \geq 0$ :
$$f_\lambda * f_\lambda(x) = \int_0^x \lambda e^{-\lambda y}\cdot \lambda e^{-\lambda(x-y)}\,\mathrm{d}y = \lambda^2 e^{-\lambda x}\int_0^x \mathrm{d}y = \lambda^2 x e^{-\lambda x}$$
Donc :
$$f_\lambda * f_\lambda(x) = \lambda^2 x e^{-\lambda x}\chi_{[0,+\infty[}(x)$$
