class Solution:
    def replaceSpace(self, s: str) -> str:
        # can't modify the str directly, it is defined in python
        ans = ""
        for i in s:
            if i == " ":
                i = "%20"
            ans += i
        return ans


# if this question is in C++, we could use the double pointer
# one is from the begin to the end, if space add two spacne
# one is from the end to begin if space, change to '0', '2', '%'

if __name__ == "__main__":
    s = Solution()
    test = "We are happy."
    print(s.replaceSpace(test))
