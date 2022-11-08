'''
백준 9935번
https://www.acmicpc.net/problem/9935
'''

strs = input()
explostion = input()
explostion_len = len(explostion)
stack = []

for char in strs:
    
    stack.append(char)
    
    if len(strs) >= explostion_len:
        tmp = ''.join(stack[-explostion_len:])
        
        if tmp == explostion:
            i = 0
            
            while i < explostion_len:
                stack.pop()
                i += 1

if len(stack) == 0 :
    print('FRULA')
else:
    print(''.join(stack))
        