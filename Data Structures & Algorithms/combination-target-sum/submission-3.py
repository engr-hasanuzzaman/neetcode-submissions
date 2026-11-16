class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        self.bt(nums, target, [], ans, 0)
        return ans


    def bt(self, nums, remaining, cur_path, ans, start):
        # print('cur_path, start, remaining', cur_path, start, remaining)
        if remaining == 0:
            # print
            # sorted_path = sorted(cur_path)
            ans.append(cur_path[:])
            return 
    
        if nums[start] > remaining:
            # print('---returning')
            return
        
        idx = start
        while idx < len(nums):
            num = nums[idx]
            if remaining < num:
                break
            cur_path.append(num)
            self.bt(nums, remaining - num, cur_path, ans, idx)
            cur_path.pop()
            idx += 1



        