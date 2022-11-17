'''
백준 1463번
https://www.acmicpc.net/problem/1463
'''
'''
    dp[i] 와 dp[i//3] + 1은 각각 i-1의 횟수와 i//3의 횟수를 비교하여
    최솟값을 찾아낸다. ex) i = 27 -> 7번 째 줄에 의해 dp[27] = dp[26]+1
    27에서 1을 뺀 26의 횟수dp[i]와 27에서 3을 나눈 횟수dp[i//3]의 횟수를
    비교하여 최솟값을 출력한다.
'''
N = int(input())
dp = [0] * (N + 1)

for i in range(2, N + 1): 
    
    dp[i] = dp[i-1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[N])