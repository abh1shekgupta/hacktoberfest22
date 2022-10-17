board = [[6, 0, 9, 0, 0, 0, 3, 0, 0],
         [5, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 8, 9, 0, 0, 0, 0],
         [0, 0, 0, 3, 5, 0, 0, 6, 0],
         [9, 5, 0, 6, 0, 8, 0, 3, 7],
         [0, 3, 0, 0, 4, 7, 0, 0, 0],
         [0, 0, 0, 0, 2, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 8, 0, 2],
         [0, 0, 3, 0, 0, 0, 9, 0, 4]]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if board[i][j] == 0:
                print("#", end=" ")
            else:
                print(board[i][j], end=" ")
        print()


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None


def check_postion(board, num, pos):
    """
    Returns True if position number is valid at the position
    pos should be row, col
    """
    # check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for j in range(len(board)):
        if board[j][pos[1]] == num and pos[0] != j:
            return False

    # check 3x3 box
    # box_x in loop
    box_y = (pos[0] // 3) * 3
    # max is in loop with box_x
    max_y = box_y + 3
    while box_y < max_y:
        box_x = (pos[1] // 3) * 3
        max_x = box_x + 3
        while box_x < max_x:
            if board[box_y][box_x] == num:
                return False
            box_x += 1
        box_y += 1

    return True


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if check_postion(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


print_board(board)
print()
solve(board)
print()
print_board(board)
