#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSeen={}
        for i in range(len(nums)):
            difference=target-nums[i]
            if difference in numsSeen:
                return [i, numsSeen[difference]]
            else:
                numsSeen[nums[i]]=i

            
        
# @lc code=end

