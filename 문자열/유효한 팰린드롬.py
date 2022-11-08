'''
파이썬 인터뷰
문자열이 팰린드롬이지 판별하는 문제
'''

import re

strs = re.sub('[^a-z]', '', input().lower())

if strs == strs[::-1]:
    print('yes')
else:
    print('no')