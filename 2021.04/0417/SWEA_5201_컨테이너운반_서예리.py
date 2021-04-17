for T in range(1, int(input())+1):
    # N = 컨테이너 개수, M = 트럭 수
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse=True)  # 무게가 무거운 순으로
    truck.sort(reverse=True)  # 실을 수 있는 적재량이 큰 순으로
    total = 0  # 최종 컨테이너 적재량
    i = 0  # 트럭 idx
    j = 0  # 화물 idx
    # 더 이상 화물이 없거나, 움직일 수 있는 트럭이 없을때까지 반복
    while i < M and j < N:
        # 화물이 적재량보다 작거나 같을 때
        if truck[i] >= container[j]:
            total += container[j]  # 최종 적재량에 더하기
            i += 1  # 다음 트럭
            j += 1  # 다음 화물
        else:
            j += 1
    print("#{} {}".format(T, total))