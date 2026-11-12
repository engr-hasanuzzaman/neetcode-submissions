
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}
        ans = []
        self.back_track(s, [], ans, memo)
        return ans


    def is_palindrome(self, s, memo):
        if s in memo:
            return memo[s]
    
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                memo[s] = False
                return memo[s]
            left += 1
            right -= 1
        
        memo[s] = True
        return memo[s]


    def back_track(self, s, cur_path, ans, memo):
        if len(s) == 0:
            return ans.append(cur_path[:])
        
        for l in range(1, len(s) + 1):
            c_s = s[:l]
            if self.is_palindrome(c_s, memo):
                cur_path.append(c_s)
                self.back_track(s[l:], cur_path, ans, memo)
                cur_path.pop()
        