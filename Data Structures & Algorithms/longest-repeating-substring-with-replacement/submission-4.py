from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fq = defaultdict(int)
        m_count = 0
        l = 0
        m_c = None
        res = 0
        for r in range(len(s)):
            fq[s[r]] += 1
            # adjust max count
            if fq[s[r]] > m_count:
                m_count = fq[s[r]]
                m_c = s[r]
            # m_count = max(, ])
            while r - l + 1 - max(fq.values()) > k:
                fq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res

            


        