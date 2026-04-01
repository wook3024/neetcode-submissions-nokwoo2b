class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_len = len(nums)
        
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

        return curr_min

        