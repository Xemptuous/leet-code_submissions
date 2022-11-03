class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.result = s[0]
        self.resLen = 0

        for i in range(len(s)):
            self.expandAroundCenter(s, i, i)
            self.expandAroundCenter(s, i, i + 1)

        return self.result

    def expandAroundCenter(self, s, L, R):
        while L >= 0 and R < len(s) and s[L] == s[R]:
            if R - L + 1 > self.resLen:
                self.result = s[L:R+1]
                self.resLen = R - L + 1
            L -= 1
            R += 1
