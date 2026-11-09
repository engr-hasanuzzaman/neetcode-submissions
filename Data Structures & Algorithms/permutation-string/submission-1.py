
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if need == window:
            return True
        
        l = 0
        for r in range(n, len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            window[ord(s2[r]) -  ord('a')] += 1
            if need == window:
                return True
            l += 1
        return False

        