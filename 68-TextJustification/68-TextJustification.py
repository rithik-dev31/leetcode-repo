# Last updated: 8/12/2026, 11:32:37 AM
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_words = []
            line_len = 0

            # pick words for current line
            while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
                line_words.append(words[i])
                line_len += len(words[i])
                i += 1

            # last line or single word line → left justify
            if i == n or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - line_len
                gaps = len(line_words) - 1
                space_each, extra = divmod(spaces, gaps)

                line = ""
                for j in range(gaps):
                    line += line_words[j]
                    line += " " * (space_each + (1 if j < extra else 0))
                line += line_words[-1]

            res.append(line)

        return res