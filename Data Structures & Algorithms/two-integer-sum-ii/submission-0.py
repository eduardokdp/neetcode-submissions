class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        n = len(numbers)
        high = n - 1
        low = 0


        while low < high:
            sums = numbers[low] + numbers[high]
            if sums == target:
                return [low + 1, high + 1]
            elif sums > target:
                high -= 1
            else:
                low += 1
        return [low + 1, high + 1]


