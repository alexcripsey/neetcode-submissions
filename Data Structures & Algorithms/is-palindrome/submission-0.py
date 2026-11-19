import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        if (s_clean == s_clean[::-1]):
            return True
        else:
            return False
