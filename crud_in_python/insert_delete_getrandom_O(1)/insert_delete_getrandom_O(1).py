# slow version written without help, 100% by me
import random

class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        else:
            self.s.remove(val)
            return True

    def getRandom(self) -> int:
        x = random.randint(0, len(self.s) - 1)
        y = list(self.s)
        return y[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# O(1) version 
import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.arr[-1]

        self.arr[idx] = last
        self.pos[last] = idx

        self.arr.pop()
        del self.pos[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
    
# my version of O(1)

import random

class RandomizedSet:

    def __init__(self):
        self.store = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val not in self.indices:
            self.store.append(val)
            self.indices[val] = len(self.store) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            # locate index of element to be removed
            remove_index = self.indices[val]
            # determine last value of list
            last_value = self.store[-1]
            # set to be removed element as last element
            self.store[remove_index] = last_value
            # fix dict index tracking
            self.indices[last_value] = remove_index
            # remove last element
            self.store.pop()
            # delete removed value from dict
            self.indices.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        x = random.randint(0, len(self.store) - 1)
        return self.store[x]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()