n, m = map(int, input().split())
mid = (2*n-1)//2
mid_one = mid
mid_plusone = mid
check = []
check.append(mid)
if m == 1 and n < 100 and n > 0:
    a = 0
    for i in range(n):
        a += 1
        for j in range(1, a+1):
            print('*', end='')
        print()

elif m == 2 and n < 100 and n > 0:
    a = n+1
    for i in range(n):
        a -= 1
        for j in range(a, 0, -1):
            print('*', end='')
        print()

elif m == 3 and n < 100 and n > 0:
    for i in range(n):
        for j in range((2*n)-1):
            if j in check:
                print('*', end='')
            else:
                print(' ', end='')
        print()
        mid_one -= 1
        mid_plusone += 1
        check.append(mid_one)
        check.append(mid_plusone)

elif n < 1 or n > 100 or m < 1 or m > 3:
    print('INPUT ERROR!')