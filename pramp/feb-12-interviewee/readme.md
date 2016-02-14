# pramp - Problem feb-12-interviewee
finding absent element

Given an array arr of n unique non-negative integers, how can you most efficiently find a non-negative integer that is not in the array?

Your solution should return such an integer or null if arr contains all possible integers.
Analyze the runtime and space complexity of your solution.

Hints & Tips
If your peer is stuck ask what do you both know about the numbers in arr. answer: non-negative unique integers and there are n such numbers. Then try to ask how can you find the n+1th number and so on

If it doesn't help ask if your peer about the pigeonhole principle and how can this be applied. If your peer is not familiar with it, this is the time to explain :)

We know that the second solution may seem easier, yet it worth understanding the first one and why it works. the pigeonhole principle is a simple yet powerful piece of logic.

If your peer is still stuck ask how can you use a hash function to find a number that is not in arr.

If all of it doesn't help, ask your peer what holds true about any group of n+1 unique numbers, relative to arr. (The answer: one of them is not in arr).

If you have time you can ask your peer how can you generate more numbers that are not in arr.
This can be done either by building arr2 as a longer array or by using the formula  j + m(n+1)  from the solution.

Solution
A naive solution is to randomize numbers. However, this is not a good approach: if n is very large we'll have to search the random numbers in that array many times.

Another simple solution is to keep record of the minimum/maximum while iterating over all numbers in arr and then produce numbers smaller/larger than all numbers in arr. However, this won't work if the minimum number is 0 and the maximum number is MAX_INT. Another iteration tactic is returning the sum of all numbers, but it won't work for the array [0, 3]. Also, returning the multiplication of all numbers in arr would not be correct if 0 is one of the numbers in arr.

There are 2 possible solutions:

1. Applying the pigeonhole principle and using a similar approach to hashing:
We create an array arr2 of length n+1. If we use a hash function to map every number from arr to an index of arr2 then from the pigeonhole principle at least one cell in arr2 will remain empty.
We can use a simple hash function like f(x) = x mod (n+1) for this mapping.
Then, for any index j of an empty cell of arr2 we can  guarantee that the integer j is not in arr.

Moreover, any result of j + m(n+1) for any integer m that is within the limits [0, MAX_INT] is a number that is not in arr (this is derived directly from mod definition).