# 중위순회
def inorder_traverse(root):
    if root != 0:
        inorder_traverse(L[root])
        visit.append(root)
        inorder_traverse(R[root])

for T in range(1, int(input())+1):
    N = int(input())
    visit = [0]
    L = [0] * (N+1)
    R = [0] * (N+1)
    node = []
    # 1은 루트노드이니까 제외하고, 2부터 N까지가 자식노드로 순서대로 번호가 지정되니까 2부터 N+1까지
    for i in range(2, N+1):
        # 완전이진트리 노드 저장
        node.append(i)
        # 왼쪽 자식 노드
        if L[i//2] == 0:
            L[i//2] = i
        # 오른쪽 자식 노드
        else:
            R[i//2] = i
    root = 1
    # 중위순회
    inorder_traverse(root)
    for i in range(len(visit)):
        # 이진 탐색 트리의 루트에 저장된 값
        if visit[i] == root:
            ans1 = i
        # N/2번 노드에 저장된 값
        if visit[i] == N//2:
            ans2 = i
    print("#{} {} {}".format(T, ans1, ans2))