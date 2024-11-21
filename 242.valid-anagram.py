#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict={}
        tDict={}
        if len(s) != len(s):
            return False
        for char in s:
            if char in sDict:
                sDict[char]+=1
            else:
                sDict[char]=1
        for char in t:
            if char in tDict:
                tDict[char]+=1
            else:
                tDict[char]=1

        return sDict == tDict

# @lc code=end

