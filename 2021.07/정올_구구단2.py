s, e = map(int, input().split())
if s > e:
    for i in range(s, e-1, -1):
        for j in range(1, 4):
            if i*j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print()
        for j in range(4, 7):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print()
        for j in range(7, 10):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print('\n ')
else:
    for i in range(s, e+1):
        for j in range(1, 4):
            if i*j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print()
        for j in range(4, 7):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print()
        for j in range(7, 10):
            if i * j < 10:
                print(f'{i} * {j} =  {i * j}', end='   ')
            else:
                print(f'{i} * {j} = {i * j}', end='   ')
        print('\n ')
