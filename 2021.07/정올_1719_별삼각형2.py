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
# 2의 경우
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
# 3의 경우
elif m == 3 and n < 100 and n > 0:
    nums = []
    pop_nums = []
    # nums에 0부터 n까지 숫자 추가
    for i in range(n):
        nums.append(i)
    # 위에 절반
    for i in range(n // 2):
        for j in range(n):
            if j in nums:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        # 양 끝의 인덱스 제거
        zero_pop = nums.pop(0)
        last_pop = nums.pop(-1)
        # 제거한 숫자 저장
        pop_nums.append(zero_pop)
        pop_nums.append(last_pop)
    # 아래 절반
    for i in range(n // 2, n):
        for j in range(n):
            if j in nums:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        # pop_nums가 비어있지 않을때
        if len(pop_nums) > 0:
            # 아까 뺐던 인덱스 다시 추가
            for k in range(2):
                put_num = pop_nums.pop(-1)
                nums.append(put_num)
                nums = sorted(nums)  # 정렬

# elif m == 4 and n < 100 and n > 0:


#
#
# elif n < 1 or n > 100 or m < 1 or m > 3:
#     print('INPUT ERROR!')

