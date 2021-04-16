# 전에 풀다가 포기했는데...일단은 시도는 했습니다...
# 다시 풀어보겠습니다... 일단 제출...!

for T in range(1, int(input())+1):
    # N : 세로, M : 가로
    N, M = map(int, input().split())
    pw_info = [list(map(str, input())) for _ in range(N)]
    result = []
    sixteen = []
    breaker = False  # 다중 for문을 빠져나오기 위한 변수 설정
    sixteen_num = []
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if pw_info[i][j] != '0':
                # 뒤에서부터 돌아서 0이 아닌 것을 만나면
                # for k in range(15):
                for z in range(j, j-15, -1):
                    sixteen.append(pw_info[i][z])
                # if len(sixteen_num) != 0 and len(sixteen_num) % 15 == 0:
                #     sixteen.append(sixteen_num)
                #     sixteen_num = []
                breaker = True
                break
        if breaker == True:
            break
    sixteen = sixteen[::-1]
    # print(sixteen)
    eng = ['A', 'B', 'C', 'D', 'E', 'F']
    alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = []
    final_ans = []
    # 16진수의 알파벳을 숫자로 바꾸기
    for i in range(len(sixteen)):
        if sixteen[i] not in eng:
            x = int(sixteen[i])
        else:
            x = alp[sixteen[i]]
        result.append(x)
    print("#{}".format(T), end=' ')
    # 2진수로 바꾸기
    for i in range(len(result)):
        binary = []
        k = result[i]
        while k > 0:
            div = k // 2
            mod = k % 2
            k = div
            binary.append(mod)
        ans = binary[::-1]
        # 4자리를 맞춰주기 위해 앞에 0 추가
        while len(ans) < 4:
            ans.insert(0, 0)
        for j in ans:
            final_ans.append(j)
    sixteen_final = []
    for i in final_ans:
        sixteen_final.append(i)
    print(*sixteen_final)


    #             # 거기부터 7개씩 끊어서 8번 저장
    #             for k in range(8):
    #                 ans = []
    #                 for z in range(j, j-7, -1):
    #                     ans.append(pw_info[i][z])
    #                 j = j-7
    #                 x = ans[::-1]  # 거꾸로 받아왔으니까 다시 뒤집어주기
    #                 result.append(''.join(x))  # 문자열로 저장
    #             breaker = True
    #             break
    #     if breaker == True:
    #         break
    # password = result[::-1]  # 뒤에서부터 받아와서 또 뒤집기
    # num = []
    # # # 암호코드로 변환
    # # for i in password:
    # #     if i in password_code:
    # #         num.append(password_code[i])
    # code = (num[0] + num[2] + num[4] + num[6]) * 3 + (num[1] + num[3] + num[5]) + num[7]
    # # 검증하기
    # if code % 10 == 0:
    #     print(sum(num), end='')
    # else:  # 검증 실패하면 0 출력
    #     print(0, end='')
    # print()