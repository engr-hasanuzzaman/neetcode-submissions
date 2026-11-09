import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [(p, s) for p, s in zip(position, speed)]
        comb.sort(reverse=True)
        # print(comb)
        stack = []
        for p, s in comb:
            # p, s = comb[i]
            step = (target - p)/s
            # print(p, s, step, stack)
            
            if not stack or stack[-1] < step:
                stack.append(step)

        return len(stack)
        