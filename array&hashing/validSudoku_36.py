class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for row in board] #  9
        cols = [set() for col in board] #  9
        boxes = [set() for box in board] # 9

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False
                    box_num = (i // 3) + (j // 3) * 3
                    if board[i][j] in boxes[[i, j]]:
                        return False
                    
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[box_num].add(board[i][j])
        return True