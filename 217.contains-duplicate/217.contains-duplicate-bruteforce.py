#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for indexNum1 in range(len(nums)):
            for indexNum2 in range(indexNum1+1,len(nums)):
                if indexNum1 != indexNum2:
                    if nums[indexNum1] == nums[indexNum2]:
                        return True
                    
        return False

# @lc code=end

