def merge(left, right):
    global idx, idx_l, idx_r
    while idx_l < len(left) or idx_r < len(right):
        if idx_l < len(left) and idx_r < len(right):
            if left[idx_l] <= right[idx_r]:
                result[idx] = left[idx_l]
                idx += 1
                idx_l += 1
            else:
                result[idx] = right[idx_r]
                idx += 1
                idx_r += 1
        elif len(right) > 0:
            result[idx] = right[idx_r]
            idx += 1
            idx_r += 1

def merge_sort(m):
    if len(m) == 1:
        return m
    left = []
    right = []
    middle = len(m) // 2
    for x in range(0, middle):
        left.append(m[x])
    for x in range(middle, len(m)):
        right.append(m[x])
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

for T in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = [0] * N
    idx_l = 0
    idx_r = 0
    idx = 0
    merge_sort(arr)
    print(result)
