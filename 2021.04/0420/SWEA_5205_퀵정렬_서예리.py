# Hoare-Partition
# 처음에 낼 때 마지막 테케가 런타임 에러났는데, 다시 내니까 통과됨.....
def quicksort(mlist: list, l: int, r: int):
    if l < r:
        s = partition(mlist, l, r)
        quicksort(mlist, l, s-1)
        quicksort(mlist, s+1, r)
    return mlist

def partition(m2list: list, l: int, r: int):
    p = m2list[l]
    i = l
    j = r
    while i < j:  # i <= j로 하니까 i와 j가 같을 때 무한반복해서 수정함
        while m2list[i] <= p:
            if i == r:  # 이 조건을 안 넣어주니 i가 정해둔 l을 초과해서 막 넘어가길래 추가했다.
                break
            i += 1
        while m2list[j] >= p:
            if j == l:  # j도 마찬가지
                break
            j -= 1
        if i < j:
            m2list[i], m2list[j] = m2list[j], m2list[i]

    m2list[l], m2list[j] = m2list[j], m2list[l]
    return j


for T in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = quicksort(arr, 0, N-1)
    print("#{} {}".format(T, arr[N//2]))