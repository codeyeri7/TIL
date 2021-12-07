N = int(input())
for i in range(1, N+1):
    # *이 i개 만큼 찍혀야 한다.
    for j in range(i):
        # *이 바로 옆에 연속적으로 찍히기 위해 end=""를 추가한다.
        print("*", end="")
    print()
