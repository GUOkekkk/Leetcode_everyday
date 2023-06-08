class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n, len(s)):
            res.append(s[i])
        for i in range(n):
            res.append(s[i])

        # a shorter way
        # for i in range(n, n+len(s)):
        #    res.append(s[i % len(s)])

        # remember how to use the join
        return "".join(res)
