class Solution:
    def isValid(self, s: str) -> bool:
        p_map = {")": "(", "}": "{", "]": "["}
        open_b = ["(", "{", "["]

        stack = []

        for chr in s:
            if chr in open_b:
                stack.append(chr)
            else:
                if not stack or stack.pop() != p_map[chr]:
                    return False
        
        return not stack

        