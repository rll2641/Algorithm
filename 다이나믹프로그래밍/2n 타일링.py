'''
백준 1463번
https://www.acmicpc.net/problem/1463
'''

'''
점화식 존재 -> n = (n-1) + (n-2), 즉 1과2의 경우의 수가 3이상의 경우의 수를
모두 포함하고 있다.
'''

import sys
sys.setrecursionlimit(60000)

def Top_Down(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = (Top_Down(n-1) + Top_Down(n-2)) % 10007
        return dp[n]

n = int(input())
dp = [0] * (n + 1)
print(Top_Down(n))

'''
n = int(input())

result = 1
dp = [1] * (n + 1)

if n == 1:
    result = 1
else:
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    result = dp[n] % 10007

print(result)
'''