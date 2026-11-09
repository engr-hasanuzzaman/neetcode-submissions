class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        
        c_sum = 0
        l = 0
        ans = len(nums)
        for r in range(len(nums)):
            num = nums[r]
            c_sum += num
            while c_sum >= target:
                # print(c_sum, r, l)
                ans = min(ans, r - l + 1)
                c_sum -= nums[l]
                l += 1
        return ans
                
        