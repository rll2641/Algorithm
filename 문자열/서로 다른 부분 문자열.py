'''
백준 11478번
https://www.acmicpc.net/problem/11478
'''

S = input()
set_str = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        set_str.add(S[i:j+1])

print(len(set_str))