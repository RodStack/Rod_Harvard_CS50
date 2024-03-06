class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Jar is full")
        self.size = self.size + n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar")
        else:
            self.size = self.size - n

    @property
    def capacity(self):
        return self._capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size cannot exceed capacity")
        self._size = size

def main():
    ...


if __name__ == "__main__":
    main()

