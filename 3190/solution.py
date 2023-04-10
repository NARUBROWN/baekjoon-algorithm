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
snakeMakerUpDown = "|"
appleMaker = "*"

# 뱀은 매 초마다 이동함...
# 다시짜자...

# 게임 시작 (뱀을 보드에 위치)
gameMap[0][0] = snakeMaker

# 사과를 맵에 위치
for i in range(len(applePosition)):
    A = int(str(applePosition[i])[1])
    B = int(str(applePosition[i])[4])
    gameMap[A][B] = appleMaker

# 뱀 객체
snakeDi = {
    'current': [0, 0],
    'direction': "0"
}


# 뱀의 뱡항을 알아내고 그만큼 이동하는 함수
def snake_direction(snake, toward):
    try:
        # 뱀의 마지막 방향을 가져옴
        direction = snake['direction']
        # 뱀의 마지막 위치를 가져오기
        current = snake['current']
        # 뱀의 진로 방향을 알아내기

        # 뱀이 오른쪽으로 가고 있다면,
        if gameMap[current[0]][current[1]-1] == snakeMaker:
            # 방향 확인하기
            if direction[1] == "L":
                # 위로 이동
                # 맞는지 모르겠음
                for c in reversed(range(current[0], board - toward)):
                    print(c)
                    gameMap[c - 1][current[1]] = snakeMakerUpDown
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][0] -= 1
            elif direction[1] == "D":
                # 아래로 이동
                for c in range(current[0], toward):
                    gameMap[c+1][current[1]] = snakeMakerUpDown
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][0] += 1

        # 뱀이 아래를 향하고 있다면,
        elif gameMap[current[0]-1][current[1]] == snakeMaker:
            print("아래")
            # 아래로 이동
            # 방향을 가져오기
            if direction[1] == "L":
                # 오른쪽으로 이동
                for c in range(current[1], toward):
                    # 머리를 제외 해야하기 때문에 1을 더해줌
                    gameMap[current[0]][c + 1] = snakeMaker
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][1] += 1
            elif direction[1] == "D":
                # 왼쪽으로 이동
                # 리버스 들어간 애들 확인해야됨
                for c in reversed(range(current[1], board - toward)):
                    print(c)
                    # 머리를 제외 해야하기 때문에 1을 빼줌
                    gameMap[current[0]][c - 1] = snakeMaker
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][1] -= 1

        # 뱀이 위를 향하고 있다면
        elif gameMap[current[0]+1][current[1]] == snakeMaker:
            print("위")
            # 방향을 가져오기
            if direction[1] == "L":
                # 왼쪽으로 이동
                for c in reversed(range(current[1], board - toward)):
                    print(c)
                    # 머리를 제외 해야하기 때문에 1을 빼줌
                    gameMap[current[0]][c - 1] = snakeMaker
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][1] -= 1
            elif direction[1] == "D":
                # 오른쪽으로 이동
                for c in range(current[1], toward):
                    # 머리를 제외 해야하기 때문에 1을 더해줌
                    gameMap[current[0]][c + 1] = snakeMaker
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][1] += 1

        # 뱀이 왼쪽으로 가고 있다면,
        elif gameMap[current[0]][current[1]+1] == snakeMaker:
            print("<-")
            # 왼쪽으로 이동
            if direction[1] == "L":
                # 아래로 이동
                for c in range(current[0], toward):
                    gameMap[c + 1][current[1]] = snakeMakerUpDown
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][0] += 1
            elif direction[1] == "D":
                # 위로 이동
                # 맞는지 모르겠음
                for c in reversed(range(current[0], board - toward)):
                    print(c)
                    gameMap[c - 1][current[1]] = snakeMakerUpDown
                    # 이동할때마다 현재 위치 변경
                    snakeDi['current'][0] -= 1


        else:
            # 초기 방향
            # current 열 값부터 진로방향까지 +
            for i in range(current[1], toward):
                # 머리를 제외 해야하기 때문에 1을 더해줌
                gameMap[0][i+1] = snakeMaker
                # 이동할때마다 현재 위치 변경
                snakeDi['current'][1] += 1

    except IndexError:
        # error 발생시 게임오버
        return False

# 게임 진행 함수
def move(snake_route):
    # route 사전에 등록된 방향과 진로를 가지고 옴
    # 가지고 온 정보를 가지고 게임 진행
    for a in range(len(snake_route)):
        # 나아가야 할 칸의 개수
        toward = int(snake_route[a][0])

        try:
            snake_direction(snakeDi, toward)
            snakeDi['direction'] = snake_route[a]
        except False:
            break

move(route)

print(snakeDi)


# 게임 보드 표시
for i in range(board):
    for j in range(board):
        print(gameMap[i][j], end="")
    print()
