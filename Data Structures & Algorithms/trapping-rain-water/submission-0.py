class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,2,0,3,1,0,1,3,2,1]
        size = len(height)
        pref = [0] * size
        suf =  [0] * size

        c_pref = 0
        # [0,2,0,3,1,0,1,3,2,1]
        for i in range(size):
            pref[i] = c_pref
            c_pref = max(c_pref, height[i])
        
        # [0,0,2,2,1,0,1,3,2,1]
        c_suf = 0
        for r in range((size - 1),-1,-1):
            suf[r] = c_suf
            c_suf = max(c_suf, height[r])
        
        ans = 0
        for idx in range(size):
            contain = min(pref[idx], suf[idx]) - height[idx]
            if contain > 0:
                ans += contain
        return ans






'''
     [0,2,0,3,1,0,1,3,2,1]

prf: [0,0,2,2,3,3,3,3,3,3]
suf: [3,3,3,3,3,3,3,3,2,1]


w = min(p, s) - h[i]
'''
        