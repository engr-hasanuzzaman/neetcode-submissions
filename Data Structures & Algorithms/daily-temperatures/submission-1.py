class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prev_warmer_day = []
        right = len(temperatures) - 1
        ans = [0] * len(temperatures)
        while right >= 0:
            cur_temp = temperatures[right]
            while prev_warmer_day and prev_warmer_day[-1][0] <= cur_temp:
                prev_warmer_day.pop()

            if prev_warmer_day:
                ans[right] = prev_warmer_day[-1][1] - right

            prev_warmer_day.append((cur_temp, right))
            right -= 1
        return ans
        