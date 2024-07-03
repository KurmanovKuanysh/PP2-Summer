#Insert spaces between words starting with capital letters
import re

def insert_spaces_between_capital_words(s):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, ' ', s)

# Test examples
print(insert_spaces_between_capital_words("HelloWorldThisIsATest"))  # "Hello World This Is A Test"
