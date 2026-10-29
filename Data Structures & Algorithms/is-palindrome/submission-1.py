class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return False

        s = bool(re.match(r"^[a-zA-Z0-9]+$", s))
        
        strr = ''
        for char in s:
            strr += char.lower()
        return strr == strr[::-1]