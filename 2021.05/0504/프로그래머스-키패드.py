def find_key(curr_r, curr_c):
    global ans
    a = curr_r - arrive_r
    b = curr_c - arrive_c
    total = abs(a) + abs(b)
    ans.append(total)


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
          4: (1, 0), 5: (1, 1), 6: (1, 2),
          7: (2, 0), 8: (2, 1), 9: (2, 2),
          '*': (3, 0), 0: (3, 1), '#': (3, 2)}
L_num = [1, 4, 7]  # 왼손으로 누를 수 있는 수
R_num = [3, 6, 9]  # 오른손으로 누를 수 있는 수
L_Queue = []
R_Queue = []
arrive = []
answer = ""
L_curr_r, L_curr_c = 3, 0  # 왼손 출발점
R_curr_r, R_curr_c = 3, 2  # 오른손 출발점

for i in range(len(numbers)):
    if numbers[i] in L_num:  # 왼손으로 누를 수 있는 수
        L_Queue.append(keypad[numbers[i]])
        answer += "L"
        # 왼손 현재 위치 갱신
        L_curr_r, L_curr_c = L_Queue.pop(0)
    elif numbers[i] in R_num:  # 오른손으로 누를 수 있는 수
        R_Queue.append(keypad[numbers[i]])
        answer += "R"
        # 오른손 현재 위치 갱신
        R_curr_r, R_curr_c = R_Queue.pop(0)
    # 왼손, 오른손 중 가까운 손이 눌러야하는 수
    elif numbers[i] not in L_num and numbers[i] not in R_num:
        arrive.append(keypad[numbers[i]])
        arrive_r, arrive_c = arrive.pop(0)
        ans = []
        # 왼손과의 거리
        find_key(L_curr_r, L_curr_c)
        # 오른손과의 거리
        find_key(R_curr_r, R_curr_c)
        # 더 가까운 곳 찾기
        if ans[0] < ans[1]:
            answer += "L"
            # 왼손 현재 위치 갱신
            L_curr_r, L_curr_c = arrive_r, arrive_c
        elif ans[0] > ans[1]:
            answer += "R"
            # 오른손 현재 위치 갱신
            R_curr_r, R_curr_c = arrive_r, arrive_c
        elif ans[0] == ans[1]:
            if hand == "left":
                answer += "L"
                # 왼손 현재 위치 갱신
                L_curr_r, L_curr_c = arrive_r, arrive_c
            else:
                answer += "R"
                # 오른손 현재 위치 갱신
                R_curr_r, R_curr_c = arrive_r, arrive_c
print(answer)