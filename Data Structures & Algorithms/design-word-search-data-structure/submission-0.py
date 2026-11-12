from collections import defaultdict

class Node:
    def __init__(self):
        self.children = defaultdict(None)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Node()
            cur_node = cur_node.children[c]
        cur_node.is_end = True
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        return self.searchInNode(word, cur_node)
        
    def searchInNode(self, word: str, cur_node) -> bool:
        for idx, c in enumerate(word):
            if c == '.':
                for node in cur_node.children.values():
                    is_present = self.searchInNode(word[idx+1:], node)
                    if is_present:
                        return True
                return False
            
            if c not in cur_node.children:
                return False
            cur_node = cur_node.children[c]
        
        return cur_node.is_end

            