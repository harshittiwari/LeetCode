class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n < 1:
            return []
        li = [1]
        last = 1
        for _ in range(1,n):
            x = last * 10
            if x <= n:
                last = x
            else:
                if last == n:
                    last = last // 10
                last += 1
                while last % 10 == 0:
                    last = last // 10
            li.append(last)
        return li


sol = Solution()
print(sol.lexicalOrder(13))