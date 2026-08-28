import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_prefix = []
        arr_suffix = []
        arr_out = []
        cur_s = cur_p = 1


        for n in nums:
            cur_p *= n
            arr_prefix.append(cur_p)
        
        for n in reversed(nums):
            cur_s *= n
            arr_suffix.append(cur_s)
        arr_suffix.reverse()
        length = len(nums)

        for i in range(length):
            if i == 0:
                arr_out.append(arr_suffix[1])
            elif i == length - 1:
                arr_out.append(arr_prefix[length - 2])
            else:
                arr_out.append(arr_suffix[i+1] * arr_prefix[i-1])

        return arr_out