# Last updated: 8/12/2026, 11:28:45 AM
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()

        built = set([""])
        ans = ""

        for word in words:
            if word[:-1] in built:
                built.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans