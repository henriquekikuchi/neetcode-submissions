class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity if capacity > 0 else 1 
        self.array = []
        self.items = 0
        self.last_index = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.items:
            self.resize()
        self.items += 1
        self.array.append(n)
        
    def popback(self) -> int:
        tmp = self.get(self.items - 1)
        self.set(self.items-1, None)
        self.items -= 1
        return tmp

    def resize(self) -> None:
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.items
    
    def getCapacity(self) -> int:
        return self.capacity