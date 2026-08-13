class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            seen = set()
            left = 0
            max_len = 0

            for right in range(len(s)):
                # shrink from the left until s[right] is no longer a duplicate
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                max_len = max(max_len, right - left + 1)

            return max_len