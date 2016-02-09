# misc - Problem 0a6c12bc-b8ab-4ee3-adef-e5ca18bfe20e
minimum steps to one

Problem Statement: On a positive integer, you can perform any one of the following 3 steps.

1. Subtract 1 from it. ( n = n - 1 ) 
2. If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
3. If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).

## Now the question is given a positive integer n, find the minimum number of steps that takes n to 1
eg:
1. For n = 1 , output: 0
2. For n = 4 , output: 2  ( 4  /2 = 2  /2 = 1 )
3. For n = 7 , output: 3  (  7  -1 = 6   /3 = 2   /2 = 1 )

## The recursive formula

Let's call f(n) the value of the minimal number of steps from n to 1.
From n we go to either m=n-1, n/2, n/3. At this step the minimal number of steps from m to 1 if f(m), and f(n)=f(m)+1.
So min(f(n)) = min(f(m)) + 1 = min(f(n-1), f(n/2), f(n/3)) + 1
