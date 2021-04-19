def merge_sort(m):  # 분할하기
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = merge_sort(m[:middle])
    right = merge_sort(m[middle:])
    return merge(left, right)  # 분할이 끝났다면 합쳐주기

def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))  # 병합한 결과 저장
    idx_l, idx_r = 0, 0  # left의 인덱스 : idx_l, right의 인덱스 : idx_r
    idx = 0
    # left의 맨 마지막과 right의 맨 마지막을 비교해
    # left의 맨 마지막이 더 클 때 카운트 +1
    if left[-1] > right[-1]:
        cnt += 1
    while idx_l != len(left) or idx_r != len(right):
        if idx_l != len(left) and idx_r != len(right):
            if left[idx_l] <= right[idx_r]:
                result[idx] += left[idx_l]
                idx += 1
                idx_l += 1
            else:
                result[idx] += right[idx_r]
                idx += 1
                idx_r += 1
        elif idx_l != len(left):
            result[idx] += left[idx_l]
            idx += 1
            idx_l += 1
        elif idx_r != len(right):
            result[idx] += right[idx_r]
            idx += 1
            idx_r += 1
    return result


for T in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    # arr의 가운데 값, cnt 출력
    print("#{} {} {}".format(T, arr[N//2], cnt))

