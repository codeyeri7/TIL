# 직원 순서, 직원의 수, 고려한 탑의 높이, 안전높이, 아직 고려 안 한 탑 높이
def tower(i, n, s, b, rs):
    global min_s
    # 모든 직원을 다 고려한 경우
    if i == n:
        if s >= b:  # 다 고려한 탑의 높이가 B보다 크고
            if min_s > s:  # min_s 보다 작을 때
                min_s = s  # min_s 값 갱신
    # min_s가 s보다 작으면 다시 돌림
    elif min_s <= s:
        return
    # 탑에 불참한 사람이 많은 경우 이러한 결과가 나옴. 다시 돌리자.
    elif s + rs < b:
        return
    # 다 아닐 때 다음 사람을 고려해보자
    else:
        # s+tall[i] = 탑에 i번째 사람이 참여
        # rs-tall[i] = 아직 고려 안 한 탑 높이에서 참여한 i의 키가 빠짐
        tower(i+1, n, s+tall[i], b, rs-tall[i])
        # s = 탑에 i번째 사람 불참 그래서 높이는 그대로 감
        # rs-tall[i] = 참여하든 불참이든 고려 끝났으니 아직 고려 안 한 탑 높이에서는 빠진다.
        tower(i+1, n, s, b, rs-tall[i])


for T in range(1, int(input())+1):
    # N : 직원의 수, B : 안전한 탑의 높이
    N, B = map(int, input().split())
    # 직원들의 키
    tall = list(map(int, input().split()))
    tall_sum = sum(tall)
    min_s = 987654321  # B보다 큰 탑 중 최저높이의 탑
    # 직원 순서, 직원의 수, 고려한 탑의 높이, 안전높이, 아직 고려 안 한 탑 높이
    tower(0, N, 0, B, tall_sum)
    ans = min_s - B
    print("#{} {}".format(T, ans))

    # 부분집합으로 일일히 돌면서 구하기에는 시간이 너무 오래 걸리고 비효율적이다..
    # 런타임 에러가 뜬다. 앞으로는 위의 방법대로 하는 걸 더 연습하자.
    # total = []
    # # 부분집합 구하기
    # for i in range(1<<N):
    #     result = []
    #     for j in range(N):
    #         if i & (1<<j):
    #             result.append(j)
    #     total.append(result)

    # final_result = set()
    # min_result = 20000
    # # 부분집합을 바탕으로 직원들의 키의 합에서 빼면서 B보다 큰 수 중 가장 차이가 적은걸 구할 것.
    # for k in range(len(total)):
    #     tower = sum(tall)  # tower 초기화
    #     ans = 0
    #     for l in range(len(total[k])):
    #         # tower에서 직원들의 키를 돌아가면서 빼보기(부분집합이용)
    #         tower -= tall[total[k][l]]
    #         # if tower < B:
    #         #     break
    #     # 뺀 값이 B보다 큰 경우 중에서 B와의 차이를 구하자
    #     if tower >= B:
    #         ans = tower - B
    #         if ans < min_result:
    #             final_result.add(ans)
    #             min_result = ans
    #         # else:
    #
    # # 키의 합 전체에서 B와의 차이도 추가하자.
    # if sum(tall) >= B:
    #     ans = sum(tall) - B
    #     final_result.add(ans)
    # print(final_result)
    # print("#{} {}".format(T, min(final_result)))
