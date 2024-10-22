#Task 3

class myList:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def get(self, index):
        if index >= 0 and index < len(self.items):
            return self.items[index]
        else:
            return Nonie

    def __str__(self):
        return str(self.items)

myList = myList()
myList.add(137)
myList.add(28)
print(myList.get(0))
myList.remove(28)
print(str(myList))
