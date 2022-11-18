'''
백준 11727번
https://www.acmicpc.net/problem/11727
'''

import sys
sys.setrecursionlimit(60000)

def Top_Down(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 3
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = (Top_Down(n-1) + (2 * Top_Down(n-2))) % 10007
        return dp[n]
    
n = int(input())
dp = [0] * (n + 1)
print(Top_Down(n))