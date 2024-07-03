#Match a string that has an 'a' followed by anything, ending in 'b'
import re

def match_a_followed_by_anything_ending_in_b(s):
    pattern = r'a.*b'
    return re.fullmatch(pattern, s) is not None

# Test examples
print(match_a_followed_by_anything_ending_in_b("acb"))  # True
print(match_a_followed_by_anything_ending_in_b("ab"))   # True
print(match_a_followed_by_anything_ending_in_b("a_test_b")) # True
