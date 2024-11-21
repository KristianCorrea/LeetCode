#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = set()
        for num in nums:
            if num in numDict:
                return True
            numDict.add(num)
        return False
                
# @lc code=end

