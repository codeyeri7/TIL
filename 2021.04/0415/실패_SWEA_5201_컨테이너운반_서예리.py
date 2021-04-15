# 런타임에러의 지옥...
def max_container(list):  # 필터함수 만들기
    # truck의 적재량보다 작거나 같은 것 반환
    if list <= truck[i]:
        return True
    else:
        return None


for T in range(1, int(input())+1):
    # N = 컨테이너 개수, M = 트럭 수
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    total = 0  # 최종 컨테이너 적재량
    ans = 0
    max_idx = 100
    for i in range(M):  # 트럭을 기준으로
        # 필터함수 사용
        able_con = list(filter(max_container, container))
        # 찾았으면 토탈에 추가하기
        total += max(able_con)
        # 배달된 컨테이너는 0으로 바꿔주기
        max_idx = container.index(max(able_con))
        container[max_idx] = 0
    print("#{} {}".format(T, total))