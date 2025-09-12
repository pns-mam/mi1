![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2024-25
# Exam CC no. 2

**Durée 2H00. Documents non autorisés. Tous les exercices sont indépendants.
Le barème prévisionnel est indiqué pour chaque exercice.**

**Rendre sur des copies séparées les exercices 1 et 2 d'une part, 3 et 4 d'autre part.** 

# Exercice 1 (6 points)

## 1.1

Déterminer, si elle existe, la limite quand $n$ tend vers l'infini de la suite

$$ \int_{-\infty}^\infty |x|\cos((x+1)/n)e^{-x^2}\,\mathrm{d}x,\quad n \geq 1. $$

**Réponse.** Pour tout $x\in \mathbf{R}$, soit $f_n(x)=|x|\cos((x+1)/n)e^{-x^2}$. Pour tout $x\in \mathbf{R}$, on a $\lim_{n\to \infty} f_n(x)=|x|e^{-x^2}=:f(x)$.

Par ailleurs $|f_n|\leq f$ sur $\mathbf{R}$. Comme 

$$ \int_{\mathbf{R}} f(x)\mathrm{d}x = 2 \int_0^\infty x e^{-x^2} \mathrm{d}x = 2 \left[ -\frac{e^{-x^2}}{2} \right]_0^\infty=1, $$

on a $f\in L^1(\mathbf{R})$ (où on a employé la parité de $f$). Donc par le théorème de convergence dominée,

$$ \lim_{n\to \infty} \int_{\mathbf{R}} f_n(x)\mathrm{d}x = \int_{\mathbf{R}} f(x)\mathrm{d}x = 1. $$
## 1.2

Déterminer, si elle existe, la limite quand $n$ tend vers l'infini de la suite

$$ \int_0^n \frac{n \mathrm{d}x}{n + x^2}\,,\quad n \geq 1. $$

**Réponse.** Pour tout $x\in \mathbf{R}_+$, on note  $f_n(x)=\frac{n}{n + x^2} {\chi} _{[0,n]}$. Comme $\frac{x^2}{n}\geq \frac{x^2}{n+1}$ on en déduit que 

$$ \frac{1}{1+\frac{x^2}{n}} \leq \frac{1}{1+\frac{x^2}{n+1}}. $$

Puis de ${\chi} _{[0,n]} \leq {\chi} _{[0,n+1]}$ on déduit que $f_n\leq f _{n+1}$ sur $\mathbf{R} _+$. Enfin, on a  $\lim _{n\to \infty} f_n(x)=1$ donc par le théorème de convergence monotone,

$$ \lim _{n\to \infty} \int_0^n \frac{n \mathrm{d}x}{n + x^2}=\int_0^\infty \mathrm{d}x = \infty. $$ 

## 1.3

Déterminer, si elle existe, la limite quand $n$ tend vers l'infini de la suite

$$ \int_e^\infty \frac{n \sin(x/n)}{x^2 \ln^2 x}\,\mathrm{d}x,\quad n \geq 1. $$

**Réponse.** Pour tout $x\in [e,\infty[$, on note  $f_n(x)=\frac{n \sin(x/n)}{x^2 \ln^2 x}$. On remarque en premier lieu que pour to $x>0$, $\lim_{n\to \infty} \frac{\sin(x/n)}{x/n}=1$ et $\frac{\sin(x/n)}{x/n}\leq 1$. 

Donc pour tout $x\in [e,\infty[$, $\lim_{n\to \infty} f_n(x)=\frac{1}{x \ln^2(x)}=:f(x)$ et $|f_n(x)|\leq f(x)$. Par ailleurs, $f\in L^1([e,\infty[)$, par exemple car c'est une intégrale de Bertrand convergente (ou se prouve par le calcul ci-dessous).

Par le théorème de convergence dominée,

$$ \lim_{n\to \infty} \int_e^\infty f_n(x) \mathrm{d}x=\int_e^\infty f(x)\mathrm{d}x = \left[-\frac{1}{\ln x}\right]_e^\infty=1 $$ 

# Exercice 2 (5 points)

## 2.1

Montrer que la fonction

$$  F(t) := \int_0^\infty \frac{\cos(tx)e^{-x}}{1+x^2}\,\mathrm{d}x $$

est bien définie pour $t \in \mathbf{R}$.

**Réponse.** Pour $t\in \mathbf{R}$ et $x\in [0,\infty[$, on note $f(t,x)=\frac{\cos(tx)e^{-x}}{1+x^2}$. Pour tout $t\in \mathbf{R}$ fixé, $f(t,x)\leq e^{-x}=:g(x)$. Or $g\in L^1(\mathbf{R}_+)$ donc $f(t,\cdot)\in L^1(\mathbf{R} _+)$ pour tout $t$ et $F(t)$ est bien définie.

## 2.2

Montrer que la fonction $F$ est deux fois dérivable, et donner les expressions de $F'$ et $F''$.

**Réponse.** Pour tout $t\in \mathbf{R}$, $x>0$, $\frac{\partial}{\partial t} f(t,x)= - \frac{x \sin(tx)e^{-x}}{1+x^2}$ et $\left|\frac{\partial}{\partial t} f(t,x)\right|\leq x e^{-x}$. Par croissance comparée, $x\mapsto x e^{-x}$ est encore de classe $L^1(\mathbf{R} _+)$.

Par le théorème de dérivation des intégrales à paramètre, $F(t)$ est dérivable sur $\mathbf{R}$ de dérivée 

$$ F'(t) = - \int_0^\infty \frac{x \sin(tx)e^{-x}}{1+x^2}\,\mathrm{d}x. $$

Le même argument s'applique pour $F''$. $\frac{\partial^2}{\partial t^2} f(t,x)= - \frac{x^2 \cos(tx)e^{-x}}{1+x^2}$ et $\left|\frac{\partial^2}{\partial t^2} f(t,x)\right|\leq x^2 e^{-x}$. Par croissance comparée, $x\mapsto x^2 e^{-x}$ est de classe $L^1(\mathbf{R} _+)$.

Par le théorème de dérivation des intégrales à paramètre, $F'(t)$ est dérivable sur $\mathbf{R}$ de dérivée 

$$ F''(t) = - \int_0^\infty \frac{x^2 \cos(tx)e^{-x}}{1+x^2}\,\mathrm{d}x. $$

## 2.3

En déduire que $F$ vérifie l'équation différentielle

$$ F''(t) - F(t) = G(t),\quad t \in \mathbf{R}, $$

avec $G$ une fonction dont on donnera une expression explicite.

**Réponse.** On additionne simplement les deux intégrales obtenues:

$$ F''(t) - F(t) =  -\int_0^\infty \frac{(1+x^2) \cos(tx)e^{-x}}{1+x^2}\,\mathrm{d}x=-\int_0^\infty \cos(tx)e^{-x} \,\mathrm{d}x = Re\left(\left[-\frac{e^{it x-x}}{it-1}\right]_0^\infty\right)= Re\left(\frac{1}{it-1}\right) = - \frac{1}{1+t^2}.$$ 

# Exercice 3 (4 points)

## 3.1

Soient $f \in L^p(X,\mathscr{B},\mu)$ et $g \in L^q(X,\mathscr{B},\mu)$, avec $1/p + 1/q = 1/r$ et $p$, $q$, $r$ dans $[1,\infty[$. Montrer que $fg$ appartient à $L^r(X,\mathscr{B},\mu)$ et que

$$ \|fg\|_r \leq \|f\|_p \|g\|_q. $$

[**Indication** : noter que $1/(p/r) + 1/(q/r) = 1$, et que $f^r$ est dans $L^{p/r}$. ]

**Réponse.** Par hypothèse, $f^r$ est dans $L^{p/r}$ et $g^r$ est dans $L^{q/r}$ (noter que $p/r$ et $q/r$ sont nécessairement supérieurs ou égaux à $1$): comme $1/(p/r) + 1/(q/r) = 1$, on peut appliquer Hölder pour conclure que $f^r g^r$ est dans $L^1$ et que

$$ \|f^r g^r\|_1 \leq \|f^r\|_{p/r} \|g^r\|_{q/r} $$

et donc que (prendre la puissance $1/r$ des deux membres)

$$ \|fg\|_r \leq \|f\|_{p} \|g\|_{q}. $$

## 3.2

Soient $f_1 \in L^{p_1}(X,\mathscr{B},\mu)$, ..., $f_n \in L^{p_n}(X,\mathscr{B},\mu)$, avec $1/p_1 + \cdots + 1/{p_n} = 1/r$ et $p_1,\dots,p_n$, $r$ dans $[1,\infty[$. Montrer que $f_1 \cdots f_n$ appartient à $L^r(X,\mathscr{B},\mu)$ et que

$$ \|f_1 \cdots f_n\|_r \leq \|f_1\|_{p_1} \cdots \|f_n\|_{p_n}. $$

**Réponse.** La relation est vraie pour $n = 2$ d'après la question précédente. Supposons qu'elle est vraie au rang $n \geq 2$, et montrons, pour conclure par récurrence, qu'elle est alors vraie au rang $n + 1$. Soient $f_1,\dots,f_{n+1}$ vérifiant les hypothèses indiquées pour $p_1,\dots,p_{n+1}$ des réels dont la somme des inverses vaut $1/r$. Soit $s$ tel quel $1/s$ vaut $1/p_1 + \cdots 1/p_n$ ; par hypothèse de récurrence, $f_1 \cdots f_n$ appartient à $L^s$, et la question précédente appliquée à ce produit et à $f_{n+1}$ donne le résultat voulu puisque $1/s + 1/p_{n+1} = 1/r$.

# Exercice 4 (5 points)

## 4.1

Soient $\beta > \alpha > 0$. Monter que l'intégrale

$$ I := \int_0^\infty \frac{e^{-\alpha x} - e^{-\beta x}}{x}\,\mathrm{d}x $$

est bien définie.

**Réponse.** L'intégrande est continu donc mesurable, et positif puisque $\alpha < \beta$ : l'intégrale est donc bien définie.

## 4.2

Montrer que

$$ I := \int_0^\infty (\int_\alpha^\beta e^{-tx}\,\mathrm{d}t)\,\mathrm{d}x. $$

**Réponse.** Pour tout $x$ positif,

$$ \int_\alpha^\beta e^{-tx}\,\mathrm{d}t = \frac{e^{-\alpha x} - e^{-\beta x}}{x} \cdot $$

## 4.3

En déduire $I$.

**Réponse.** La fonction $(t,x) \mapsto e^{-tx}$ est mesurable et positive, donc Tonelli implique que

$$ \begin{align} I &= \int_0^\infty (\int_\alpha^\beta e^{-tx}\,\mathrm{d}t)\,\mathrm{d}x,\\
                   &= \int_\alpha^\beta (\int_0^\infty e^{-tx}\,\mathrm{d}x)\,\mathrm{d}t,\\
                   &= \int_\alpha^\beta \frac{1}{t}\,\mathrm{d}t,\\
                   &= \ln\beta - \ln\alpha.
   \end{align} $$
