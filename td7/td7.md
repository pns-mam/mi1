![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1

# 2025-26

# TD 7 - Fubini

## Exercice 1

Soient $a$ et $b$ deux réels, $a < b$. Soit $f \in L^1([a,b]^2)$.

### 1.1

Montrer que les deux intégrales ci-dessous sont bien définies et égales : 

$$ \int_a^b \left( \int_a^x f(x,y)\,\mathrm{d}y \right) \mathrm{d}x
 = \int_a^b \left( \int_y^b f(x,y)\,\mathrm{d}x \right) \mathrm{d}y =: I. $$

### 1.2

On suppose de plus que, presque pour tout $(x,y) \in [a,b]^2$, on a $f(y,x)=f(x,y)$. Montrer que

$$ I = \frac{1}{2} \int_{[a,b]^2} f(x,y)\,\mathrm{d}x\mathrm{d}y. $$

## Exercice 2

Calculer de deux façons différentes

$$ \int_{\mathbf{R}_+^2} \frac{\mathrm{d}x\mathrm{d}y}{(1+y)(1+x^2y)} $$

et en déduire la valeur de 

$$ \int_0^\infty \frac{\ln x\,\mathrm{d}x}{x^2-1} \cdot $$

## Exercice 3

Soit $f : \mathbf{R}^2 \to \mathbf{R}$ dérivable et possédant des dérivées partielles croisées $\partial^2 f/\partial x\partial y$ et 
$\partial^2 f/\partial y\partial x$ continues.

### 3.1

Soient $a \leq b$ et $c \leq d$, calculer

$$ \int_c^d \left( \int_a^b \frac{\partial^2 f}{\partial x\partial y}(x,y)\,\mathrm{d}x \right) \mathrm{d}y \quad \text{et} \quad
   \int_a^b \left( \int_c^d \frac{\partial^2 f}{\partial y\partial x}(x,y)\,\mathrm{d}y \right) \mathrm{d}x. $$

### 3.2

À l'aide du théorème de Fubini, montrer que

$$ \int_c^d \left( \int_a^b \left( \frac{\partial^2 f}{\partial x\partial y}(x,y) - \frac{\partial^2 f}{\partial y\partial x}(x,y) \right) \,\mathrm{d}x \right) \mathrm{d}y = 0. $$

Conclure.

## Exercice 4

### 4.1

Soit $f_n : X \to \mathbf{\overline{R}}$ une suite d'applications mesurables définies sur $(X,\mathscr{B},\mu)$, espace mesuré $\sigma$-fini, telle que

$$ \sum_n \int_X |f_n(x)|\,\mathrm{d}x < \infty. $$

Montrer qu'on a

$$ \int_X \sum_n f_n(x)\,\mathrm{d}x =
   \sum_n \int_X f_n(x)\,\mathrm{d}x. $$

## 4.2

Déterminer, si elle existe, la valeur de

$$ \int_0^\infty \sum_{n \geq 1} (-1)^{n+1}e^{-n^2 x}\,\mathrm{d}x. $$
