def hansu(n):
    # 한수 개수
    hansu_cnt = 0
    # 1부터 n까지에서 한수를 찾아보자
    for i in range(1, n+1):
        # 각 자리수 구하기
        n_list = list(map(int, str(i)))
        # 100보다 작으면 무조건 한수
        if i < 100:
            hansu_cnt += 1
        # 아니면 각 자리의 차가 같은 수만 찾자
        elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            hansu_cnt += 1
    return hansu_cnt  # 한수 개수 리턴

n = int(input())
ans = hansu(n)
print(ans)