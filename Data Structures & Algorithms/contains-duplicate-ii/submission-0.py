from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for idx, num in enumerate(nums):
            if last_index.get(num, None) is not None:
                if (idx -  last_index.get(num)) <= k:
                    return True
            last_index[num] = idx
        
        return False

        