class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = nums[0]
        while left <= right:
            if  nums[left] < nums[right]:
                res = min(res, nums[left])
                # if current window is sorted, left will contains the val
                break
            mid = left + (right - left) // 2
            res = min(res, nums[mid])
            # print('left, righ, mid ', left, right, mid, nums[mid])
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return res


        