board = [
    [0,6,0,0,1,0,0,0,9],
    [0,1,0,0,0,0,7,0,0],
    [0,0,3,0,0,5,4,0,0],
    [0,0,0,9,0,7,1,0,0],
    [5,0,0,0,2,3,0,0,8],
    [1,0,0,0,0,0,0,0,3],
    [0,2,0,0,0,4,0,0,6],
    [0,0,0,5,8,0,0,0,0],
    [0,0,0,0,7,0,9,0,0]
]
def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i
        
            if solve(board):
                return True
            
            board[row][col] = 0

    return False

def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for x in range(len(board[0])):
            if x % 3 == 0 and x != 0:
                print(' | ', end='')
                
            if x == 8:
                print(board[i][x])
            else:
                print(str(board[i][x]) + ' ', end='')


def find_empty(board):
    for i in range(len(board)):
        for x in range(len(board[0])):
            if board[i][x] == 0:
                return (i, x)
    return None

def valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board[0])):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for x in range(box_x * 3, box_x * 3 + 3):
            if board[i][x] == num and (i, x) != pos:
                return False
    return True



print_board(board)
solve(board)
print("                                             ")
print_board(board)

