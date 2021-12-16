T = int(input())
for _ in range(T):
    quiz = list(map(str, input()))
    point_list = []
    point = 0
    for i in range(len(quiz)):
        # O가 나올 때 마다 1점씩 추가해서 저장하기
        if quiz[i] == "O":
            point += 1
            point_list.append(point)
        # X가 나오면 점수 초기화한 후 저장
        else:
            point = 0
            point_list.append(point)
    print(sum(point_list))