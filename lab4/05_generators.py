#Generator that Generates the Squares of Numbers up to N
def generate_squares(N):
    for i in range(N + 1):
        yield i * i

# Example usage
N = 10
for square in generate_squares(N):
    print(square)
