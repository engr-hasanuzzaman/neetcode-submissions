from collections import defaultdict

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq_count = defaultdict(int)
        for num in nums:
            freq_count[num] += 1
        
        idx = 0
        for num in range(3):
            for _ in range(freq_count[num]):
                nums[idx] = num
                idx += 1
        