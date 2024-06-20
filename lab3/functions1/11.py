def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
# Check if a word or phrase is a palindrome