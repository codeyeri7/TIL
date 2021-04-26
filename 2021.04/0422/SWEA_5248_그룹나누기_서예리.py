def find_m_team(idx):
    stack = []
    new_team = []
    # stack이 비워지면 끝
    while len(stack) >= 0:
        for i in range(N):
            # 시작점에서 인접한 노드를 찾아서 그 줄로 이동
            if arr[idx][i] == 1:
                stack.append(i)
                # 지나온 길은 0으로 표시
                arr[idx][i] = 0
                for j in range(len(team_result)):
                    # 나랑 짝궁인 번호가 이미 조에 있으면 나도 거기 추가
                    if idx in team_result[j]:
                        team_result[j].append(i)
        # 돌다가 스택이 없으면 나가기
        # 이거 없이 while len(stack) > 0을 하면 중간에 스택이 비워질 때가 있는데 그 때 멈춰버림
        if len(stack) == 0:
            break
        else:  # 아직 스택에 숫자가 남아있으면 빼서 그걸 idx로 바꾸기
            num = stack.pop()
        idx = num

for T in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_paper = list(map(int, input().split()))
    arr = [[0] * N for _ in range(N)]
    # 인접 행렬 만들기
    for i in range(len(num_paper)):
        if i % 2 == 0:
            arr[num_paper[i]-1][num_paper[i+1]-1] = 1
            arr[num_paper[i+1]-1][num_paper[i]-1] = 1
    team_result = []
    # arr를 돌면서 출발점 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                new_list = []
                new_list.append(i)
                team_result.append(new_list)
                find_m_team(i)
    # 단독으로 조를 구성할 사람 추가하기
    cnt = len(team_result)
    for i in range(N):
        imnothere = []
        for j in range(cnt):
            if i not in team_result[j]:
                imnothere.append(j)
        if len(imnothere) == cnt:
            new_list = []
            new_list.append(i)
            team_result.append(new_list)
    # 중복인 경우 제거
    for i in range(len(team_result)):
        team_result[i] = set(team_result[i])
    print("#{} {}".format(T, len(team_result)))
