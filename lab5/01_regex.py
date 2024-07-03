#Match a string that has an 'a' followed by zero or more 'b's
import re

def match_ab_zero_or_more_b(s):
    pattern = r'a*b*'
    return re.fullmatch(pattern, s) is not None

# Test examples
print(match_ab_zero_or_more_b("ab"))  # True
print(match_ab_zero_or_more_b("a"))   # True
print(match_ab_zero_or_more_b("b"))   # True
print(match_ab_zero_or_more_b("abb")) # True
print(match_ab_zero_or_more_b("ac"))  # False
