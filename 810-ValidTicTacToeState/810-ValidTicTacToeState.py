# Last updated: 8/12/2026, 11:28:33 AM
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        flat = "".join(board)

        x_count = flat.count("X")
        o_count = flat.count("O")

        def win(p):
            b = board
            # rows
            for i in range(3):
                if b[i][0] == b[i][1] == b[i][2] == p:
                    return True
            # cols
            for j in range(3):
                if b[0][j] == b[1][j] == b[2][j] == p:
                    return True
            # diagonals
            if b[0][0] == b[1][1] == b[2][2] == p:
                return True
            if b[0][2] == b[1][1] == b[2][0] == p:
                return True
            return False

        x_win = win("X")
        o_win = win("O")

        # rule 1: turn order
        if not (x_count == o_count or x_count == o_count + 1):
            return False

        # rule 2: both cannot win
        if x_win and o_win:
            return False

        # rule 3: win must match turn count
        if x_win and x_count != o_count + 1:
            return False

        if o_win and x_count != o_count:
            return False

        return True