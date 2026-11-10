class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # seen = set()
        # for n in nums:
        #     if n in seen:
        #         return n
            
        #     seen.add(n)

        nums.sort()
        for idx in range(1, len(nums)):
            if nums[idx] == nums[idx - 1]:
                return nums[idx]
        
        