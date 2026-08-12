# Last updated: 8/12/2026, 11:28:09 AM
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, identifier))

        # sort letter logs
        letter_logs.sort(key=lambda x: (x[0], x[1]))

        # rebuild
        return [f"{i} {r}" for r, i in letter_logs] + digit_logs