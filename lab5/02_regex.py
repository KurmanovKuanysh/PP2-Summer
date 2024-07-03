#Match a string that has an 'a' followed by two to three 'b's
import re

def match_a_followed_by_2_to_3_b(s):
    pattern = r'ab{2,3}'
    return re.fullmatch(pattern, s) is not None

# Test examples
print(match_a_followed_by_2_to_3_b("abb"))  # True
print(match_a_followed_by_2_to_3_b("abbb")) # True
print(match_a_followed_by_2_to_3_b("abbbb")) # False
