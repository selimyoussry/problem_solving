# hackerrank - Problem beautiful_strings
beautiful strings - hackerrank

https://www.hackerrank.com/contests/101hack34/challenges/beautiful-string

You are given a string, SS, consisting of lowercase English letters.

A string is beautiful with respect to SS if it can be derived from SS by removing exactly 22 characters.

Find and print the number of different strings that are beautiful with respect to SS.

Input Format

A single string of lowercase English letters denoting SS.

Constraints

3≤|S|≤1063≤|S|≤106
3≤|S|≤203≤|S|≤20 holds for test cases worth at least 15%15% of the problem's score.
3≤|S|≤20003≤|S|≤2000 holds for test cases worth at least 30%30% of the problem's score.
Output Format

Print the number of different strings that are beautiful with respect to SS.

Sample Input

abba
Sample Output

4
Explanation

S={abba}S={abba}

The following strings can be derived by removing 22 characters from SS: ab,bb,ba,ab,ba,aa,and bbab,bb,ba,ab,ba,aa,and bb.

This gives us our set of unique beautiful strings, B={ab,ba,aa,bb}B={ab,ba,aa,bb}. As |B|=4|B|=4, we print 44.