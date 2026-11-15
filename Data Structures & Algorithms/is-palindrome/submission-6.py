class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "":
            return False

        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()

        right = len(s) -1
        left = 0


        while left < right:
            if s[left] == s[right]:
                right -= 1
                left += 1
            else:
                return False
        return True