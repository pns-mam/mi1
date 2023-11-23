![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1

# 2023-24

# TD 8 - Convolution

## Exercice 1

### 1.1
Soient $f \in L^1(\mathbf{R})$ et $g \in L^\infty(\mathbf{R})$, montrer que $f * g$ est bien définie, que $f * g$ appartient à $L^\infty(\mathbf{R})$ et que

$$ ||f * g||\_\infty \leq ||f||\_1 \cdot ||g||_\infty. $$

### 1.2
Soient $f \in L^2(\mathbf{R})$ et $g \in L^2(\mathbf{R})$, montrer que $f * g$ est bien définie, que $f * g$ appartient à $L^\infty(\mathbf{R})$ et que

$$ ||f * g||_\infty \leq ||f||_2 \cdot ||g||_2. $$

## Exercice 2

Montrer que les produits de convolution ci-dessous sont bien définis et les calculer :

### 2.1

$$ \chi_{[0,1]} * \chi_{[0,1]} $$

### 2.2

$$ \chi_{[-a,a]} * \cos,\quad \chi_{[-a,a]} * \sin \quad (a > 0) $$

### 2.3

$$ f * H $$ 

pour $f \in L^1(\mathbf{R})$ et $H := \chi_{\mathbf{R}_+}$

## Exercice 3

### 3.1
Soient $f$ et $g$ dans $L^1(\mathbf{R})$, montrer que

$$ \widehat{f * g} = \widehat{f} \cdot \widehat{g}. $$

### 3.2
Déterminer la transformée de Fourier de $\chi_{[0,1]} * \chi_{[0,1]} * \chi_{[0,1]}$.