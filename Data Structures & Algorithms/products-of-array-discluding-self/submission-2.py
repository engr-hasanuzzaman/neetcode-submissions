class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums = [1,2,4,6] 
        prod_prefix = [1]
        idx = 1
        cur_prod = nums[0]
        while idx < len(nums):
            prod_prefix.append(cur_prod)
            cur_prod *= nums[idx]
            idx += 1

        # print(prod_prefix)
        postfix = 1
        idx = len(nums) - 1
        while idx >= 0:
            prod_prefix[idx] *= postfix
            postfix  *= nums[idx]
            idx -= 1
        return prod_prefix
        