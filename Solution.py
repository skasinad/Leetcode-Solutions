class Solution(object):
    def isPalindrome(self, x):
        string_X = str(x)
        reversed_string_X = string_X[::-1]
        return reversed_string_X == string_X