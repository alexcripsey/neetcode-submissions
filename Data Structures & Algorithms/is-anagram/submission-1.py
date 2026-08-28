from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = defaultdict(int)
        letter_comparison = defaultdict(int)

        if len(s) != len(t):
            return False

        else:
            for letter in s:
                letter_count[letter] += 1
        
            for letter in t:
                letter_comparison[letter] += 1

            for n in letter_count:
                if letter_count[n] != letter_comparison[n]:
                    return False
        
            return True