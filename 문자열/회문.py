'''
백준 17609번
https://www.acmicpc.net/problem/17609
'''

import sys

for _ in range(int(input())):
    
    strs = sys.stdin.readline().rstrip()
    
    # 회문 판별
    if strs == strs[::-1]:
        print('0')
        continue
    
    # 그 외
    left, right = 0, len(strs) - 1
    
    while left < right:
        
        if strs[left] == strs[right]:
            left += 1
            right -= 1
        else:
            # 왼쪽 문자 제거
            tmp = strs[:left] + strs[left+1:]
            if tmp == tmp[::-1]:
                print('1')
                break
            
            # 오른쪽 문자 제거
            tmp = strs[:right] + strs[right+1:]
            if tmp == tmp[::-1]:
                print('1')
                break
            
            print('2')
            break
        