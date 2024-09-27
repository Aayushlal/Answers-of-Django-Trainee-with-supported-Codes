
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

# input from the user is taken
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))

# Create an instance of Rectangle with user input
rect = Rectangle(length, width)

# Iterate over the instance and print the dimensions
for dimension in rect:
    print(dimension)

# Example output:
# Enter the length : 10
# Enter the width : 5
# {'length': 10}
# {'width': 5}
