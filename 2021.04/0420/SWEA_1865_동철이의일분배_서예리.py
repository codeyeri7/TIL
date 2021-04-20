def dfs(idx):
    global max_ans, ans
    if idx == N:  # idx와 N이 같다면
        if max_ans < ans:  # ans가 max_ans보다 클 때(최대값을 구해야하니)
            max_ans = ans  # 최종 값을 max_ans로 갱신!
            return
    if max_ans > ans:  # ans가 최대값보다 작으면 다시 돌아가
        return
    if idx < N:
        for i in range(N):
            if visit[i] == 0:  # 아직 방문하지 않은 곳만
                # zero division 에러가 떴다.
                # 확률이 0인 것을 곱해주면 ans가 0이 되는데
                # 이걸 밑에서 arr[idx][i]로 나누려니까 0을 나눌 수 없다며 에러가 뜸.
                # 그래서 arr[idx][i]가 0이 아닐때만 돌도록 바꿔줌.
                if arr[idx][i] != 0:
                    visit[i] = 1  # 방문체크
                    ans *= arr[idx][i]  # 확률값 추가
                    dfs(idx+1)  # 다음 줄 돌기!
                    visit[i] = 0  # 돌고 왔으면 다시 원상복구
                    ans /= arr[idx][i]  # 값도 다시 빼주기


for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N  # 방문체크
    ans = 1  # 확률
    max_ans = -1  # 최대값을 구하기 위한 값
    for i in range(N):
        for j in range(N):
            arr[i][j] = round(arr[i][j] * 0.01, 2)
    dfs(0)  # dfs로 돌기!
    print('#{}'.format(T), end=' ')
    # 소수점 6째자리까지 나오기 위
    print('{:.6f}'.format(float(max_ans*100)))
