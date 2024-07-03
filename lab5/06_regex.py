#Replace all occurrences of space, comma, or dot with a colon
import re

def replace_space_comma_dot_with_colon(s):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', s)

# Test examples
print(replace_space_comma_dot_with_colon("Hello, world. This is a test"))  # "Hello:world:This:is:a:test"
