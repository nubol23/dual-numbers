# Dual Numbers

This repository implements dual numbers with it's operations as a class.

Dual numbers are a kind o hyperreal number system, which has infinitesimals as elements, these infinitesimals are represented by ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20%5Cvarepsilon%7D) and satisfy the condition ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20%5Cvarepsilon%5E2%3D0%7D).

A dual number is of the form ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20a&plus;b%5Cvarepsilon%7D), with ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20a%7D) and ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20b%7D) real numbers. They can be added, subtracted, multiplied and divided.

It's most useful property is that a function's Taylor expansion at a dual number is equal to

![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7Df%28a&plus;b%5Cvarepsilon%29%3D%5Csum_%7Bn%3D0%7D%5E%7B%5Cinfty%7D%20%5Cfrac%7Bf%5E%7B%28n%29%7D%28a%29%7D%7Bn%21%7Db%5En%5Cvarepsilon%5En%3Df%28a%29&plus;bf%27%28a%29%5Cvarepsilon%7D)

this way is computationally cheap to compute the derivative evaluated at ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20a%7D) by setting ![equation](https://latex.codecogs.com/png.latex?%7B%5Ccolor%7BGreen%7D%20b%3D1%7D).

