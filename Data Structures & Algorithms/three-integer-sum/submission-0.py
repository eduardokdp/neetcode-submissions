class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        output = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+i, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tup = [nums[i], nums[j], nums[k]]
                        output.append(tuple(tup))
        return [list(i) for i in output]
