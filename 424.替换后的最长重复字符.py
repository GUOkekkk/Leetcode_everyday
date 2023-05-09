#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#

# @lc code=start

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        num = [0] * 26 # store the number of each character in the slide window string
        n = len(s) # length of string
        maxn = left = right = 0

        while right < n:
            num[ord(s[right]) - ord("A")] += 1
            maxn = max(maxn, num[ord(s[right]) - ord("A")])

            # do the replace operation
            if right - left + 1 - maxn > k: # if the number of characters to be replaced is greater than k, move left pointer
                num[ord(s[left]) - ord("A")] -= 1
                left += 1
            right += 1

        return right - left
# @lc code=end
