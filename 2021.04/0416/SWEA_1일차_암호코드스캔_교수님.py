pattern = {(2, 1, 1): 0,
            (2, 2, 1): 1,
            (1, 2, 2): 2,
            (4, 1, 1): 3,
            (1, 3, 2): 4,
            (2, 3, 1): 5,
            (1, 1, 4): 6,
            (3, 1, 2): 7,
            (2, 1, 3): 8,
            (1, 1, 2): 9}

hexTobin = {'0': [0, 0, 0, 0], '1': [0, 0, 0, 1], '2': [0, 0, 1, 0], '3': [0, 0, 1, 1],
            '4': [0, 1, 0, 0], '5': [0, 1, 0, 1], '6': [0, 1, 1, 0], '7': [0, 1, 1, 1],
            '8': [1, 0, 0, 0], '9': [1, 0, 0, 1],
            'A': [1, 0, 1, 0], 'B': [1, 0, 1, 1],
            'C': [1, 1, 0, 0], 'D': [1, 1, 0, 1], 'E': [1, 1, 1, 0], 'F': [1, 1, 1, 1]}

def find():
    ans = 0
    for i in range(N):
        # j = M * 4 - 1 #4배로 늘림(이건 왜 있는건지 모르겠음..)
        idx = len(arr[i]) - 1
        while idx >= 55:  # 암호코드의 가로 길이가 무조건 55이상
            # 같은거 거르기 위해서
            # 현재 위치의 값이 1인데 그 윗줄이 0이다? == 얘는 처음 등장한 암호코드!
            if arr[i][idx] and arr[i - 1][idx] == 0:
                pwd = []  # 검증코드 저장
                for _ in range(8):  # 검증코드는 8개니까 8번 돌기
                    # 암호코드는 0, 1, 0, 1 순서로 되어있는데
                    # 맨 앞의 0 부분은 셀 필요가 없어서 c2, c3, c4만 카운트하자
                    c2 = c3 = c4 = 0
                    while arr[i][idx] == 0: idx -= 1
                    while arr[i][idx] == 1: c4, idx = c4 + 1, idx - 1
                    while arr[i][idx] == 0: c3, idx = c3 + 1, idx - 1
                    while arr[i][idx] == 1: c2, idx = c2 + 1, idx - 1
                    # 암호코드의 길이가 56보다 길면 7자리의 2진수의 n배의 길이로 나온다.
                    # 그걸 같은 비율로 값을 찾아줘야 한다.(pattern을 이용해서)
                    # 그래서 c2, c3, c4 중 가장 작은 값으로 나눠주면 같은 비율이 나와서
                    # pattern에서 찾을 수 있다.
                    MIN = min(c2, c3, c4)
                    pwd.append(pattern[(c2 // MIN, c3 // MIN, c4 // MIN)])

                # 검증코드 확인!
                b = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                a = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if (a * 3 + b) % 10 == 0:
                    ans += a + b
            idx -= 1
    return ans


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]
    for i in range(N):
        tmp = input()
        for j in range(M):
            # 16진수를 2진수로 다 바꿔서 넣기
            arr[i] += hexTobin[tmp[j]]
    print('#{} {}'.format(tc, find()))