class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.ds(0, nums, [], ans)
        return ans


    def ds(self, start, nums, cur_list, ans):
        ans.append(cur_list[:])

        while start < len(nums):
            cur_list.append(nums[start])
            self.ds(start+1, nums, cur_list, ans)
            cur_list.pop()
            start += 1

        

        
        