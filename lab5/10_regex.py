#Convert a given camel case string to snake case
import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.sub(pattern, '_', camel_str).lower()

# Test examples
print(camel_to_snake("helloWorldThisIsATest"))  # "hello_world_this_is_a_test"
