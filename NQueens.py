class Solution(object):
    def PlaceQueenIn(self,matrix,sz,r):
        if r >= sz:
            return [matrix]
        s = []
        for j in range(0,sz):
            if self.IsValid(matrix,sz,r,j):
                matrix[r][j] = "Q"
                s = self.PlaceQueenIn(matrix,sz,r + 1)
                if len(s) > 0:
                    return s
                matrix[r][j] = "."
        return s


    def IsValid(self,matrix,sz,m,n):
        for i in range(sz):
            if matrix[i][n] == "Q":
                return False

        i = m
        j = n
        while i >= 0 and j >= 0:
            if matrix[i][j] == "Q":
                return False
            i-=1
            j-=1

        i = m
        j = n
        while i < sz and j >= 0:
            if matrix[i][j] == "Q":
                return False
            i+=1
            j-=1

        i = m
        j = n
        while i >= 0 and j < sz:
            if matrix[i][j] == "Q":
                return False
            i-=1
            j+=1

        i = m
        j = n
        while i < sz and j < sz:
            if matrix[i][j] == "Q":
                return False
            i+=1
            j+=1
        return True

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        solution = []
        if n == 1:
            return [["Q"]]
        for j in range(n):
            matrix = [["." for i in range(n)] for j in range(n)]
            matrix[0][j] = "Q"
            if j + 1 < n:
                s = self.PlaceQueenIn(matrix,n,1)
                if len(s) > 0:
                    li = [''.join(x) for x in matrix]
                    solution.append(li)
            matrix[0][j] = "."
        return solution

print(Solution().solveNQueens(-1))
print(Solution().solveNQueens(0))
print(Solution().solveNQueens(1))
print(Solution().solveNQueens(2))
print(Solution().solveNQueens(3))
print(Solution().solveNQueens(4))
