class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        ans = [""]
        for i in range(len(digits)):
            new_ans = []
            for p in ans:
                for s in mapping[digits[i]]:
                    new_ans.append(p + s)
            ans = new_ans
        
        return ans