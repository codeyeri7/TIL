for T in range(1, int(input())+1):
    money = int(input())  # 거슬러 주어야 하는 돈
    # 돈의 종류
    every_money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []  # 결과값
    print("#{}".format(T))
    for i in range(len(every_money)):
        cnt = 0  # 종류별 돈의 개수
        # 거슬러주어야 하는 돈이 돈의 종류 i번째보다 작다면
        if every_money[i] <= money:
            # 거슬러주어야 하는 돈이 더 클 때까지 반복
            while money >= every_money[i]:
                # 돈의 종류 i번째를 계속 빼주기
                money = money - every_money[i]
                cnt += 1
            # 빼준 횟수만큼 result에 추가
            result.append(cnt)
        else:
            result.append(cnt)
    print(*result)