# cracking_coding - Problem 7ff93590-4c85-43f4-abd4-7d839c0c36ca
Found in cracking the coding interview, page 23

The problem is, find  all positive integer solution under 1,000 to a^3 + b^3 = c^3 + d^3.

# Notes

Note that if (a, b, c, d) is solution, then (b, a, c, d), (a, b, d, c), (b, a, d, c) are solutions too.
Also (a, a, a, a) is solution for every a, and there is no other solution possible if b=a, by strict monotony of all the
involved functions.