from typing import List
#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start

# Kians Solution

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         sortedNums = sorted(nums)

#         for index in range(len(sortedNums)-1):
#             if(sortedNums[index] == sortedNums[index+1]):
#                 return True
#         return False

# BRUTE FORCE (FAILED)

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         for numI in range(len(nums)):
#             for num2I in range(len(nums)):
#                 if numI != num2I:
#                     if nums[numI] == nums[num2I]:
#                         return True
#         return False
    
# Time Limit Exceeded
# 65/75 cases passed (N/A)
# Testcase
# [-24500,-24499,-24498,-24497,-24496,-24495,-24494,...29999]

# My Solution with dict. Could use set instead and would be slightly memory efficient.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount = {}

        for num in nums:
            if num in numCount:
                return True
            else:
                numCount[num]=1
        return False
    
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         numCount = set()
#         for num in nums:
#             if num in numCount:
#                 return True
#             else:
#                 numCount.add(num)
#         return False

# 1 liner solution w/ Set (Insane Big Brain)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)

# @lc code=end
solution = Solution()

print(solution.containsDuplicate([1,2,3,1]))
print(solution.containsDuplicate([1,2,3,4]))
print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))