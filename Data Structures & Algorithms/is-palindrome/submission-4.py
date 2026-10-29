class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if s == "":
            return False

        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        ri = len(s) - 1
        le = 0

        while le < ri:
            if s[le] == s[ri]:
                ri -= 1
                le += 1
            else:
                return False
        return True
            

