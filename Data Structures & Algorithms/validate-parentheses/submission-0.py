class Solution:
    def isValid(self, s: str) -> bool:
        

        while ('()' or '{}' or '[]') in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')

        return s == ''