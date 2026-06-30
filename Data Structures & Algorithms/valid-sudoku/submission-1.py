class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            d1 = {}
            for j in range(9):
                if board[i][j] == '.':
                    continue
                
                elif board[i][j] not in d1:
                    d1[board[i][j]] = 1

                else:
                    return False
                    break
        


        transpose_board = list(map(list, zip(*board)))

        for i in range(9):
            d1 = {}
            for j in range(9):
                if transpose_board[i][j] == '.':
                    continue
                elif transpose_board[i][j] not in d1:
                    d1[transpose_board[i][j]] = 1

                else:
                    return False
                    break

        
        
        d1 = {}
        for i in range(9):
            for j in range(9):
                coordinate = i//3 , j//3
                value = board[i][j] 
                
                if coordinate not in d1:
                    d1[coordinate] = set()

                if value == '.':
                    continue

                elif value not in d1[coordinate]:
                    d1[coordinate].add(value)

                else:
                    return False
                    break
                
        
        
        return True

        


        