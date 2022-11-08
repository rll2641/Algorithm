'''
파이썬 인터뷰
주어진 문자열 안에 가장 긴 팰린드롬을 찾는 문제
'''

import re

strs = re.sub('[^\w]', '', input().lower())

def expand(left, right):
    while left >= 0 and right < len(strs) and strs[left] == strs[right]:
        left -= 1
        right += 1
    
    return strs[left+1:right]

if len(strs) < 2 and strs[::-1] == strs:
    print('yes')

result = ''

for i in range(len(strs) - 1):
    result = max(result,
                expand(i, i+1),
                expand(i, i+2),
                key=len)

print(result)