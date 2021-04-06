# 사칙연산
def gyesan(root):
    # 자식노드가 없으면 연산이 필요 X
    if left[root] == 0 and right[root] == 0:
        return
    else:
        # 왼쪽, 오른쪽으로 내려가서 자식 노드 값을 확인 후
        gyesan(left[root])
        gyesan(right[root])
        # 사칙연산 시작
        if node[root] == '+':
            node[root] = node[left[root]] + node[right[root]]
        elif node[root] == '-':
            node[root] = node[left[root]] - node[right[root]]
        elif node[root] == '*':
            node[root] = node[left[root]] * node[right[root]]
        elif node[root] == '/':
            node[root] = node[left[root]] / node[right[root]]


for T in range(1, 11):
    N = int(input())
    node = [0] * (N+1)  # 노드 번호의 값
    left = [0] * (N+1)  # 왼쪽 자식 노드
    right = [0] * (N+1)  # 오른쪽 자식 노드
    for i in range(1, N+1):
        # 노드 정보 인풋
        info = list(map(str, input().split()))
        if len(info) > 2:  # info의 개수가 2개 이상이라면 자식 노드 정보가 있다는 뜻
            left[int(info[0])] = int(info[2])
            right[int(info[0])] = int(info[3])
        # 연산자가 아닐때는 정수로 넣기(현재 str)
        if info[1] != '+' and info[1] != '-' and info[1] != '*' and info[1] != '/':
            node[int(info[0])] = int(info[1])
        else:
            node[int(info[0])] = info[1]
    # print(left)
    # print(right)
    # print(node)
    root = 1
    gyesan(root)
    print("#{} {}".format(T, int(node[1])))
