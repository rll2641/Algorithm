'''
백준 1003번
https://www.acmicpc.net/problem/1003
'''
'''
0->10, 1->01, 2-> 11, 3->12, 4->23
n의 0, 1의 횟수는 각각 n-1의 1갯수, n의 1갯수와 같다. 
dp(n) = dp(n-1) + dp(n)
'''

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != 0:
        return dp[n]
    else:
        dp[n] = fibo(n-1) + fibo(n-2)
        return dp[n]

for _ in range(int(input())):
    
    N = int(input())
    dp = [0] * 41
    
    if N == 0:
        print('1 0')
    elif N == 1:
        print('0 1')
    else:
        print(f'{fibo(N-1)} {fibo(N)}')