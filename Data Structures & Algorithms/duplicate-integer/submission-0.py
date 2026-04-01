class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checklist = dict()
        for num in nums:
            if num in checklist:
                return True
            checklist[num] = True
        return False
        
