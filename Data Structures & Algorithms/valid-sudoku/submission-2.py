class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        boxes = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == ".":
                    continue

                coordinate = (i//3 , j//3)
                if coordinate not in boxes:
                    boxes[coordinate] = set()

                if (val in rows[i]) or (val in col[j]) or (val in boxes[coordinate]):
                    return False

            

                rows[i].add(val)
                col[j].add(val)
                boxes[coordinate].add(val)

        return True
