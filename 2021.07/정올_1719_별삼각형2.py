n, m = map(int, input().split())
mid = (2*n-1)//2
mid_one = mid
mid_plusone = mid
check = []
check.append(mid)
# 1의 경우
if m == 1 and n < 100 and n > 0:
    a = 0
    mid = n // 2
    # 삼각형 위의 절반
    for i in range(mid+1):
        a += 1  # 별 개수 하나씩 추가
        for j in range(1, a+1):
            print('*', end='')
        print()
    # 아래 절반
    for i in range(mid+1, n):
        a -= 1  # 절반 이후로는 별 개수 하나씩 빼기
        for j in range(a, 0, -1):
            print('*', end='')
        print()

elif m == 2 and n < 100 and n > 0:
    mid = n // 2
    a = mid+1
    # 삼각형 위의 절반
    for i in range(mid + 1):
        a -= 1  # 빈 공간 하나씩 빼기
        for j in range(mid + 1):
            if j < a:
                print(' ', end='')
            else:
                print('*', end='')
        print()
    # 아래 절반
    for i in range(mid + 1, n):
        a += 1  # 절반 이후로는 빈 공간 하나씩 추가
        for j in range(mid + 1):
            if j < a:
                print(' ', end='')
            else:
                print('*', end='')
        print()

# elif m == 3 and n < 100 and n > 0:
#     mid = n // 2
#     a = mid + 1
#     for i in range(mid + 1):
#         for j in range()
#     for i in range(mid + 1, n):
#         for j in range((2*n)-1):
#             if j in check:
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print()
#         mid_one -= 1
#         mid_plusone += 1
#         check.append(mid_one)
#         check.append(mid_plusone)
#
# elif n < 1 or n > 100 or m < 1 or m > 3:
#     print('INPUT ERROR!')

