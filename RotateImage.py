class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size // 2):
            for j in range(i,size - i-1):
                x = matrix[i][j]
                y = matrix[j][size - i - 1]
                z = matrix[size - i - 1][size - j - 1]
                w = matrix[size - j - 1][i]
                matrix[i][j] = w
                matrix[j][size - i - 1] = x
                matrix[size - i - 1][size - j - 1] = y
                matrix[size - j - 1][i] = z
                pass
       
A = [['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']]
Solution().rotate(A)
print(A)

A = [['00', '01', '02', '03'], ['10', '11', '12', '13'], ['20', '21', '22', '23'], ['30', '31', '32', '33']]
Solution().rotate(A)
print(A)

A= [['00', '01'], ['10', '11']]
Solution().rotate(A)
print(A)

A=[["00"]]
Solution().rotate(A)
print(A)

A=[[]]
Solution().rotate(A)
print(A)
