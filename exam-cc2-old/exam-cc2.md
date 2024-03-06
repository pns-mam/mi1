![PNS](http://caillau.perso.math.cnrs.fr/logo-pns.png)
## MAM3
# Mathématiques de l'ingénieur.e 1
# 2022-2023

# Exam CC2

**Durée 2H. Documents non autorisés. Rendre sur deux copies séparées les exos 1 et 2 d'une part, 3 et 4 d'autre part.**

## Exo 1 (3 points)

Soit $(X,\mathscr{T})$ un espace mesurable. Soit $A$ une partie de $X$. Montrer que $A$ appartient à la tribu $\mathscr{T}$ si et seulement si l'application caractéristique $\chi_A : X \to \mathbf{R}$ est $(\mathscr{T},\mathscr{B}_{\mathbf{R}})$-mesurable, où $\mathscr{B}_{\mathbf{R}}$ désigne la tribu des boréliens.

(On rappelle que, par définition, $\chi_A(x)$ vaut $1$ si $x \in A$, $0$ sinon.)

**Réponse.** Si $A$ appartient à la tribu, soit $B \subset X$ (partie borélienne ou non !) On a quatre cas :
- $0 \notin B$, $1 \notin B$ : $\chi_A^{-1}(B)=\emptyset$,
- $0 \in B$, $1 \notin B$ : $\chi_A^{-1}(B)=X \setminus A$,
- $0 \notin B$, $1 \in B$ : $\chi_A^{-1}(B)=A$,
- $0 \in B$, $1 \in B$ : $\chi_A^{-1}(B)=X$.

Dans chacun des cas, on voit que l'image réciproque appartient à la tribu. Réciproquement, si $\chi_A$ est mesurable, comme $\{1\}$ est une partie fermée, c'est un borélien, donc $A=\chi_A^{-1}(\{1\}) \in \mathscr{T}$.

## Exo 2 (6 points)

Pour chacune des expressions ci-dessous (où $n \geq 1$) dire si la limite quand $n \to \infty$ existe et, le cas échéant, déterminer cette limite.

### 2.1
$$ \int_0^\infty e^{-nx}\cos(nx)\,\mathrm{d}x $$

**Réponse.** Soit $x \gt 0$, on voit que $f_n(x):=e^{-nx}\cos(nx)$ converge vers $0$ quand $n \to \infty$. Comme, pour tout $x \gt 0$ et $n \geq 1$,

$$ |f_n(x)| \leq e^{-x}, $$

on a domination par une fonction intégrable : le théorème de CV dominée implique que la limite existe et vaut $0$.

### 2.2
$$ \int_0^\infty \frac{\ln(1+x/n)}{1+x^2}\,\mathrm{d}x $$

**Réponse.** Soit $x \gt 0$, on voit que

$$ f_n(x) := \frac{\ln(1+x/n)}{1+x^2} \sim \frac{x}{n(1+x^2)} $$

converge vers $0$ quand $n \to \infty$. Comme, pour tout $x \gt 0$ et $n \geq 1$,

$$ |f_n(x)| \leq \frac{\ln(1+x)}{1+x^2}\,, $$

on a domination par une fonction intégrable (critère de Riemann) : le théorème de CV dominée implique que la limite existe et vaut $0$.

### 2.3
$$ \int_0^n \frac{nx}{1+e^x}\,\mathrm{d}x $$

**Réponse.** Soit $x \gt 0$, on voit que $f_n(x):=nx \chi_{[0,n]}(x)/(1+e^x)$, mesurable et positive, converge en croissant vers $\infty$ quand $n \to \infty$. Le théorème de CV monotone implique que la limite existe et vaut $\infty$.

## Exo 3 (6 points)

### 3.1
Montrer que la fonction

$$ F(t) := \int_0^\infty e^{-tx}\cos x\ \mathrm{d}x $$

est bien définie pour $t \gt 0$.

**Réponse.** Pour $t \gt 0$, $|e^{-tx}\cos x| \leq e^{-tx}$, d'où l'intégrabilité (et le caractère bien défini de $F(t)$).

### 3.2
Soit $t_0 > 0$ ; montrer que $F$ est continue en $t_0$.

**Réponse.** Posons $f(t,x):=e^{-tx}\cos x$ ; pour $t \in [t_0/2,t_0+1]$ et $x \geq 0$, on a

$$ |f(t,x)| \leq e^{-t_0 x/2}, $$

d'où la domination par une fonction intégrable. Comme $ t \mapsto f(t,x)$ est continue en $t_0$ pour tout $x \geq 0$, l'intégrale à paramètre est continue en $t_0$.

### 3.3
Soit $t_0 > 0$ ; montrer que $F$ est dérivable en $t_0$ et donner l'expression de sa dérivée.

**Réponse.** La fonction $t \mapsto f(t,x)$ est dérivable en tout $t \in ]t_0/2,t_0+1[$, quel que soit $x \geq 0$, et

$$ \left| \frac{\partial f}{\partial t}(t,x) \right| = |-xe^{-tx}\cos x| \leq xe^{-t_0 x/2}, $$

d'où la domination par une fonction intégrable. L'intégrale à paramètre est dérivable en $t_0$ et

$$ F'(t_0) = -\int_0^\infty xe^{-t_0 x}\cos x\,\mathrm{d}x. $$

### 3.4
Calculer $F(t)$ pour tout $t > 0$.

**Réponse.** On peut par exemple écrire

$$ F(t) = \text{Re} \int_0^\infty e^{(i-t)x}\,\mathrm{d}x = \frac{t}{t^2+1} \cdot $$

### 3.5
En déduire, pour $t > 0$, la valeur de

$$ \int_0^\infty xe^{-tx}\cos x\,\mathrm{d}x. $$

**Réponse.** D'après les questions 3.3 et 3.4,

$$ \int_0^\infty xe^{-tx}\cos x\,\mathrm{d}x = -F'(t) = \frac{t^2-1}{(t^2+1)^2} \cdot $$ 

## Exo 4 (5 points)
Soit $(X,\mathscr{T},\mu)$ un espace mesuré tel que $\mu(X) \lt \infty$.

### 4.1
Montrer que $L^\infty(X,\mathscr{T},\mu) \subset L^1(X,\mathscr{T},\mu)$.

**Réponse.** Soit $f$ dans $L^\infty(X,\mathscr{T},\mu)$, on a

$$ \int_X |f|\,\mathrm{d}\mu \leq \|f\|_\infty \int_X 1\,\mathrm{d}\mu = \mu(X)\|f\|_\infty \lt \infty. $$

### 4.2
Montrer que $L^2(X,\mathscr{T},\mu) \subset L^1(X,\mathscr{T},\mu)$.

(Indication : si $f$ appartient à $L^2(X,\mathscr{T},\mu)$, on pourra écrire $|f|=|f|\cdot 1$ et utiliser l'inégalité de Hölder.)

**Réponse.** Soit $f$ dans $L^2(X,\mathscr{T},\mu)$ ; comme $\mu(X) \lt \infty$, la fonction constante $g \equiv 1$ est aussi dans $L^2(X,\mathscr{T},\mu)$, et d'après l'inégalité de Hölder

$$ \int_X |f|\cdot 1\,\mathrm{d}\mu \leq \|f\|_2 \|g\|_2 = \sqrt{\mu(X)}\|f\|_2 \lt \infty. $$

### 4.3
Donner un contrexemple à chacune des inclusions précédentes quand $\mu(X)=\infty$.

**Réponse.** On prend $X=[1,\infty[$, $\mu=\mu_L$ et on voit que :
- la fonction constante égale à $1$ est dans $L^\infty(X)$, pas dans $L^1(X)$,
- la fonction $x \mapsto 1/x$ est dans $L^2(X)$, pas dans $L^1(X)$ (Riemann).
