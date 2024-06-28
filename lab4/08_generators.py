#Generator to Yield the Square of All Numbers from (a) to (b)

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Example usage
a = 1
b = 5
for square in squares(a, b):
    print(square)
