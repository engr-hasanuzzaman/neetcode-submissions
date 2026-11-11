from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        memo = defaultdict(int)
        for num in nums:
            memo[num] += 1

        ans = set()
        for num in set(nums):
            memo[num] -= 1
            # complement = - num
            # print("current numbe is ", num)
            res = self.twoSum(nums, -num, memo)
            # print("n1, n2, n3", num, n1, n2)
            for n1, n2 in res:
                a = sorted([num, n1, n2])
                ans.add((a[0], a[1], a[2]))
            memo[num] += 1

        return list(ans)

    def twoSum(self, nums, target, memo):
        result = []
        for num in nums:
            rem = target - num
            if not memo[num] > 0:
                continue
            
            memo[num] -= 1

            if memo[rem] > 0:
                # print('found target ', target, num, rem)
                result.append([num, rem])
            memo[num] += 1
        return result

        