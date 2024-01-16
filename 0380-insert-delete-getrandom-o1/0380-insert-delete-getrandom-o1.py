import random

class RandomizedSet:

    def __init__(self):
        self.d = defaultdict(int) # 紀錄[插入的數字,index]

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.d[val] = len(self.d)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.d:
            del self.d[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        if len(self.d) > 0:
            # print(self.d)
            index = random.randint(0 , len(self.d) - 1)
            # print(index)
            # print(list(self.d)[index])
            return list(self.d)[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()