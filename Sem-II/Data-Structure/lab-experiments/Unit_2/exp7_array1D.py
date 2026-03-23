class Array1D:
    def __init__(self, size):
        self.arr = [None] * size
        self.n = 0

    def insert(self, index, val):
        if self.n >= len(self.arr):
            return "Overflow"
        # Shifting elements to the right: O(n)
        for i in range(self.n, index, -1):
            self.arr[i] = self.arr[i-1]
        self.arr[index] = val
        self.n += 1

    def delete(self, index):
        if index < 0 or index >= self.n:
            return "Index Out of Bounds"
        val = self.arr[index]
        # Shifting elements to the left: O(n)
        for i in range(index, self.n - 1):
            self.arr[i] = self.arr[i+1]
        self.arr[self.n - 1] = None
        self.n -= 1
        return val

    def display(self):
        print("Array:", self.arr[:self.n])

def main():
    arr = Array1D(10)
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)
    arr.display()
    arr.delete(1)
    arr.display()
    
if __name__ == "__main__":
    main()