#set text(font: "New Computer Modern")
#align(center)[
  #text(size: 20pt, style: "italic")[Negative Hypergeometric]
]
#align(center)[
  #text(size: 12pt, style: "italic")[Yehor Korotenko (#link("https://dobbikov.com")[dobbikov.com])]
]
#set heading(numbering: "1.1")
// #show math.equation: set numbering("1.1")
#set math.equation(numbering: "(1)")
#let no-num(content) = {
  math.equation(
    block: true, 
    numbering: none, 
    content
  )
}
Let's consider the next case: there are $N$ balls among which there are  $G$
red ones and  $N - G$ blue ones. We introduce $T$ - the number of balls we need
to take without returns in order to get  $r$ red ones. What is the probability that the number of balls $T$ is  $n$?

Our goal is to find:  $P(T = n)$. 
= PMF
- We have an urn with $N$ balls, with  $G$ red ones.
- $T = n$ means that on the  $n$'th draw we took exactly  $r$'th red ball.
== Number of ways to get $r$ red balls among  $n$ draws 
- Among the first $n-1$ draws we took exactly  $r-1$ red balls, the number of ways to put  $r-1$ red balls between  $n-1$ draws is  $binom(n-1, r-1)$.
- The $n$'th draw is our  $r$'th red ball.
- So we are left to count the number of ways to place  $G-r$ red left balls among  $N-n$ left balls in the urn. Why? #footnote[We have to count all the ways of placing #emph[all] the balls. To make an analogy, imagine the case when we shuffle a deck of cards and take $n$ first cards. Even though we don't care about the rest of the deck, we have to count the number of ways that the cards in the deck have positions in order to have the true probability.] 

== All possible outcomes
- The number of possible outcomes is the number of ways to put $G$ red balls among all the $N$ balls :
#no-num[
  $binom(N, G)$
]

== Final probability
Combining altogether we get:
$
P(T = n) = (binom(n-1, r-1)binom(N-n, G-r))/(binom(N, G))
$ 

= Expectation
$
EE[T] = r (N+1)/(G+1)
$<expectation> 

Let's also get an intuition of the @expectation. 
Imagine you line up all $N$ draw positions in a row:

#no-num[$ 1,2,3,…,N $]

Now you drop the $M$ successes randomly into this line.
Think of it like splitting the line into $M+1$ chunks:
- before the 1st success,
- between 1st and 2nd success,
- #math.dots
- after the last success.

On average, each chunk has length about $(N+1)/(G+1)$.
So the r-th success will typically sit at the end of the r-th chunk:

That’s all the formula says:
“the r-th success is expected at about r-times the average spacing between successes.”

= Variance
$
#text[Var(X)]=( r(M−r+1)(N+1)(N−M) )/((M+1)^2(M+2)).
$ 

Just by the formula of variance, no intuition here.
