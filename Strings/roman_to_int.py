class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        result = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "C":
                result += d[s[i]] * (-1 if result >= 500 else 1)
            elif s[i] == "X":
                result += d[s[i]] * (-1 if result >= 50 else 1)
            elif s[i] == "I":
                result += d[s[i]] * (-1 if result >= 5 else 1)
            else:
                result += d[s[i]]
        return result
            
