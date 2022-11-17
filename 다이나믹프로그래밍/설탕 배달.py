'''
백준 2839번
https://www.acmicpc.net/problem/2839
'''

N = int(input())
cnt = 0
while N > 0:
    
    if N % 5 == 0:
        cnt += N // 5
        N = 0
        break
    else:
        N -= 3
        cnt += 1

if N:
    print(-1)
else:
    print(cnt)