class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str= ''
        for s in strs:
            length = len(s)
            encoded_str += str(length)
            encoded_str += "#"
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(i, j)
            size = int(s[i:j])
            i = j + 1
            j = i + size
            ans.append(s[i: j])
            i = j
            
        return ans

