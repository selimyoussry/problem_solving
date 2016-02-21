# hackerrank - Problem kings_and_four_sons
kings and four sons - hackerrank

https://www.hackerrank.com/contests/101hack34/challenges/happy-king

The King of Byteland wants to grow his territory by conquering KK other countries. To prepare his 44 heirs for the future, he decides they must work together to capture each country.

The King has an army, AA, of NN battalions; the ithith battalion has AiAi soldiers. For each battle, the heirs get a detachment of soldiers to share but will fight amongst themselves and lose the battle if they don't each command the same number of soldiers (i.e.: the detachment must be divisible by 44). If given a detachment of size 00, the heirs will fight alone without any help.

The battalions chosen for battle must be selected in the following way:

A subsequence of KK battalions must be selected (from the NN battalions in army AA).
The jthjth battle will have a squad of soldiers from the jthjth selected battalion such that its size is divisible by 44.
The soldiers within a battalion have unique strengths. For a battalion of size 55, the detachment of soldiers {0,1,2,3}{0,1,2,3} is different from the detachment of soldiers {0,1,2,4}{0,1,2,4}
The King tasks you with finding the number of ways of selecting KK detachments of battalions to capture KK countries using the criterion above. As this number may be quite large, print the answer modulo 109+7109+7.

Input Format

The first line contains two space-separated integers, NN (the number of battalions in the King's army) and KK (the number of countries to conquer), respectively.

The second line contains NN space-separated integers describing the King's army, AA, where the ithith integer denotes the number of soldiers in the ithith battalion (AiAi).

Constraints

1≤N≤1041≤N≤104
1≤K≤min(100,N)1≤K≤min(100,N)
1≤Ai≤1091≤Ai≤109
1≤Ai≤1031≤Ai≤103 holds for test cases worth at least 30%30% of the problem's score.
Output Format

Print the number of ways of selecting the KK detachments of battalions modulo 109+7109+7.

Sample Input

3 2
3 4 5
Sample Output

20
Explanation

First, we must find the ways of selecting 22 of the army's 33 battalions; then we must find all the ways of selecting detachments for each choice of battalion.

Battalions {A0,A1}{A0,A1}: 
A0A0 has 33 soldiers, so the only option is an empty detachment ({}{}). 
A1A1 has 44 soldiers, giving us 22 detachment options ({}{} and {0,1,2,3}{0,1,2,3}). 
So for this subset of battalions, we get 1×2=21×2=2 possible detachments.

Battalions {A0,A2}{A0,A2}: 
A0A0 has 33 soldiers, so the only option is an empty detachment ({}{}). 
A2A2 has 55 soldiers, giving us 66 detachment options ({}{}, {0,1,2,3}{0,1,2,3}, {0,1,2,4}{0,1,2,4}, {1,2,3,4}{1,2,3,4}, {0,1,3,4}{0,1,3,4}, {0,2,3,4}{0,2,3,4}). So for this subset of battalions, we get 1×6=61×6=6 possible detachments.

Battalions {A1,A2}{A1,A2}: 
A1A1 has 44 soldiers, giving us 22 detachment options ({}{} and {0,1,2,3}{0,1,2,3}). 
A2A2 has 55 soldiers, giving us 66 detachment options ({}{}, {0,1,2,3}{0,1,2,3}, {0,1,2,4}{0,1,2,4}, {1,2,3,4}{1,2,3,4}, {0,1,3,4}{0,1,3,4}, {0,2,3,4}{0,2,3,4}). 
So for this subset of battalions, we get 2×6=122×6=12 possible detachments.

In total, we have 2+6+12=202+6+12=20 ways to choose detachments, so we print 20 % (109+7)20 % (109+7), which is 2020.

