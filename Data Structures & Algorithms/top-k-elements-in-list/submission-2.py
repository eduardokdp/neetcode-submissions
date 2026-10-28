class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        most_frequent = {}
        for num in nums:
            most_frequent[num] = 1 + most_frequent.get(num, 0)

        arr = []

        for num, cnt in most_frequent.items():
            arr.append([cnt, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res