class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Rows
        for row in board:
            arr = [x for x in row if x != '.']
            if len(arr) != len(set(arr)):
                return False

    
        for col in range(9):
            arr = []
            for row in range(9):
                if board[row][col] != '.':
                    arr.append(board[row][col])

            if len(arr) != len(set(arr)):
                return False


        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                arr = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != '.':
                            arr.append(board[i][j])

                if len(arr) != len(set(arr)):
                    return False

        return True