# 행, 열, 이동횟수, 빈 문자열
def seven_numbers(r, c, cnt, output):
    # 동서남북
    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    # 들어온 값 먼저 추가
    output += arr[r][c]
    if cnt == 6:  # 이동횟수가 6이라면 result set에 추가
        result.add(int(output))
    else:
        for a in range(4):
            nr = r + dr[a]
            nc = c + dc[a]
            # 범위 내에서 돌기
            if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                continue
            seven_numbers(nr, nc, cnt+1, output)


for T in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    # 중복을 거르기 위해서 set을 사용
    result = set()
    for i in range(4):
        for j in range(4):
            cnt = 0  # 이동 횟수 카운트
            output = ''  # 빈 문자열
            seven_numbers(i, j, cnt, output)
    print("#{} {}".format(T, len(result)))