class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        arr = [ [] for _ in range(numRows) ]
        row = 0
        direction = -1

        for ch in s:
            arr[row].append(ch)
            if row == 0 or row == numRows - 1:
                direction *= -1
            row += direction
        return "".join([ch for r in arr for ch in r])
