class solution:
    def isValidSudokuBoard(self, board):
        #Write your code here...
        #for row
        for row in board:
            seen=set()
            for num in row:
                if num in seen:
                    return False
                if num==".":
                    continue
                else:
                    seen.add(num)
        #for column
        for col in range(9):
            seen=set()
            for row in range(9):
                num=board[row][col]
                if num==".":
                    continue
                if num in seen:
                    return False
                else:
                    seen.add(num)
        return True