# Calculator
A scientific calculator using *appJar* for GUI and *math* library for calculations.

## Evaluating input
The biggest problem with this program is parsing the input. We need to check (efficiently) if what user put makes sense and calculate it, preferably in *O(n)* time.
To do that, we'll sort possible input values into 3 categories:
* **Number** (e.g. 0, 9)
* **Extra number** (e, π)
* **Operator** (e.g. %, +, sin)

Each category can be preceded and followed by one or more of the others. That splits input characters into even more groups:

|Group            | Allowed after        | Can be followed by   | Members                     |
| --------------- | -------------------- | -------------------- | --------------------------- |
|Number           | Number, Operator     | Number, Operator     | 0 .. 9                      |
|Extra number     | Operator             | Operator             | e, π                        |
|Prefix operator  | Number, Extra number | Operator             | x!, %, )                    |
|Postfix operator | Operator             | Number, Extra number | (, √, ln, log, sin, cos, tan|
|Double operator  | Number, Extra number | Number, Extra number | /, *, -, +, xⁿ, mod         |
|Dot operator     | Number               | Number               | .                           |

**Note:** Beginning and end of the equation counts as an operator.

## Parentheses
Another *problem* is handling parentheses. Parsing input left to right makes it a little easier. When we encounter a parenthesis, we call a processing function recurrently and use the result as part of the evaluated equation.
