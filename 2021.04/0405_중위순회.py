# 중위순회
def inorder_traverse(root):
    if arr[root] != 0:
        inorder_traverse(L[root])
        visit_in.append(arr[root])
        inorder_traverse(R[root])


for T in range(1, 11):
    # 정점의 수
    N = int(input())
    arr = [0] * (N+1)  # 트리
    L = [0] * (N+1)  # 왼쪽 자식 노드
    R = [0] * (N+1)  # 오른쪽 자식 노드
    visit_in = []  # 방문한 순서대로 나오도록
    print("#{}".format(T), end=' ')
    for i in range(1, N+1):
        # 정점 번호별 정보
        info = list(map(str, input().split()))
        # 자식 노드가 없는 경우~다 있는 경우
        if len(info) >= 2:
            arr[i] = info[1]
        # 왼쪽 자식 노드만 있는 경우
        if len(info) >= 3:
            L[i] = int(info[2])
        # 왼쪽, 오른쪽 자식 노드가 다 있는 경우
        if len(info) >= 4:
            R[i] = int(info[3])
    root = 1  # 루드 정점
    inorder_traverse(root)  # 중위순회
    for i in range(len(visit_in)):
        print(*visit_in[i], end='')
    print()
