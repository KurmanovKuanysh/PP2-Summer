#Find sequences of lowercase letters joined with an underscore
import re

def find_lowercase_sequences_with_underscore(s):
    pattern = r'[a-z]+_[a-z]+'
    return re.findall(pattern, s)

# Test examples
print(find_lowercase_sequences_with_underscore("hello_world this_is_a_test"))  # ['hello_world', 'this_is', 'a_test']
