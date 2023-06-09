# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         for i in s:
#             if s.count(i) == 1:
#                 return i
#         return " "


# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         if not s:
#             return " "
#         # use the hash table to store the number of each character
#         d = {}
#         for i in s:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1

#         for i in s:
#             if d[i] == 1:
#                 return i
#         return " "


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]:
                return c
        return " "


# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         dic = collections.OrderedDict()
#         for c in s:
#             dic[c] = not c in dic
#         for k, v in dic.items():
#             if v: return k
#         return ' '

# this one does not work, it will fail because the odd number
# class Solution:
#     def firstUniqChar(self, s: str) -> str:
#         if not s:
#             return " "

#         unique = []
#         for i in s:
#             if i in unique:
#                 unique.remove(i)
#                 continue
#             if i not in unique:
#                 unique.append(i)
#         if not unique:
#             return " "
#         return unique[0]


if __name__ == "__main__":
    s = Solution()
    print(s.firstUniqChar("aadadaad"))
