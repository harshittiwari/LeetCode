class Solution(object):
    def __init__(self):
        self.opArr = ["-","+","*"]
        self.ch

    def addOps(self,num):
        if len(num) == 1:
            return {num:int(num)}
        if len(num) == 2:
            d = {}
            for op in self.opArr:
                x = num[0] + op + num[1]
                d[x] = [eval(x)]
            return d
        else:
            d = {}
            for i in range(1,len(num) - 1):
                x = self.addOps(num[:i])
                y = self.addOps(num[i:])
                for x1 in x:
                    for y1 in y:
                        for op in self.opArr:
                            v = x1 + op + y1
                            if v in d:
                                d[v].append(eval(v))
                            else:
                                d[v] = [eval(v)]
        return d

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ret = []
        d = self.addOps(num)
        for item in d:
            if target in d[item]:
                ret.append(item)
        return ret

print(Solution().addOperators("123", 6))
print(["1+2+3", "1*2*3"])
print("**")
print(Solution().addOperators("232", 8))
print(["2*3+2", "2+3*2"])
print("**")
print(Solution().addOperators("1234", 9191))
print(Solution().addOperators("12345", 9191))
print(Solution().addOperators("123456", 9191))
print(Solution().addOperators("3456237490", 9191))