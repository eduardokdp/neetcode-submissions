class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = {}

        for strr in strs:
            frequency = [0] * 26

            for char in strr:
                frequency[ord(char) - ord("a")] += 1
            groups[tuple(frequency)].append(strr)
        return list(groups.values())
            
