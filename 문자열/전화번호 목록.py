'''
백준 5052번
https://www.acmicpc.net/problem/5052
'''

'''
시간초과
class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            
            curr_node = curr_node.children[char]
            
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            curr_node = curr_node.children[char]
            
        if curr_node.children:
            return False
        else:
            return True
     
t = int(input())

for _ in range(t):
    
    n = int(input())
    
    Tr = Trie()
    numbers = []
    
    for _ in range(n):
        number = input()
        Tr.insert(number)
        numbers.append(number)
            
    numbers.sort()
    
    bool = True
    
    for i in numbers:
        if not Tr.search(i):
            bool = False
            break
    
    if bool:
        print('YES')
    else:
        print('NO')
'''

import sys

class Node:
    def __init__(self, key, data = None):
        self.key = key
        self.data = data
        self.children = {}

class Trie:
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        curr_node = self.head
        
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
            
        curr_node.data = string
    
    def search(self, string):
        curr_node = self.head
        
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            
                if curr_node.data is not None:
                    return True
            else:
                Tr.insert(string)
                return False
            
        return True      

for _ in range(int(input())):
    
    Tr = Trie()
    is_consistency = True
    
    for _ in range(int(input())):
        number = sys.stdin.readline().rstrip()
        
        if not is_consistency:
            continue
        
        if Tr.search(number):
            print('NO')
            is_consistency = False
    
    if is_consistency:
        print('YES')
        