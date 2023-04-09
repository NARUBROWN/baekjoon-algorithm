board = int(input())
gameMap = [[0 for _ in range(board)] for _ in range(board)]
apple = int(input())
applePosition = []

for i in range(apple):
    applePosition.append(list(map(int, input().split())))
snakeTurn = int(input())

# 디렉토리 위치는 int로 변환해서 사용해야함
route = {}
for i in range(snakeTurn):
    route[i] = list(input().split())

snakeMaker = "-"
appleMaker = "*"

# 게임 시작 (뱀을 보드에 위치)
gameMap[0][0] = snakeMaker

# 사과를 맵에 위치
for i in range(len(applePosition)):
    A = int(str(applePosition[i])[1])
    B = int(str(applePosition[i])[4])
    gameMap[A][B] = appleMaker

snakeDi = {
    'current': [0, 0],
    'direction': "0"
}


def move(snake, time, direction):
    if direction == "D":
        print("")
    elif direction == "L":
        print("")
    else:
        for i in range(snake['current'][0], time):
            gameMap[0][i] = snakeMaker

def game():
    for i in route:
        # 1초마다 한칸 이동
        time = int(route[i][0])
        # 방향
        direction = route[i][1]
        # 이동
        move(snakeDi, time, direction)


game()

# 게임 보드 표시
for i in range(board):
    for j in range(board):
        print(gameMap[i][j], end="")
    print()
