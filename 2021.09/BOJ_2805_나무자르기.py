N, M = map(int, input().split())
trees = list(map(int, input().split()))
s, e = 1, max(trees)
while s <= e:
    mid = (s + e) // 2
    get_t = 0
    for i in trees:
        # 나무의 높이가 mid보다 큰 경우에만 더해준다.
        if i > mid:
            get_t += i - mid
    # 가져갈 수 있는 나무의 합이 아직 못 미쳤을 때
    if M > get_t:
        # mid가 현재보다 더 작아야한다.
        e = mid - 1
    # 가져갈 수 있는 나무의 합이 M보다 클 때
    else:
        # mid가 현재보다 더 커야한다.
        s = mid + 1
print(e)  # end 값이 절단기 길이의 최대값
