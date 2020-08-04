"""
Question: Symmetric Difference

Given 2 sets of integers,  M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  M or N  but do not exist in both.


Input Format:
The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.

Input 1
4
2 4 5 9
4
2 4 11 12

Output 1
5
9
11
12

"""

m = int(input())
M = list(map(int,input().split()))
n = int(input())
N = list(map(int,input().split()))

i = j = 0
M.sort()
N.sort()

while i < m and j < n:
  if M[i] < N[j]:
    print(M[i])
    i += 1
  elif M[i] > N[j]:
    print(N[j])
    j += 1
  else:
    i += 1
    j += 1

for k in range(i, m):
  print(M[k])
for k in range(j,n):
  print(N[k])
