from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dq = deque([])
        window = set()
        max_window = 0
        for chr in s:
            if chr not in window:
                window.add(chr)
                dq.append(chr)
                # print(dq)
                max_window = max(max_window, len(window))
            else:
                while True:
                    pc = dq.popleft()
                    window.remove(pc)
                    if pc == chr:
                        break
                window.add(chr)
                dq.append(chr)
            # right += 1
        return max_window