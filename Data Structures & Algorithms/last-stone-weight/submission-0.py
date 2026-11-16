class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-num for num in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            b1, b2 = -heapq.heappop(max_heap), -heapq.heappop(max_heap)
            new_stone = b1 - b2
            heapq.heappush(max_heap, -new_stone)
        
        return -max_heap[0]
        