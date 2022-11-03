from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      slist = []
      nums1.reverse()
      nums2.reverse()
      while nums1 and nums2:
        if nums1[-1] < nums2[-1]:
          slist.append(nums1.pop())
        else:
          slist.append(nums2.pop())
      nums1.reverse()
      nums2.reverse()
      slist += nums1
      slist += nums2
      sl = len(slist)
      mid = sl // 2
      if sl % 2:
        return slist[mid]
      else:
        return (slist[mid-1] + slist[mid]) / 2
          
