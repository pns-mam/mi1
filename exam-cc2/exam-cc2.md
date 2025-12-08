![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2025-26
# Exam CC no. 2

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants.
Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

## Exo 1 (6 points)

Pour chacune des expressions ci-dessous (où $n \geq 1$) dire si la limite quand $n \to \infty$ existe et, le cas échéant, déterminer cette limite.

### 1.1
$$ \int_0^\infty \frac{1}{x^n + e^x}\,\mathrm{d}x $$

**Correction.** Soit $f_n(x)= \frac{1}{x^n + e^x}$. Si $0<x<1$, $\lim_{n\to \infty}f_n(x)= \frac{1}{e^x}$. Si $x>1$, $\lim_{n\to \infty}f_n(x)=0$. Pour tout $x\geq 0$, $f_n(x)\leq e^{-x}$ (qui est intégrable). Par le théorème de convergence dominée, 

$$
\lim_{n\to \infty} \int_0^\infty f_n(x)\,\mathrm{d}x =\int_0^\infty \lim_{n\to \infty}  f_n(x) \,\mathrm{d}x = \int_0^1 e^{-x}\,\mathrm{d}x = 1-1/e.
$$

### 1.2

$$ \int_0^\infty \frac{\ln(1+x/n)}{1+x^2}\,\mathrm{d}x $$

**Correction.** $\lim_{n\to \infty} \ln(1+x/n)=0$. De plus $\frac{\ln(1+x/n)}{1+x^2}\leq \frac{\ln(1+x)}{1+x^2}$. La fonction $x\mapsto \frac{\ln(1+x)}{1+x^2}$ est intégrable sur $[0,\infty[$: elle est bien bornée sur ce domaine et un équivalent en $+\infty$ est $\frac{\ln(x)}{x^2}$ qui est intégrable (c'est une intégrale de Bertrand).
Donc 

$$
\lim_{n\to \infty} \int_0^\infty \frac{\ln(1+x/n)}{1+x^2}\,\mathrm{d}x =0.
$$

### 1.3

$$ \int_0^n \frac{nx}{1+e^{x/n}}\,\mathrm{d}x $$

**Correction.** Soit $f_n(x) = \frac{nx}{1+e^{x/n}} \chi_{[0,n]}(x)$. On a $\frac{(n+1)x}{1+e^{x/(n+1)}}\geq  \frac{nx}{1+e^{x/n}}$ et $\chi_{[0,n+1]}(x)\geq  \chi_{[0,n]}(x)$. Donc $f_{n+1}(x)\geq f_n(x)$. Par ailleurs $\lim_{n\to \infty} f_n(x)=+\infty$ si $x>0$. Donc par le théorème de convergence monotone,


$$ \lim_{n\to \infty} \int_0^n \frac{nx}{1+e^{x/n}}\,\mathrm{d}x =+\infty.$$


# Exercice 2 (5 points)

Soit

$$ F(t) := \int_1^\infty \frac{\cos(tx)}{x}e^{-x}\ \mathrm{d}x,\quad t \in \mathbf{R}. $$

### 2.1
Montrer que l'on définit bien ainsi une fonction de $\mathbf{R}$ dans $\mathbf{R}$.

### 2.2
Montrer que $F$ est dérivable sur $\mathbf{R}$ et calculer sa dérivée.

### 2.3
En déduire une nouvelle expression de $F$.

# Exercice 3 (4 points)

## 3.1

Montrer que la fonction ci-dessous appartient à $L^1([0,\infty])$ : 

$$ f(x) := \frac{1}{x(1 + |\ln x|)^2}\,,\quad x > 0. $$

## 3.2

Montrer que la fonction ci-dessous appartient à $L^{3/2}([0,\infty])$ : 

$$ g(x) := \frac{\sin x}{x(1 + x)}\,,\quad x > 0. $$

## 3.3

En déduire que $f^{1/3}g$ appartient à $L^1([0,\infty])$.

# Exercice 4 (5 points)

## 4.1

On considère une suite d'applications mesurables $f_n : \mathbf{R} \to \mathbf{R}$. À l'aide du théorème de convergence monotone, montrer que

$$ \int_{\mathbf{R}} \sum_{n=0}^\infty |f_n(x)|\,\mathrm{d}x = \sum_{n=0}^\infty \int_{\mathbf{R}} |f_n(x)|\,\mathrm{d}x. $$

**Indication.** Considérer la suite d'applications $(\sum_{n=0}^N |f_n|)_N$ définie par les sommes partielles.

## 4.2

À l'aide du théorème de convergence dominée, en déduire que, sous l'hypothèse

$$ \sum_{n=0}^\infty \int_{\mathbf{R}} |f_n(x)|\,\mathrm{d}x < \infty, $$

on a 

$$ \int_{\mathbf{R}} \sum_{n=0}^\infty f_n(x)\,\mathrm{d}x = \sum_{n=0}^\infty \int_{\mathbf{R}} f_n(x)\,\mathrm{d}x. $$

## 4.3

Déterminer

$$ \int_{\mathbf{R}} \sum_{n=0}^\infty \frac{1}{1 + (n+1)^4 x^2}\,\mathrm{d}x. $$

