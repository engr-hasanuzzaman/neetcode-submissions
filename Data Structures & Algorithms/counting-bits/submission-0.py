class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            ans.append(self.count_one(num))
        return ans


    def count_one(self, n):
        res = 0

        while n > 0:
            res += 1
            n = n & (n-1)
        return res
        