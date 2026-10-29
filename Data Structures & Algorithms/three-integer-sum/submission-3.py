class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lists = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i - 1]:
                continue

            low = i + 1
            high = len(nums) - 1
            while low < high:
                target = nums[i] + nums[low] + nums[high]
                if target == 0:
                    lists.append([nums[i], nums[low], nums[high]])

                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif target < 0:
                    low += 1
                else:
                    high -= 1
        return lists
                            
        
        