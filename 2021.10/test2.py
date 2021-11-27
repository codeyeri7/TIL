for i in range(1, 11):
    for j in range(2, 12):
        if i in [3, 4, 7, 8] or j in [4, 5, 8, 9]:
        # if i == 3 or i == 4 or i == 7 or i == 8 or j == 4 or j == 5 or j == 8 or j == 9:
            print(0, end='')
        else:
            print(1, end='')
    print()