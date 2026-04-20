class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_sanitized = "".join([i for i in s if i.isalnum()]).lower()
        n = len(s_sanitized)
        left = 0
        right = n - 1
        while left < right:
            if s_sanitized[left] == s_sanitized[right]:
                left += 1
                right -= 1
            else:
                return False
        return True