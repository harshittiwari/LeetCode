from heapq import heappush
from heapq import heappop

class Solution(object):
    def getSkyline(self, bl):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        sl = []
        live = []
        i = 0
        size = len(bl)
        while i < size or live:
            if (not live) or (i < size and bl[i][0] <= -live[0][1]):
                x = bl[i][0]
                while i < size and bl[i][0] == x:
                    heappush(live,(-bl[i][2],-bl[i][1]))
                    i += 1
            else:
                x = -live[0][1]
                while live and x >= -live[0][1]:
                    heappop(live)
            if not sl or (live and -live[0][0] != sl[-1][1]):
                sl.append([x,-live[0][0]])
            if not live:
                sl.append([x,0])

            pass
        return sl
        
print(Solution().getSkyline([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print([[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
print("*****")
print(Solution().getSkyline([[1,2,1],[1,2,2],[1,2,3]]))
print([[1,3],[2,0]])
print("*****")