class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        for n in nums:
            if (n - 1) not in num_set:
                current_num = n
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                max_length = max(max_length, current_streak)

        return max_length