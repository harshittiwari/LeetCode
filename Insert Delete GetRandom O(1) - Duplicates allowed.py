from collections import defaultdict
import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.d = defaultdict(set)        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.vals.append(val)
        self.d[val].add(len(self.vals) - 1)
        return len(self.d[val]) == 1

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            indx = self.d[val].pop()
            if indx != len(self.vals) - 1:
                self.vals[indx] = self.vals[-1]            
                self.d[self.vals[-1]].remove(len(self.vals)-1)
                self.d[self.vals[-1]].add(indx)
            if len(self.d[val]) == 0:
                del self.d[val]
            self.vals.pop() 
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.vals[random.randint(0,len(self.vals)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
print(obj.insert(1))
print(obj.insert(1))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.getRandom())
print(obj.remove(1))
print(obj.getRandom())



rc = RandomizedCollection()
rc.insert(1)
rc.insert(0)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(1)
rc.insert(0)
rc.remove(0)
rc.remove(0)