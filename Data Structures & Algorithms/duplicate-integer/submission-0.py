from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1
            if memo[num] > 1:
                return True
        
        return False