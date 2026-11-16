from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        print(freq)
        for k, v in freq.items():
            if v == 1:
                return k
        return 0
        
        