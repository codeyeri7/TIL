def find_parent(parent_list, node):  # 조상노드 찾기
    for i in range(V+1):
        if ch1[i] == node:
            parent_list.append(i)
            if i == 1:  # 루트노드 도착하면 종료
                return
            find_parent(parent_list, i)  # 조상노드 다 찾을 때까지 재귀
        elif ch2[i] == node:
            parent_list.append(i)
            if i == 1:
                return
            find_parent(parent_list, i)


def inorder(root):  # 중위순회
    if root != 0:
        inorder(ch1[root])
        visit.append(root)
        inorder(ch2[root])


for T in range(1, int(input())+1):
    V, E, node1, node2 = map(int, input().split())
    ch1 = [0] * (V+1)
    ch2 = [0] * (V+1)
    visit = []
    tree = list(map(int, input().split()))
    for i in range(E):
        p, c = tree[i*2], tree[i*2+1]
        if ch1[p] == 0:  # 자손노드 저장
            ch1[p] = c
        else:
            ch2[p] = c
    parent_list_1 = [node1]  # node1의 조상노드
    parent_list_2 = [node2]  # node2의 조상노드
    find_parent(parent_list_1, node1)  # node1의 조상노드 찾기
    find_parent(parent_list_2, node2)  # node2의 조상노드 찾기
    same_parent = []  # 조상노드 중 공통인 노드 찾기
    for i in parent_list_1:
        if i in parent_list_2:
            same_parent.append(i)
    ans_parent = same_parent[0]  # 공통조상노드 중 맨 앞에 있는게 제일 가까운 조상노드
    inorder(ans_parent)  # 공통조상노드의 서브트리 크기 찾기
    print("#{} {} {}".format(T, ans_parent, len(visit)))