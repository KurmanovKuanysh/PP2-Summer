#Split a string at uppercase letters
import re

def split_at_uppercase(s):
    pattern = r'[A-Z][a-z]*'
    return re.findall(pattern, s)

# Test examples
print(split_at_uppercase("HelloWorldThisIsATest"))  # ['Hello', 'World', 'This', 'Is', 'A', 'Test']
