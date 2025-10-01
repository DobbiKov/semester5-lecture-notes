#import "@local/dobbikov-book:1.0.0":*
#set math.equation(numbering: "(1)")
= Lebesgue
== Introduction
Almost all the probability theory is build around the *measure theory* and
*lebesgue integral*. You can skip this chapter if you are already familiar with
these two notions. However, I would highly recommend to read this chapter
anyway because I provide here an intuition to those notions and their
connection to the probability theory. The two last helped me a lot for
understanding the probability theory.

== When we pass to continuous
In continuous probability theory we introduce the notion of *measure* but why?
The most common example-_explanation_ is a random variable $X$ that describes a
height of a person.

Let $X$ be a random variable that returns a height of a person. \
We are used to describe our height using 3 digits. For example: mine is
$1.79$ cm. However, this number doesn't describe my real height, it is only a
good approximation.

There's nothing wrong with it because there is no need in high precision for
the height. Furthermore, you don't know all the digits of the  $pi$ number
(or do you?) even though it is one of the most important numbers in
engineering, what is left to say about our height?. However, in this particular
example, we suppose that  $X$ provide the real height of a person, i.e  $X in
RR^+$.

Now, imagine that we want to calculate the probability that the person has
height between $1.60$ cm and  $1.70$ i.e we want to calculate 
$
P(1.60 <= X <= 1.70)
$ 

In discrete probability we would iterate all the numbers between $1.60$ and
$1.70$, take the probability of having each of them and sum all of them up.
However, in our example, it is not possible. We can't sum over an interval of
real numbers because we can sum only over countable sets but $[1.60, 1.70]$
is not countable.

Hopefully, a continuous equivalent of sums exist -- an integral. We could possibly try to write:
$
P(X in [1.60, 1.70]) = integral_(1.60)^(1.70) P(X = x)d x
$<eq:probas-plus-integral-example> 
However, we come to another subtle point. What is a probability that the height
of your friend is $1.(64) = 1.64646464 dots$? 

== An other view on probability <sec:another-view-on-probas>
Before we continue, let's take a different approach of looking at probability.
Instead of asking for $P(X = k)$ "what are the chances that X equals k", we
could ask: what proportion of the whole sample equals to $k$. Let's make it clearer.
#ex("Balls in a box")[
  Let's consider a box where there are 2 blue balls, 5 red balls and 3 green
  balls. Clearly, the total number of balls is: 10, then if we take randomly a
  ball from that box the probability of the ball being green is $0.3$. But that
  is equivalent to say that blue balls are the  $0.3 = 30\%$ of all the balls.
]

== Infinite case
Let's continue with our question. What is the probability that the height
of your friend is $1.(64) = 1.64646464 dots$? Let's consider for our example that 
$forall x in RR^+$ there exists one and only one person with such a height.
That is to say that your friend is the only person in the world with such a
height. 

In order to find the probability of your friend having such a height, we can
find a proportion of the sample space that the number  $1.(64)$ take. According
to our hypothesis, there's only one person with such a height and for each
positive number there exist a person with such a height (what a crowded world).
Thus, we need to calculate how many persons in the world exist, or, simplier,
how many numbers are there in the $RR^+$. You could try to count but I'll tell
you anyway that there are infinitely many positive real numbers.

In conclusion,  
$
P(X = 1.(64)) = 1/(+infinity) = 0
$<eq:prob-164-0>

It may surprise you that your friend can't have such a height. Is there
something special about this number that no one can have it? The answer is no.
Actually, the are two ways of viewing this concept.

1. We need @eq:prob-164-0 to equal zero because the cardinal of $RR^+$ is
   infinity. But, in this case we lose intuition.
2. Even if your friend had such a height, there do not exist a tool to measure
   the height of your friend with such precision.

What does it mean for us? It means that the integral in
@eq:probas-plus-integral-example equals 0. Does it mean that we can't calculate
such probability?

No, we just need to use new tools in order to calculate that probability. This
is the first moment when we pass from discrete probability to continuous and
introduce new notion Probability Density Function (PDF) look @defn:pdf.

== Density
Obviously, I won't leave you just with a definition. Actually, there are two ways to introduce density in probability theory:
- Intuitive
- Rigorous

I will do both in this chapter. Let's start with intuitive one.

=== Intuitive way to see probability density
Do you remember how we introduced in @sec:another-view-on-probas another view
on probability. That is the key to understand the density function. Let's
remind the idea:

Instead of asking, what is the probability that an outcome will happen, we
could ask, what is the proportion of the whole sample space our outcome takes.

Let's imagine a city that is built along a road (for instance: Kryvyi Rih in
Ukraine). We introduce a random variable $X$ that returns the location between
$-infinity$ and  $+infinity$ where a random person lives.

#defn("Probability Density Function")[
 TODO 
]<defn:pdf>
