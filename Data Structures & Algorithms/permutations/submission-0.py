class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.bt(nums, [], ans, len(nums))
        return ans

    
    def bt(self, nums, cur_path, ans, size):
        # print(cur_path, len(cur_path), len(nums))
        if size == len(cur_path):
            # print('resoult found ')
            ans.append(cur_path[:])
            return

        for idx in range(len(nums)):
            cur_path.append(nums[idx])
            self.bt(nums[:idx] + nums[idx+1:], cur_path, ans, size)
            cur_path.pop()
        