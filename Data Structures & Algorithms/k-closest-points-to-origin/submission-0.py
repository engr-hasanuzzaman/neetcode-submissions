class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            dis = self.distance_from_origin(point)
            heapq.heappush(min_heap, (-dis, point))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        ans = []
        for _, p in min_heap:
            ans.append(p)
        return ans
        # return [_ p for _ in min_heap]


    def distance_from_origin(self, point):
        return math.sqrt((point[0] ** 2 + point[1] ** 2))
        