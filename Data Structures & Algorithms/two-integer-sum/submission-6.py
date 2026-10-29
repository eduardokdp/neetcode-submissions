class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
  

        hashm = {}
        n = 0

        for i in range(len(nums)):
            n = target - nums[i]
            if (n in hashm):
                return [hashm[n], i]
            hashm[nums[i]] = i
        return []
