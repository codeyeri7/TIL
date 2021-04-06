# 전위순회
def preorder_traverse(root):
    if root != 0:
        visit.append(root)
        preorder_traverse(left[root])
        preorder_traverse(right[root])


for T in range(1, int(input())+1):
    # N : 노드의 개수, M : 리프 노드의 개수, L : 출력할 노드 번호
    N, M, L = map(int, input().split())
    # 리프 노드의 값
    leaf_node_ans = [0] * (N+1)
    # 리프 노드의 번호
    leaf_node_num = []
    visit = []  # 방문체크
    left = [0] * (N+1)  # 왼쪽 자식 노드
    right = [0] * (N+1)  # 오른쪽 자식 노드
    for i in range(M):  # 인풋 받아서 리프 노드의 값과 번호 넣기
        l_node = list(map(int, input().split()))
        leaf_node_ans[l_node[0]] = l_node[1]
        leaf_node_num.append(l_node[0])
    for i in range(1, N+1):
        if i*2 <= N:
            # 왼쪽 자식 노드
            left[i] = i*2
        if i*2+1 <= N:
            # 오른쪽 자식 노드
            right[i] = i*2+1
    root = L
    preorder_traverse(root)  # 전위순회
    # L의 자식 노드들 중 리프 노드만 저장
    L_leaf = []
    for i in visit:
        if i in leaf_node_num:
            L_leaf.append(i)
    ans = []
    # 리프 노드의 값 갖고 오기
    for i in L_leaf:
        ans.append(leaf_node_ans[i])
    print("#{} {}".format(T, sum(ans)))
