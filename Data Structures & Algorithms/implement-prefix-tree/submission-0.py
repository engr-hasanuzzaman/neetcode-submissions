from collections import defaultdict

class Node:
    def __init__(self, val, is_terminal=False):
        self.val = val
        self.neighbours = defaultdict(None)
        self.is_terminal = is_terminal


class PrefixTree:

    def __init__(self):
        self.head = Node("")

    def insert(self, word: str) -> None:
        cur_node = self.head
        for c in word:
            if c not in cur_node.neighbours:
                cur_node.neighbours[c] = Node(c)

            cur_node = cur_node.neighbours[c]
        cur_node.is_terminal = True


    def search(self, word: str) -> bool:
        cur_node = self.head
        for c in word:
            if c not in cur_node.neighbours:
                return False
            cur_node = cur_node.neighbours[c]
        
        return cur_node.is_terminal
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.head
        for c in prefix:
            if c not in cur_node.neighbours:
                return False
            cur_node = cur_node.neighbours[c]
        
        return True
        
        