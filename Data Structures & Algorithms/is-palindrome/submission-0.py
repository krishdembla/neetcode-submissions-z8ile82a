class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped = ''
        for ch in s:
            if ch.isalnum():
                stripped += ch.lower()
        return stripped == stripped[::-1]

        