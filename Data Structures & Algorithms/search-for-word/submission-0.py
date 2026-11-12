class Node:
    def __init__(self):
        self.children = {}
        self.is_terminal = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word):
        cur_node = self.root

        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = Node()
            cur_node = cur_node.children[c]
        
        cur_node.is_terminal = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        trie = Trie()
        trie.add_word(word)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = self.dfs(board, r, c, trie.root)
                    if res:
                        return res
        return False

    
    def dfs(self, board, r, c, node):
        print()
        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == '_':
            return False

        if board[r][c] not in node.children:
            return False
        
        # if
        # 
        origina_word = board[r][c]
        board[r][c] = '_'
        cur_node = node.children[origina_word]
        if cur_node.is_terminal:
            return True
        res = (self.dfs(board, r, c + 1, cur_node) or
                self.dfs(board, r, c - 1, cur_node) or
                self.dfs(board, r + 1, c, cur_node) or
                self.dfs(board, r - 1, c, cur_node)
            )
        board[r][c] = origina_word
        return res
        

