# Find the sequences of one uppercase letter followed by lowercase letters
import re

def find_uppercase_followed_by_lowercase(s):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, s)

# Test examples
print(find_uppercase_followed_by_lowercase("Hello World This Is A Test"))  # ['Hello', 'World', 'This', 'Test']
