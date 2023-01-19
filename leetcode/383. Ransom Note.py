class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for key in ransomNote:
            if key in dict:
                dict[key] -= 1
            else:
                dict[key] = -1
        for key in magazine:
            if key in dict:
                dict[key] += 1
            else:
                dict[key] = 1
        return len([k for k, v in dict.items() if v < 0]) == 0


if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    res = Solution().canConstruct(ransomNote, magazine)
    print(res)