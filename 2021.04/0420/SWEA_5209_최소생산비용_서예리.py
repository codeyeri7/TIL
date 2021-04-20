def dfs(idx):
    global min_ans, ans
    # N번째 공장까지 다 가봤으면 최종 비용 저장
    if idx == N:
        # idx가 N이고, ans가 최소비용보다 작을 때에만!
        # 이걸 추가 안 했더니 값이 다르게 나왔음.
        if min_ans > ans:
            min_ans = ans
    # 지금까지 나온 최소비용보다 크다면 바로 돌려보내기
    if min_ans <= ans:
        return
    # 공장돌면서 비용 비교하기
    for i in range(N):
        if visit[i] == 0:  # 아직 방문 안 한 곳만 가기
            visit[i] = 1  # 방문체크
            ans += arr[idx][i]  # 비용 추가
            dfs(idx+1)  # 다음 줄로 이동
            visit[i] = 0  # 갔다왔으면 원상복구
            ans -= arr[idx][i]  # 추가했던 비용도 다시 빼기


for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N  # 방문체크용
    ans = 0
    min_ans = 987654321  # 최소비용 비교를 위한 값
    dfs(0)
    print("#{} {}".format(T, min_ans))
