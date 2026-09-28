class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=[c.lower() for c in s if c.isalnum()]
        s_clean="".join(clean)
        return s_clean==s_clean[::-1]