for T in range(1, int(input())+1):
    ans = []
    N = float(input())
    a = 1  # a는 1이라고 가정
    print("#{}".format(T), end=' ')
    while a != 0:  # a는 0 밑의 소수부이니까 0이면 멈춤
        x = int(N * 2)  # 정수부를 저장
        a = (N * 2) - x
        N = a
        ans.append(x)
    if len(ans) > 12:  # 12자 이내는 출력, 아니면 overflow로 출력
        ans = 'overflow'
        print(ans, end='')
    else:
        for i in ans:
            print(i, end='')
    print()