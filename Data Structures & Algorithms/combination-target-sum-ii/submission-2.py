class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.bt(candidates, target, 0, [], ans)
        u_ans = set()
        for l in ans:
            u_ans.add(tuple(l))

        return [list(s) for s in u_ans]



    def bt(self, candidates, remaining, start, cur_path, ans):    
        if remaining == 0:
            ans.append(cur_path[:])
            return

        if remaining < 0 or start >= len(candidates) or remaining < candidates[start]:
            return
    
        
        idx = start
        while idx < len(candidates):
            num = candidates[idx]
            if idx > start and  candidates[idx - 1] == candidates[idx]:
                idx += 1
                continue
        
            cur_path.append(num)
            self.bt(candidates, remaining - num, idx + 1, cur_path, ans)
            cur_path.pop()
            idx += 1



        