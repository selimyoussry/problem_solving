# hackerrank - Problem minimum_penalty_path
minimum penalty path - hackerrank

https://www.hackerrank.com/contests/101hack34/challenges/beautiful-path

Consider an undirected graph containing NN nodes and MM edges. Each edge MiMi has an integer cost, CiCi, associated with it.

The penalty of a path is the bitwise OR of every edge cost in the path between a pair of nodes, AA and BB. In other words, if a path contains edges M1,M2,…,MkM1,M2,…,Mk, then the penalty for this path is C1C1 OR C2C2 OR ... OR CkCk.

Given a graph and two nodes, AA and BB, find the path between AA and BB having the minimal possible penalty and print its penalty; if no such path exists, print −1−1 to indicate that there is no path from AA to BB.

Note: Loops and multiple edges are allowed. The bitwise OR operation is known as or in Pascal and as | in C++ and Java.

Input Format

The first line contains two space-separated integers, NN (the number of nodes) and MM (the number of edges), respectively.

Each line ii of the MM subsequent lines contains three space-separated integers UiUi, ViVi, and CiCi, respectively, describing edge MiMi connecting the nodes UiUi and ViVi and its associated penalty (CiCi).

The last line contains two space-separated integers, AA (the starting node) and BB (the ending node), respectively.

Constraints

1≤N≤1031≤N≤103
1≤M≤1041≤M≤104
1≤Ci<10241≤Ci<1024
1≤Ui,Vi≤N1≤Ui,Vi≤N
1≤A,B≤N1≤A,B≤N
A≠BA≠B
Output Format

Print the minimal penalty for the optimal path from node AA to node BB; if no path exists from node AA to node BB, print −1−1.

Sample Input

3 4
1 2 1
1 2 1000
2 3 3
1 3 100
1 3
Sample Output

3
Explanation

The optimal path is 1→2→31→2→3. 
C(1,2)=1C(1,2)=1 and C(2,3)=3C(2,3)=3. 
The penalty for this path is: 11 OR 3=33=3, so we print 33.