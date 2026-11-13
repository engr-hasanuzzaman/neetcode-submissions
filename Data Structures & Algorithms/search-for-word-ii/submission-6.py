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

# The idea is, instead of searching each word one by one which is time consuming
# we will build a trie with all the words then find all the prefix starteing from each position
# when new word found, add them to res
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
    
     
    # we will use board to explore neighbour
    # if same neighboure present in trie, worth exploring otherewise skip further seach
    # Just think, do we have any word with current prefix ? if yes: continue seach or drop search further
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

        