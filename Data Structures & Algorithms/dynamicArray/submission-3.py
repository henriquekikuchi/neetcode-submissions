class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity if capacity > 0 else 1 
        self.array = [0] * self.capacity
        self.items = 0

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.items:
            self.resize()
        self.array[self.items] = n
        self.items += 1
        
    def popback(self) -> int:
        tmp = self.array[self.items-1]
        self.items -= 1
        return tmp

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        new_arr = [0] * self.capacity

        for i in range(0, self.items):
            new_arr[i] = self.array[i]

        self.array = new_arr

    def getSize(self) -> int:
        return self.items
    
    def getCapacity(self) -> int:
        return self.capacity