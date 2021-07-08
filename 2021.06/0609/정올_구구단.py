while True:
    s, e = map(int, input().split())
    if 2 <= s <= 9 and 2 <= e <= 9:
        if s < e:
            for j in range(1, 10):
                for i in range(s, e+1):
                    if i * j < 10:
                        print(f'{i} * {j} =  {i * j}', end="   ")
                    else:
                        print(f'{i} * {j} = {i * j}', end="   ")
                print(" ")
            break
        else:
            for j in range(1, 10):
                for i in range(s, e-1, -1):
                    if i * j < 10:
                        print(f'{i} * {j} =  {i * j}', end="   ")
                    else:
                        print(f'{i} * {j} = {i * j}', end="   ")
                print(" ")
            break
    else:
        print("INPUT ERROR!")


