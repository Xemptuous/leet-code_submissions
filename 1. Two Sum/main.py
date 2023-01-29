from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int):
    d = {v:i for i, v in enumerate(nums)}
    for i in range(len(nums)):
      diff = target-nums[i]
      if diff in d and d[diff] != i:
        return [i, d[diff]]
