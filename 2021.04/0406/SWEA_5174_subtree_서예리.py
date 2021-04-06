# 전위순회
def preorder_traverse(N):
    if N != 0:
        visit.append(N)
        preorder_traverse(ch1[N])
        preorder_traverse(ch2[N])


for T in range(1, int(input())+1):
    # E : 간선의 개수, N : 루트 노드
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    ch1 = [0] * (E+2)  # 자식노드 1
    ch2 = [0] * (E+2)  # 자식노드 2
    pa = [0] * (E+2)  # 부모노드
    visit = []  # 방문체크
    for i in range(len(arr)):
        # arr의 짝수번째에 부모노드가 있으니까
        # 부모노드 인덱스로 자식 번호 저장
        if i % 2 == 0:
            if ch1[arr[i]] == 0:  # 자식노드1에 우선적으로 넣기
                ch1[arr[i]] = arr[i+1]
            else:
                ch2[arr[i]] = arr[i+1]
        else:  # 반대로 부모 번호 저장
            pa[arr[i]] = arr[i-1]
    # 전위순회로 서브 트리에 속한 노드 찾기
    preorder_traverse(N)
    print("#{} {}".format(T, len(visit)))