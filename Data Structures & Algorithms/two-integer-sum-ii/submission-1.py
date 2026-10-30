class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        n = len(numbers)
        high = n - 1
        low = 0

        while low < high:
            total = numbers[low] + numbers[high]

            if total == target:
                return [low + 1, high + 1]
            elif total > target:
                high -= 1
            else:
                low += 1

        return [low + 1, high + 1]

        
        