class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # coolDownTracker = collections.defaultdict(int)
        counter = collections.Counter(tasks)
        max_heap = [-val for val in counter.values()]
        heapq.heapify(max_heap)
        # hold already procesed (task, earliest time to pick)
        cooldown_queue = collections.deque([])
        time = 0
        # tasks=["A","A","A","B","C"]
        while max_heap or cooldown_queue:
            if not max_heap:
                time = cooldown_queue[0][1]
            else:
                # on heap we are storing neg value
                cnt = heapq.heappop(max_heap) + 1
                time += 1
                if cnt:
                    cooldown_queue.append((cnt, time + n))
            
                
            if cooldown_queue and cooldown_queue[0][1] == time:
                heapq.heappush(max_heap, cooldown_queue.popleft()[0])
        
        return time
        