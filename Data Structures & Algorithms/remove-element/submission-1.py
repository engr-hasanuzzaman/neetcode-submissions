class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for c_idx in range(len(nums)):
            if nums[c_idx] != val:
                nums[left] = nums[c_idx]
                left += 1
        return left



        