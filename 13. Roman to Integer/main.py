ROMANS = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}
        
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for ch in s[::-1]:
            if ch == "C":
                result += ROMANS[ch] * (-1 if result >= 500 else 1)
            elif ch == "X":
                result += ROMANS[ch] * (-1 if result >= 50 else 1)
            elif ch == "I":
                result += ROMANS[ch] * (-1 if result >= 5 else 1)
            else:
                result += ROMANS[ch]
        return result
            
