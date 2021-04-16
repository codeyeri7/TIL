def change_two(n):
    global two_ten, thr_ten
    # 10진수 계산을 위해 뒤집어준다
    re_two = two_bin[::-1]
    re_three = thr_bin[::-1]
    # 2진수의 n번째 자리가 0이면 1로 바꾸고
    if re_two[n] == 0:
        re_two[n] = 1
    # 1이면 0으로 바꿈
    else:
        re_two[n] = 0
    two_ten = 0  # 0으로 초기화
    # 2진수를 10진수로 바꾸기
    for i in range(len(re_two)):
        two_ten += (2 ** i) * re_two[i]
    # 3진수를 하나씩 바꾸며 비교
    for j in range(len(re_three)):
        if re_three[j] == 0:
            re_three[j] = 1
            thr_ten = 0  # 0으로 초기화
            # 3진수를 10진수로 바꾸고
            for k in range(len(re_three)):
                thr_ten += (3 ** k) * re_three[k]
            re_three[j] = 0  # 원상복귀
            # 2진수를 10진수로 바꾼거와 3진수를 10진수로 바꾼걸 비교
            if two_ten == thr_ten:
                # 만약 둘이 같다면 출력
                return two_ten
            else:
                thr_ten = 0
                re_three[j] = 2
                for k in range(len(re_three)):
                    thr_ten += (3 ** k) * re_three[k]
                re_three[j] = 0
                if two_ten == thr_ten:
                    return two_ten
        if re_three[j] == 1:
            re_three[j] = 2
            thr_ten = 0
            for k in range(len(re_three)):
                thr_ten += (3 ** k) * re_three[k]
            re_three[j] = 1
            if two_ten == thr_ten:
                return two_ten
            else:
                thr_ten = 0
                re_three[j] = 0
                for k in range(len(re_three)):
                    thr_ten += (3 ** k) * re_three[k]
                re_three[j] = 1
                if two_ten == thr_ten:
                    return two_ten
        if re_three[j] == 2:
            re_three[j] = 0
            thr_ten = 0
            for k in range(len(re_three)):
                thr_ten += (3 ** k) * re_three[k]
            re_three[j] = 2
            if two_ten == thr_ten:
                return two_ten
            else:
                thr_ten = 0
                re_three[j] = 1
                for k in range(len(re_three)):
                    thr_ten += (3 ** k) * re_three[k]
                re_three[j] = 2
                if two_ten == thr_ten:
                    return two_ten


for T in range(1, int(input())+1):
    # 2진수와 3진수 인풋
    two_bin = list(map(int, input()))
    thr_bin = list(map(int, input()))
    # 2진수와 3진수를 10진수로 바꾼 수
    thr_ten = 0
    two_ten = 0
    ans = 0
    # 2진수 자리수만큼 돌려서 함수 시작!
    for i in range(len(two_bin)):
        ans = change_two(i)
        # 만약 two_ten과 thr_ten이 같으면 반복문 종료 결과 도출!
        if two_ten == thr_ten:
            break
    print("#{} {}".format(T, ans))