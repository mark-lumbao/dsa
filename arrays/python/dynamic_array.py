# Reference: https://www.geeksforgeeks.org/how-do-dynamic-arrays-work/
class DynamicArray:
    elements = [0]
    size = 0  # capacity
    length = 0

    def __init__(self, elements=[]):
        self.elements = elements
        self.length = len(elements)
        self.size = len(elements)

    def to_string(self):
        count = 0
        to_show = ""
        while count < self.length:
            if count == 0:
                to_show = f"[{self.elements[count]}"
            else:
                to_show = f"{to_show}, {self.elements[count]}"
            count += 1
        to_show = f"{to_show}]"
        return to_show

    def append(self, item):
        if self.size == self.length:
            self.grow()
        self.elements[self.length] = item
        self.length += 1

    # TODO: Not done yet
    def insert(self, index, item):
        if index > self.size:
            raise IndexError("No more space!")
        if self.size == self.length:
            self.grow()
        self.elements[index] = item
        self.length += 1

    def grow(self):
        self.size = 1 if self.size == 0 else self.size * 2
        temp = [0] * self.size
        count = 0
        for i in self.elements:
            temp[count] = i
            count += 1
        self.elements = temp
