class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i]:
                return True
        return False