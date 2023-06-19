# use two pointer
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # remove the space in the head and tail
        res = []
        # store the start and end index of one word
        i = j = len(s) - 1
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i + 1 : j + 1])
            # skip the space
            while s[i] == " ":
                i -= 1
            # new word
            j = i
        # transfer the list to string with space
        return " ".join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])


if __name__ == "__main__":
    test = Solution()
    s = "the sky is blue"
    print(test.reverseWords(s))
