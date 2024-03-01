from typing import List
#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = set()
        for num in nums:
            uniqueNums.add(num)
        nums[:]=sorted(uniqueNums)
        return len(nums)
# @lc code=end

solution = Solution()
nums = [1,1,2]
print(solution.removeDuplicates(nums))
print(nums)
nums = [-1,0,0,0,0,3,3]
print(solution.removeDuplicates(nums)) #[-1,0,3] Answer
print(nums)

# nums = uniqueNums changes what nums points to (it now points to a new object), while nums[:] modifies the contents of the original list object nums was referring to. This is why nums[:] affects the original list, but nums = uniqueNums does not.