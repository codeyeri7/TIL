for T in range(1, int(input())+1):
    # N : 세로, M : 가로
    N, M = map(int, input().split())
    pw_info = [list(map(str, input())) for _ in range(N)]
    result = []
    # 암호코드 정보를 딕셔너리로 만들기
    password_code = {'0001101' : 0, '0011001': 1, '0010011': 2, '0111101' : 3, '0100011' : 4, '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
    print("#{}".format(T), end=' ')
    breaker = False  # 다중 for문을 빠져나오기 위한 변수 설정
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if pw_info[i][j] == '1':
                # 뒤에서부터 돌아서 1을 만나면
                # 거기부터 7개씩 끊어서 8번 저장
                for k in range(8):
                    ans = []
                    for z in range(j, j-7, -1):
                        ans.append(pw_info[i][z])
                    j = j-7
                    x = ans[::-1]  # 거꾸로 받아왔으니까 다시 뒤집어주기
                    result.append(''.join(x))  # 문자열로 저장
                breaker = True
                break
        if breaker == True:
            break
    password = result[::-1]  # 뒤에서부터 받아와서 또 뒤집기
    num = []
    # 암호코드로 변환
    for i in password:
        if i in password_code:
            num.append(password_code[i])
    code = (num[0] + num[2] + num[4] + num[6]) * 3 + (num[1] + num[3] + num[5]) + num[7]
    # 검증하기
    if code % 10 == 0:
        print(sum(num), end='')
    else:  # 검증 실패하면 0 출력
        print(0, end='')
    print()