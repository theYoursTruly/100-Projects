# Pi generator
There is a lot of different algorithms we can use to calculate π. From simple [Leibniz formula](https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80) to the fastest known [Chudnovsky algorithm](https://en.wikipedia.org/wiki/Chudnovsky_algorithm). We'll choose something that can make our calculations iterative and produce failry small numbers in each iteration.

We will use one of the fastest spigot algorithms - [Bailey–Borwein–Plouffe formula](https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula) which can calculate pi to a certain digit without a need to calculate all preceeding digits. This, in turn, makes it easy for a computer to do.

![Formula!](formula.png)

**Note:** This is very simple program and it doesn't use any external libraries to store or display π. Therefore, even if it's able to make calculations for a pretty much unlimited precision, it won't display anything past 50 characters.
