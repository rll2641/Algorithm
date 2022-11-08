'''
파이썬 인터뷰 
주어진 문자열 중 가장 비중이 큰 단어를 찾는 문제
'''

from collections import Counter
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ['ball']

paragraph_lst = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

cnt = Counter(paragraph_lst)
print(cnt.most_common()[0][0])