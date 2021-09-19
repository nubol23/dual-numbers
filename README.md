# Dual Numbers

This repository implements dual numbers with it's operations as a class.

Dual numbers are a kind o hyperreal number system, which has infinitesimals as elements, these infinitesimals are represented by $\varepsilon$ and satisfy the condition $\varepsilon^2=0$.

A dual number is of the form $a+b\varepsilon$, with $a$ and $b$ real numbers. They can be added, subtracted, multiplied and divided.

It's most useful property is that a function's Taylor expansion at a dual number is equal to
$$
f(a+b\varepsilon)=\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}b^n\varepsilon^n=f(a)+bf'(a)\varepsilon
$$
this way is computationally cheap to compute the derivative evaluated at $a$ by setting $b=1$.