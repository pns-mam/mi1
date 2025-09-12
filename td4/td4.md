![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1

# 2024-25

# TD 4 - Convergence

## Exercice 1

### 1.1
Déterminer, si elles existent, les limites suivantes :

$$ 
\lim_{n \to \infty} \int_0^1 \frac{1+nx}{(1+x)^n}\ \mathrm{d}x,\quad
   \lim_{n \to \infty} \int_0^1 \sin\frac{1}{nx}\ \mathrm{d}x \quad (n \geq 1),\quad
   \lim_{n \to \infty} \int_0^n e^{-x}(n+x)\ \mathrm{d}x.
$$

### 1.2
Montrer que

$$ \lim_{n \to \infty} \int_0^\infty \frac{e^{-nx}}{\sqrt{x}}\ \mathrm{d}x = 0. $$

### 1.3
Déterminer, si elle existe, la limite suivante :

$$ \lim_{n \to \infty} \int_0^n (1-x/n)^n \cos x\ \mathrm{d}x \quad (n \geq 1). $$

## Exercice 2

Étant donné un réel $\alpha$, on souhaite déterminer, si elle existe, la limite

$$ L_\alpha := \lim_{n \to \infty} \int_0^n (1-x/n)^n e^{\alpha x}\ \mathrm{d}x \quad (n \geq 1). $$

### 2.1
Montrer que la limite existe pour $\alpha=1/2$ et déterminer $L_{1/2}$ à l'aide du théorème de convergence dominée.

### 2.2
On pose

$$ h_n(x) := (1-x/n)^n e^{\alpha x}\chi_{[0,n]}(x),\quad x \in \mathbf{R}_+ \quad (n \geq 1). $$

En étudiant $\ln(h_{n+1}(x)/h_n(x))$ pour $x \in [0,n[$, montrer que la suite $h_n$ est croissante, puis conclure quant à l'existence de $L_\alpha$ et sa valeur éventuelle à l'aide du théorème de convergence monotone.
