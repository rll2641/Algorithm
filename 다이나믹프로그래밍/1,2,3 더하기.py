'''
백준 9095번 
https://www.acmicpc.net/problem/9095
'''

# 점화식 존재, n > 3일 때, f(n) = f(n-1) + f(n-2) + f(n-3)
def Top_Down(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 4
    elif dp[x] != 0:
        return dp[x]
    else:
        dp[x] = Top_Down(x - 1) + Top_Down(x - 2) + Top_Down(x - 3)
        return dp[x]
    
for _ in range(int(input())):
    
    n = int(input())
    dp = [0] * (n + 1)
    print(Top_Down(n))