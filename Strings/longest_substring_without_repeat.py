class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        result = 0
        i = 0
        j = 0
        while (j < len(s)):
            if s[j] not in d:
                d[s[j]] = i
            i = max(d[s[j]], i)
            result = max(result, j - i + 1)
            d[s[j]] = j + 1
            j += 1
        return result
