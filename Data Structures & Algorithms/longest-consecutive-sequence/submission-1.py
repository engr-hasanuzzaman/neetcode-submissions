class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        visited = set()
        ans = 0
        for num in set(nums):
            if num in visited:
                continue
            cur_ans = 1
            while (num + 1) in seen:
                num += 1
                cur_ans += 1
                visited.add(num)
            ans = max(ans, cur_ans)
        return ans
                

        