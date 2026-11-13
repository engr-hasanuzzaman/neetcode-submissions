class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        res = 0
        for i in range(n):
            if i not in visited:
                self.dfs(adj, i, visited)
                res += 1
        
        return res
    
    def dfs(self, adj, idx, visited):
        if idx in visited:
            return
        
        visited.add(idx)
        for nei in adj[idx]:
            self.dfs(adj, nei, visited)
    
        