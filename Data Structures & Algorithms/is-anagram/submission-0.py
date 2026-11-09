from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charFreq = defaultdict(int)

        for idx in range(len(s)):
            charFreq[s[idx]] += 1
            charFreq[t[idx]] -= 1
        
        # print(charFreq)
        for  val in charFreq.values():
            if val != 0:
                return False
        
        return True
