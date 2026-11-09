from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                return [seen[rem], idx]
            seen[num] = idx
        
        