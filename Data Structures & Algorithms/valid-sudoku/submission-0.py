class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    # Bruteforce
        # For Rows
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        # For Columns
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]=='.':
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])

        #For 3x3 boxes
        seen=set()
        for i in range(0,3):
            for j in range(0,3):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(0,3):
            for j in range(3,6):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(0,3):
            for j in range(6,9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(3,6):
            for j in range(0,3):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(6,9):
            for j in range(0,3):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        seen=set()
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in seen:
                    return False
                seen.add(board[i][j])

        return True




















                

        