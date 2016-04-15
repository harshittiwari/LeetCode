class Solution(object):    
    def addParenthesis(self,k,l,r,s):
        if l == k and r == k:
            self.rs.append(s)
        elif l == k:
            self.addParenthesis(k,l,r + 1,s + ")")
        elif l < k:
            if r < l:
                self.addParenthesis(k,l,r + 1,s + ")")
            self.addParenthesis(k,l+1,r ,s + "(")

        pass

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rs = []
        self.addParenthesis(n,0,0,'')
        return self.rs
        

print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(4))
print(Solution().generateParenthesis(2))
print(Solution().generateParenthesis(1))
print(Solution().generateParenthesis(0))
print(Solution().generateParenthesis(-1))

#        global resultSet
#        resultSet = []
#        # this variable will be used to save all results (so far)
#        m = 2*n
#        def formParen(m, left, right, result):
#            # left is the # of left parenthesis so far
#            # right is the # of right parenthesis so far
#            # the rule, apparently, is that 
#            # (1) if left < m/2(which is n) and right == left, then we can only introduce a new left parenthesis
#            # (2) if left < m/2 and right < left, then we can introduce a new left paren, or a new right paren
#            # (3) if left >= m/2, then we cannot introduce any left parenthesis any more.
#            # (4) when left + right == m, we have form a complete parenthesis, we can append this result to 
#            # resultSet and move on.
#            if left + right == m: # (4)
#                global resultSet
#                resultSet.append(result)
#                return
#            if left < m/2 and right < left: # (1)
#                formParen(m, left + 1, right, result + '(')
#                formParen(m, left, right + 1, result + ')')
#            elif left < m/2 and left == right: # (2)
#                formParen(m, left + 1, right, result + '(')
#            else: # (3)
#                formParen(m, left, right + 1, result + ')')
#        formParen(m,0,0,'')
#        return resultSet