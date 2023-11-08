![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1

# 2023-24

# TD 7 - Transformée de Fourier

## Exercice 1

### 1.1
Soit $f \in L^1(\mathbf{R})$, montrer que

$$ \widehat{\bar{f}}(\xi) = \bar{\widehat{f}}(-\xi),\quad \xi \in \mathbf{R}. $$

### 1.2
Montrer que si $f$ est réelle et paire, sa transformée de Fourier est également réelle et paire et que

$$ \widehat{f}(\xi) = 2\int_0^\infty f(x)\cos(2\pi\xi x)\ \mathrm{d}x. $$

### 1.3
Montrer que si $f$ est réelle et impaire, sa transformée de Fourier est imaginaire pure et impaire et que

$$ \widehat{f}(\xi) =-2i\int_0^\infty f(x)\sin(2\pi\xi x)\ \mathrm{d}x. $$

## Exercice 2
Calculer les transformée de Fourier des fonctions suivantes :

### 2.1
$$ f(x) := \frac{1}{T} \chi_{[-T/2,T/2]}(x),\quad x \in \mathbf{R} $$

### 2.2
$$ f(x) := e^{-ax}\chi_{[0,\infty[}(x),\quad x \in \mathbf{R} \quad (a > 0) $$

### 2.3
$$ f(x) := e^{-a|x|},\quad x \in \mathbf{R} \quad (a > 0) $$

## Exercice 3

### 3.1
Soit $f \in L^1(\mathbf{R})$, et soient $a$ et $b$ deux réels, $a \neq 0$. On pose $g(x) := f(ax+b)$, montrer que

$$ \widehat{g}(\xi) = \frac{e^{2i\pi b/a}}{|a|}\widehat{f}(\xi/a). $$

### 3.2
Soit $\Lambda$ la fonction triangle,

$$ \Lambda(x) = (1-|x|)\chi_{[-1,1]}(x),\quad x \in \mathbf{R}. $$

Déterminer la transformée de Fourier de $\Lambda(2x-1)$.

