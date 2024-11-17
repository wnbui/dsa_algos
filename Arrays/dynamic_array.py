class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    # Get value at i-th index
    def get(self, i: int) -> int:
        return self.array[i]

    # Set value at i-th index
    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    # Insert n in the last position of the array
    def pushback(self, n: int) -> None:
        # Check to see if array is at capacity
        if self.capacity == self.length:
            self.resize()
        # Insert element n at the next empty position
        self.array[self.length] = n
        self.length += 1

    # Remove the last element in the array
    def popback(self) -> None:
        if self.length > 0:
            self.length -= 1
        return self.array[self.length]

    # Create a new array of double capacity
    def resize(self) -> None:
        # Double the capacity of array
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        # Copy elements to new_array
        for i in range(self.length):
            new_array[i] = self.array[i]

        self.array = new_array

    # Get size of dynamic array
    def getSize(self) -> int:
        return self.length

    # Get capacity of dynamic array
    def getCapacity(self) -> int:
        return self.capacity

