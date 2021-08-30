def DFS(r, c):
    global house_cnt
    # 4방향
    d_r = [-1, 0, 1, 0]
    d_c = [0, 1, 0, -1]
    # 방문한 집은 0으로 바꿔놓기
    danji[r][c] = 0
    # 집 하나 갈 때마다 카운트
    house_cnt += 1

    # 4방향이니까 4번 반복
    for i in range(4):
        # 앞으로 우리가 가야할 위치
        temp_r = r + d_r[i]
        temp_c = c + d_c[i]
        # 범위를 벗어나면 방향 바꿔서 다시 탐색하자
        if temp_r < 0 or temp_r >= N or temp_c < 0 or temp_c >= N or danji[temp_r][temp_c] == 0:
            continue
        # 범위 내라면 재귀
        DFS(temp_r, temp_c)

# 단지 개수 인풋
N = int(input())
# 단지 정보 인풋
danji = [list(map(int, input())) for _ in range(N)]
danji_cnt = 0  # 단지 개수 카운트
house = []  # 집 개수 담기

for i in range(N):
    for j in range(N):
        # 집이 있다면
        if danji[i][j] == 1:
            # 집의 개수 0으로 초기 설정
            house_cnt = 0
            # 단지 개수 추가
            danji_cnt += 1
            DFS(i, j)
            # 그렇게해서 나온 집의 개수를 저장
            house.append(house_cnt)
print(danji_cnt)  # 단지 개수 출력
house.sort()  # 오름차순으로 정렬해야 해서 sort
for i in range(danji_cnt):
    print(house[i])  # 집 개수 출력