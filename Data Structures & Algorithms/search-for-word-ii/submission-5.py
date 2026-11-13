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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        
        ans = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, r, c, "", trie.root, ans)
        
        return list(ans)
    
    # def isExist(self, board, word):
        
     
    def dfs(self, board, row, col, cur_word, node, ans):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "*":
            return

        c_chr = board[row][col]
        if c_chr not in node.children:
            return 
        
        cur_word += c_chr
        # terminal condition
        if node.children[c_chr].is_terminal:
            ans.add(cur_word)
        
        # mark visited
        board[row][col] = "*"
        new_node = node.children[c_chr]
        # visit all the neighbours
        self.dfs(board, row + 1, col, cur_word, new_node, ans)
        self.dfs(board, row - 1, col, cur_word, new_node, ans)
        self.dfs(board, row, col + 1, cur_word, new_node, ans)
        self.dfs(board, row, col - 1, cur_word, new_node, ans)
        board[row][col] = c_chr

        