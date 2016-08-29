class Directory:
    def __init__(self,name):
        self.Name = name
        self.Directories = []
        self.Files = []

    def __repr__(self, **kwargs):
        return self.Name
    
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        root = self.Parse(input)

        maxLen = self.FindMaxLen(root)
        return  maxLen - 1 if maxLen > 0 else maxLen

    def FindMaxLen(self,directory):
        maxLen = 0
        if len(directory.Files) > 0 or len(directory.Directories) > 0:
            for f in directory.Files:
                if len(f) > maxLen:
                    maxLen = len(f)
            for d in directory.Directories:
                x = self.FindMaxLen(d)
                if x > maxLen:
                    maxLen = x
            if maxLen > 0:
                maxLen += len(directory.Name) + 1
        return maxLen

    def Parse(self,input):
        root = Directory('')
        stack = [root]
        last = ''
        for ch in input:
            if ch == '\n':
                self.Add(last,stack[-1])
                last = ''
                stack = [root]
            elif ch == '\t':
                stack.append(stack[-1].Directories[-1])
            else:
                last += ch
        self.Add(last,stack[-1])
        return root

    def Add(self,last,current):
        if len(last) > 0:
            if '.' in last:
                current.Files.append(last)
            else:
                current.Directories.append(Directory(last))

sol = Solution()
print(sol.lengthLongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'))
print(sol.lengthLongestPath('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'))
print(sol.lengthLongestPath('tfile.ext'))
print(sol.lengthLongestPath(''))
print(sol.lengthLongestPath('dir'))