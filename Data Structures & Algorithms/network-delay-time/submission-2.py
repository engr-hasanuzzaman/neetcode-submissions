class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        distance = [float('inf') for _ in range(n+1)]
        distance[0] = 0
        m_heap = [(0, k)]
        # heapq.heappush()
        while m_heap:
            time, node = heapq.heappop(m_heap)
            if distance[node] <= time:
                continue

            distance[node] = time
            for nei, w in adj[node]:
                heapq.heappush(m_heap, (w + time, nei))
        
        # print(distance)
        m = max(distance)
        if m == float('inf'):
            return -1
        
        return m
        
            
        