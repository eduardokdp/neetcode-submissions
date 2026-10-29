class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        n = len(nums)

        output = [0] * n

        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                count *= nums[j]

            output[i] = count

        return output


