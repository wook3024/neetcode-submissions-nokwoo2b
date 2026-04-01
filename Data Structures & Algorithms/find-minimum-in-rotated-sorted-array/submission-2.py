class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_len = len(nums)
        curr_idx = nums_len // 2
        curr_min = 10**1000
        
        def is_in_range(idx):
            nonlocal nums_len
            if idx < 0:
                return False
            if idx >= nums_len:
                return False
            return True

        if nums[0] < nums[-1]:
            curr_idx = 0
            curr_min = nums[0]
            while curr_idx + 1 < nums_len:
                if nums[curr_idx + 1] < nums[curr_idx]:
                    curr_min = nums[curr_idx + 1]
                    curr_idx -= 1
                else:
                    return curr_min
        else:
            curr_idx = nums_len - 1
            curr_min = nums[-1]
            while curr_idx - 1 >= 0:
                if nums[curr_idx - 1] < nums[curr_idx]:
                    curr_min = nums[curr_idx - 1]
                    curr_idx -= 1
                else:
                    return curr_min

        # while True:
        #     print(curr_idx)
        #     if curr_min > nums[curr_idx]:
        #         curr_min = nums[curr_idx]
        #         half_size = curr_idx // 2 if curr_idx > 1 else 1
        #         upper_val = 10**1000
        #         lower_val = 10**1000

        #         if is_in_range(curr_idx + half_size):
        #             upper_val = nums[curr_idx + half_size]
                
        #         if is_in_range(curr_idx - half_size):
        #             lower_val = nums[curr_idx - half_size]

        #         if curr_min <= min(upper_val, lower_val) or (upper_val > 1000 and lower_val > 1000):
        #             print("break1", curr_idx, half_size)
        #             break
        #         else:
        #             if upper_val < lower_val:
        #                 curr_idx = curr_idx + half_size
        #             else:
        #                 curr_idx = curr_idx - half_size

        #     else:
        #         print("break2", curr_idx)
        #         break
        
        return curr_min

        