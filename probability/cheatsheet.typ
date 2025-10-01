#import "@local/dobbikov:1.0.0":*

#show: dobbikov.with(
  title: [CheatSheet (long version) de Probablilité],
  subtitle: none,
  author: "Yehor KORORTENKO",
  date: datetime.today(),
)



= Mathématiques Générales

== Coefficient binomiale

La formule est la suivante:
$
binom(n, k) = (n!)/((n-k)!k!)
$ 

Les propriétés utiles:

1. $binom(n, 1) = n$
2. $ binom(n, 0) = binom(n, n) = 1$ 
3. $binom(n, k) = binom(n-1, k-1) + binom(n-1, k)$

= Qu'est-ce que cela signifie?
== Montrer que la loi converge
Quand on est demandé de montrer que #emph[la loi converge]. Il faut montrer,
que la loi d'une variable aléatoire converge vers une variable aléatoire d'#emph[une autre loi].

On peut utiliser des théorèmes des approximation comme:
- La loi binomiale $Beta(n, p)$ converge vers  $P(p n)$ poisson.

etc.
