![PNS](../logo-pns.png)
## MAM3
# Mathématiques de l'ingénieur.e 1
# 2023-24

# TD 9 - Équation de la chaleur

## Exo 1 

Soit

$$
G_\sigma:x\mapsto\frac{1}{\sigma \sqrt{2 \pi}}e^{-\frac{x^2}{2\sigma^2}}
$$

et soit $\widehat{G}_\sigma$ sa transformée de Fourier.

### 1.1
Montrer que $\widehat{G}_\sigma$ est dérivable sur $\mathbf{R}$.

### 1.2
En déduire que $\widehat{G}\_\sigma$ est solution une équation différentielle linéaire et la résoudre en s'appuyant sur le problème de Cauchy de condition initiale $\widehat{G}_\sigma(0)$ (que l'on calculera).

## Exo 2
Soit $f \in L^1(\mathbf{R})$ telle que

$$
f(t) = \int_{-\infty}^t g(s)\ \mathrm{d}s
$$

avec $g \in L^1(\mathbf{R})$. On définit alors et on note $f':=g$.
Montrer que pour tout $\xi \in \mathbf{R}$,

$$
\widehat{f'}(\xi)=2i\pi\xi\widehat{f}(\xi).
$$

## Exo 3
On considère une fonction qui à tout $(t,x)\in [0,+\infty[\times \mathbf{R}$, associe $u(t,x)\in \mathbf{R}.$ On suppose que pour $t\geq 0$, $u(t,\cdot), \partial_x u(t,\cdot), \partial_{xx} u(t,\cdot)$ sont toutes dans $L^1(\mathbf{R})$ (au sens de l'exercice 2).
On cherche à décrire un tel $u$ vérifiant l'équation de la chaleur unidimensionnelle

$$ \partial_t u(t,x) = \partial_{xx}u(t,x),\quad (t,x) \in ]0,+\infty[\times \mathbf{R}, $$

$$ u(0,x) = u_0(x). $$

### 3.1
Pour tout $t> 0$ fixé, exprimer $\widehat{\partial_{xx}u(t,\cdot)}$ en fonction de $\widehat{u(t,\cdot)}$. 

### 3.2
Montrer que pour tout $\xi \in \mathbf{R}$, $t\mapsto \widehat{u}(t,\xi)$ satisfait une équation différentielle linéaire. En déduire la valeur de $\widehat{u}(t,\xi)$ en fonction de $\widehat{u}_0(\xi)$.

### 3.3
En déduire $u(t,x)$ pour tout $t>0$ et $x\in \mathbf{R}$. (Indication : on rappelle la formule $\widehat{f * g}=\widehat{f} \cdot \hat{g}$ pour tout $f,g \in L^1(\mathbf{R})$.)
