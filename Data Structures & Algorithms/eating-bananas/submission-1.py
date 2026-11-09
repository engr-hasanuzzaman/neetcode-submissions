class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        def need_hours(rate):
            total = 0
            for p in piles:
                total += math.ceil(p / rate)
            return total
            

        m_rate = max(piles)
        left, right = 1, max(piles)
        rate = left + (right - left) // 2
        while left <= right:
            mid = left + (right - left) // 2
            n_total = need_hours(mid)

            if n_total <= h:
                m_rate = min(m_rate, mid)
                right = mid - 1
            elif n_total > h:
                left = mid + 1

            # if left >= right:
            #     break
        return m_rate
        