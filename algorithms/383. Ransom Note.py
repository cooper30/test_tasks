"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        data = {}
        for c in magazine:
            if c in data:
                data[c] += 1
            else:
                data[c] = 1

        for c in ransomNote:
            if c in data and data[c] > 0:
                data[c] -= 1
            else:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    ransomNote = "aa"
    magazine = "ab"
    print(sol.canConstruct(ransomNote, magazine))
