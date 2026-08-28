from collections import defaultdict
 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        arr_response = []


        for n in reversed(nums):
            num_count[n] += 1

        # Sort dictionary items by value (frequency) in descending order
        sorted_items = sorted(num_count.items(), key=lambda item: item[1], reverse=True)
        
        # Collect the first k keys from the sorted list
        for i in range(k):
            arr_response.append(sorted_items[i][0])

        return arr_response