class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums[:k]
        heapq.heapify(self.min_heap)
        self.k = k

        for idx in range(k, len(nums)):
            num = nums[idx]
            self._add_to_heap(num)
        

    def add(self, val: int) -> int:
        self._add_to_heap(val)
        return self.min_heap[0]

    
    def _add_to_heap(self, val):
        print(self.min_heap, val)
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
            return
        
        if val > self.min_heap[0]:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)
        
