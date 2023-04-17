n = int(input())
board = [[" " for _ in range(4 * n - 3)] for _ in range(4 * n - 3)]


def draw_star(n, x, y):
    if n == 1:
        board[y][x] = "*"
        return

    length = 4 * n - 3

    for i in range(length):
        board[y][x+i] = '*'
        board[y+i][x] = '*'
        board[y + length - 1][x+i] = "*"
        board[y+i][x + length - 1] = "*"

    draw_star(n-1, x+2, y+2)

draw_star(n, 0, 0)

for i in board:
    print(''.join(i))
