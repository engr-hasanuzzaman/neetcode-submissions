from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = []
        graph = defaultdict(list)
        dep_arr = [0] * numCourses
        for c, dc in prerequisites:
            graph[dc].append(c)
            dep_arr[c] += 1
        
        for c, dependency in enumerate(dep_arr):
            if not dependency:
                queue.append(c)

        print('---intial courses without any dep', queue)
        if not queue:
            return False

        while queue:
            c = queue.pop()
            for sc in graph[c]:
                dep_arr[sc] -= 1
                if dep_arr[sc] == 0:
                    queue.append(sc)
        
        for d in dep_arr:
            if d != 0:
                return False
        
        return True

        