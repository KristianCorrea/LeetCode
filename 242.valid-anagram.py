#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        if len(t) != len(s):
            return False

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

            # if s[i] in s_count.keys():
            #     s_count[s[i]]+=1
            # else:
            #     s_count[s[i]]=1

            # if t[i] in t_count.keys():
            #     t_count[t[i]]+=1
            # else:
            #     t_count[t[i]]=1
        return s_count == t_count

# @lc code=end

