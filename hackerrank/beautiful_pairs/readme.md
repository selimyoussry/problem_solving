# hackerrank - Problem beautiful pairs
beautiful pairs - hackerrank

https://www.hackerrank.com/contests/101hack34/challenges/beautiful-path

You are given two arrays, AA and BB, both containing NN integers.

A pair of indices (i,j)(i,j) is beautiful if the ithith element of array AA is equal to the jthjth element of array BB. In other words, pair (i,j)(i,j) is beautiful if and only if Ai=BjAi=Bj.

Given AA and BB, there are kk pairs of beautiful indices (i0,j0),…,(ik−1,jk−1)(i0,j0),…,(ik−1,jk−1). A pair of indices in this set is pairwise disjoint if and only if for each 0≤x<y≤k−10≤x<y≤k−1 it holds that ix≠iyix≠iy and jx≠jyjx≠jy.

Change exactly 11 element in BB so that the resulting number of pairwise disjoint beautiful pairs is maximal, and print this maximal number to stdout.

Input Format

The first line contains a single integer, NN (the number of elements in AA and BB). 
The second line contains NN space-separated integers describing array AA. 
The third line contains NN space-separated integers describing array BB.

Constraints

1≤N≤1031≤N≤103
1≤Ai≤1031≤Ai≤103
1≤Bi≤1031≤Bi≤103
Output Format

Determine and print the maximum possible number of pairwise disjoint beautiful pairs.

Note: You must first change 11 element in BB, and your choice of element must be optimal.

Sample Input

3
1 2 2
1 2 3
Sample Output

3
Explanation

You can transform B2B2 from 33 to 22 and array BB becomes [1,2,2][1,2,2].

We now have: A=[1,2,2]A=[1,2,2] and B=[1,2,2]B=[1,2,2].

Of the 55 beautiful pairs, our pairwise disjoint beautiful pairs of indices are (0,0),(1,2),(2,1)(0,0),(1,2),(2,1).

An alternative choice would be (0,0)(0,0), (1,1)(1,1), and (2,2)(2,2).

Either solution yields 33 pairwise disjoint beautiful pairs, so we print 33.