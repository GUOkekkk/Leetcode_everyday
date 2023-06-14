# how to solve it in DP
# but it could be solved by sliding window/ two pointers
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}  # store the last apperance of the character
        res = tmp = 0  # use the res to store the max length to save the space
        for j in range(len(s)):
            i = dic.get(s[j], -1)  # get the last apperance of the character
            dic[s[j]] = j  # update the hash table
            # the state transfer function(key part of the DP)
            tmp = tmp + 1 if tmp < j - i else j - i  # dp[j - 1] -> dp[j]
            res = max(res, tmp)  # update the res
        return res
