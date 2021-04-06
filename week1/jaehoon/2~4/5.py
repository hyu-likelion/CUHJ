import sys
input = sys.stdin.readline

class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, string):
        curr_node = self.head
        for c in string :
            if c not in curr_node.children :
                curr_node.children[c] = Node(c)
            curr_node = curr_node.children[c]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head
        for c in string :
            if c not in curr_node.children :
                return False
            curr_node = curr_node.children[c]
        
        if curr_node.data == None :
            return False
        else :
            return True
    
    def solution(self, string):
        curr_node = self.head
        for c in string :
            curr_node = curr_node.children[c]
        if curr_node.children :
            return True
        else :
            return False

def solution(phone_book):
    trie = Trie()
    for num in phone_book :
        trie.insert(num)

    flag = False
    for num in phone_book :
        flag = trie.solution(num)
        if flag == True :
            return False

    if flag == False :
        return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))