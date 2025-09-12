![PNS](https://raw.githubusercontent.com/pns-mam/mi1/master/logo-pns.png)

## MAM3

# Mathématiques de l'ingénieur.e 1
# 2024-25
# TD 3 - Mesures

## Exercice 1

Soit $E$ un ensemble non-vide.

### 1.1
Soit $A \subset E$, non-vide et distincte de $E$. Déterminer $\mathscr{B}(\lbrace A \rbrace)$.

### 1.2
Soit $\mathscr{F}:=\lbrace A,B,C \rbrace$ une partition de $E$. Déterminer $\mathscr{B}(\mathscr{F})$.

### 1.3
Déterminer la tribu sur $\mathbf{R}$ engendrée par la famille $\lbrace [0,1[,[1,2],]2,3] \rbrace$.

## Exercice 2

Soit $(E,\mathscr{T})$ un espace mesurable, et soit $A$ une partie de $E$. On note $\chi_A$ la fonction indicatrice de $A$. Montrer que cette application est mesurable de $(E,\mathscr{T})$ dans $(\mathbf{R},\mathscr{B}_{\mathbf{R}})$ si et seulement si $A$ est mesurable.

## Exercice 3

Soit $(E,\mathscr{T})$ un espace mesurable, et soit $F$ un ensemble muni de la tribu $\mathscr{B}(\mathscr{A})$ engendrée par une famille de parties $\mathscr{A}$. Montrer que $f:E \to F$ est mesurable pour les tribus précédentes si et seulement si

$$ (\forall B \in \mathscr{A}) : f^{-1}(B) \in \mathscr{T}. $$

## Exercice 4 (mesure de Dirac)

Soit $(E,\mathscr{T})$ un espace mesurable, et soit $a$ un élément de $E$. On définit
$\delta_a : \mathscr{T} \to \mathbf{R}$ par

$$ \delta_a(A) := 1 \text{ si $A \ni a$, $0$ sinon.} $$

Montrer que $\delta_a$ définit une mesure sur
$(E,\mathscr{T})$.

## Exercice 5 (mesure de comptage)
On définit $\mu_d : \mathscr{P}(\mathbf{N}) \to \mathbf{R}$ par

$$ \mu_d(A) := \text{card}(A). $$

Montrer que $\mu_d$ de définit une mesure sur $\mathbf{N}$ muni de sa tribu discrète.
