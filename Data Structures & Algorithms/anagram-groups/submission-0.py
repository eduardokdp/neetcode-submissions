class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        groups = {}

        for strr in strs:
            frequency = [0] * 26

            for char in strr:
                pos = ord(char) - ord("a")
      

            groups[tuple(pos)].append(strr)
        return list(groups.values())
            
