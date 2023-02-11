from typing import List
MAP = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}
class Solution:
    @staticmethod
    def letterCombinations(digits: str) -> List[str]:
        result = [i for i in MAP[digits[0]]] if len(digits) else []
        for digit in digits[1:]:
            result = [i + j for i in result for j in MAP[digit]]
        return result


def tests():
    tests = [
        ["23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]],
        ["", []],
        ["2", ['a','b', 'c']]
    ]
    for i, test in enumerate(tests):
        assert Solution().letterCombinations(test[0]) == test[1], \
            f"Test {i} Failed"
        print(f"Test {i} Passed")
tests()
