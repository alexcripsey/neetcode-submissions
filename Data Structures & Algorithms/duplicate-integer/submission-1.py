from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = defaultdict(int)

        for n in nums:
            duplicate_map[n] += 1
            if duplicate_map[n] > 1:
                return True
        
        return False