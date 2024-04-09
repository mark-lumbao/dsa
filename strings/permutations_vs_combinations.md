In Permutation order matters, while In Combination, id doesn't.

Example:

| ABC | CAB |

This meants there are 2 permutations, but there is only 1
considered combination.

nPR - for permutation

```
  n!
------
(n - r)!

```

nCR - for combination

```
  n!
------
(n - R)! R!

```

Reference:
https://www.youtube.com/watch?v=XJnIdRXUi7A

Problem:

1. Arrange 3 books in a shelf from a group of 7.

7P3

7! / (7 - 3)!

7x6x5x4x3x2x1 / 4x3x2x1

you can cancel 4x3x2x1 which leaves you with 7x6x5

which is equal to 210.

2. Arrange 5 books in a shelf.

5P5

5! / (5 - 5)!

5x4x3x2x1 / 1 (since 0! = 1)

= 120

3. Produce teams of 4 from a pool of 12 engineers.

nCR = 12C4

12! / (12 - 4)! x 12!
12! / 8! x 12!

12x11x10x9x8x7x6x5x4x3x2x1 / (8x7x6x5x4x3x2x1) x 4x3x2x1

479001600 / 40320 x 24
479001600 / 967680
= 495
