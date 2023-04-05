#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        return [
            i for i in range(len(s) - len(words) * len(words[0]) + 1)
            if Counter(
                s[j: j + len(words[0])]
                for j in range(i, i + len(words) * len(words[0]), len(words[0]))
            ) == Counter(words)
        ]
# @lc code=end
