class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = []
        graph = defaultdict(list)
        dep_arr = [0] * numCourses
        for c, dc in prerequisites:
            graph[dc].append(c)
            dep_arr[c] += 1
        
        for c, dependency in enumerate(dep_arr):
            if not dependency:
                queue.append(c)
    
        ans = []
        # num_of_course_taken = 0
        while queue:
            c = queue.pop()
            ans.append(c)
            for sc in graph[c]:
                dep_arr[sc] -= 1
                if dep_arr[sc] == 0:
                    queue.append(sc)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []
        