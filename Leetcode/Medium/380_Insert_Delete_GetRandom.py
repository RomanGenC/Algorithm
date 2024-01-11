import random


class RandomizedSet(object):
    def __init__(self):
        self.numbers = []
        self.index = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.numbers:
            return False
        self.numbers.append(val)
        self.index[val] = len(self.numbers) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.numbers:
            return False
        idx = self.index[val]
        last = self.numbers[-1]
        self.numbers[idx] = last
        self.index[last] = idx
        self.numbers.pop()
        del self.index[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numbers)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()