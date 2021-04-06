# 힙
def heap(a, n):
    # 먼저 루트 노드의 값을 넣어준 후
    heap_list[a] = n
    # 루트노드까지 힙의 조건에 맞게 확인
    while a//2 > 0:
        if a >= 2:
            if heap_list[a] < heap_list[a//2]:
                heap_list[a], heap_list[a//2] = heap_list[a//2], heap_list[a]
        a = a//2
    return heap_list


for T in range(1, int(input())+1):
    N = int(input())  # 노드의 개수
    # 힙의 조건대로 부모 노드의 값 < 자식 노드의 값 대로 바꾼 값
    heap_list = [0] * (N+1)
    # 입력받은 자연수를 저장
    num = list(map(int, input().split()))
    for i in range(N):
        heap(i+1, num[i])  # 힙 함수
    p_node = []  # 조상 노드 모아놓기
    while N//2 > 0:
        p_node.append(heap_list[N//2])
        N = N//2
    print("#{} {}".format(T, sum(p_node)))
