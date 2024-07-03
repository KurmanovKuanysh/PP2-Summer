# Convert snake case string to camel case string
import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Test examples
print(snake_to_camel("hello_world_this_is_a_test"))  # "helloWorldThisIsATest"
