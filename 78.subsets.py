from typing import List
#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset=[]
        def subIn(numsIter):
            if (numsIter == len(nums)):
                result.append(subset[:])
                return
            subIn(numsIter+1)
            subset.append(nums[numsIter])
            subIn(numsIter+1)
            subset.pop()
        subIn(0)
        return result

        
# @lc code=end

print(Solution().subsets([1,2,3]))