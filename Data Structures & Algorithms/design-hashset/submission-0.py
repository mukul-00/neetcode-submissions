# class MyHashSet:

#     def __init__(self):
#         self.res = []

#     def add(self, key: int) -> None:
#         if key not in self.res:
#             self.res.append(key)

#     def remove(self, key: int) -> None:
#         if key in self.res:
#             self.res.remove(key)

#     def contains(self, key: int) -> bool:
#         return key in self.res

#================= set ====================

class MyHashSet:

    def __init__(self):
        self.res = set()

    def add(self, key: int) -> None:
        self.res.add(key)

    def remove(self, key: int) -> None:
        self.res.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.res
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)