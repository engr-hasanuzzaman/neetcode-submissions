from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)                      # nodes are labelled 1..n
        graph = [[] for _ in range(n + 1)]  # 1 based index that's why n + 1
        degree = [0] * (n + 1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # The graph is connected, so no node has degree 0: start with the leaves
        queue = deque(i for i in range(1, n + 1) if degree[i] == 1)

        while queue:
            node = queue.popleft()
            degree[node] -= 1               # drops to 0 -> marked as removed
            for nxt in graph[node]:
                if degree[nxt] == 0:        # already removed
                    continue
                degree[nxt] -= 1
                if degree[nxt] == 1:        # just became a leaf, we will process only leafe , for indirected 1 means no cycle
                    queue.append(nxt)

        # Remaining nodes (degree > 0) are exactly the cycle
        for u, v in reversed(edges):
            if degree[u] > 0 and degree[v] > 0:
                return [u, v]