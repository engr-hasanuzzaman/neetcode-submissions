class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.back_track(s, [], ans)
        return ans


    def is_palindrome(self, s):
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True


    def back_track(self, s, cur_path, ans):
        if len(s) == 0:
            return ans.append(cur_path[:])
        
        for l in range(1, len(s) + 1):
            if self.is_palindrome(s[:l]):
                cur_path.append(s[:l])
                self.back_track(s[l:], cur_path, ans)
                cur_path.pop()
        