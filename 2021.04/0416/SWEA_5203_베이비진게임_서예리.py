# 6장의 카드를 다 안 받아도 먼저 run이나 triplet이 되면 이기는 거니까
# 조건에 맞으면 break를 넣어서 반복문을 종료시켜야함!!!!!

for T in range(1, int(input())+1):
    card = list(map(int, input().split()))
    # 플레이어가 받은 카드 개수를 세기 위한 배열
    play_1 = [0] * 10
    play_2 = [0] * 10
    win = 0  # 승자

    for i in range(len(card)):
        # i가 짝수일 때 == 플레이어 1
        if i % 2 == 0:
            play_1[card[i]] += 1
            if play_1[card[i]] >= 3:  # run
                win = 1
                break
            # triplet 찾기(1~8)
            if card[i] != 0 and card[i] != 9:
                # 추가된 카드의 양 옆
                if play_1[card[i]+1] >= 1 and play_1[card[i]-1] >= 1:
                    win = 1
                    break
                # 오른쪽 2개가 연속으로 1 이상이어서 triplet이 됐을 때
                elif play_1[card[i]+1] >= 1 and play_1[card[i]+2] >= 1:
                    win = 1
                    break
                # 왼쪽 2개가 연속으로 1 이상이어서 triplet이 됐을 때
                elif play_1[card[i]-1] >= 1 and play_1[card[i]-2] >= 1:
                    win = 1
                    break
            # 카드가 0인 경우는 내 옆인 1과 그 옆인 2가 있어야 하니까 +1 +2
            if card[i] == 0:
                if play_1[card[i]+1] >= 1 and play_1[card[i]+2] >= 1:
                    win = 1
                    break
            # 카드가 9인 경우도 마찬가지로 -1 -2
            if card[i] == 9:
                if play_1[card[i]-1] >= 1 and play_1[card[i]-2] >= 1:
                    win = 1
                    break
        # i가 홀수일 때 == 플레이어 2
        else:
            play_2[card[i]] += 1
            # run
            if play_2[card[i]] >= 3:
                win = 2
                break
            # triplet(1~8)
            if card[i] != 0 and card[i] != 9:
                if play_2[card[i]+1] >= 1 and play_2[card[i]-1] >= 1:
                    win = 2
                    break
                elif play_2[card[i]+1] >= 1 and play_2[card[i]+2] >= 1:
                    win = 2
                    break
                elif play_2[card[i] - 1] >= 1 and play_2[card[i] - 2] >= 1:
                    win = 2
                    break
            # triplet(0)
            if card[i] == 0:
                if play_2[card[i]+1] >= 1 and play_2[card[i]+2] >= 1:
                    win = 2
                    break
            # triplet(9)
            if card[i] == 9:
                if play_2[card[i]-1] >= 1 and play_2[card[i]-2] >= 1:
                    win = 2
                    break
    print("#{} {}".format(T, win))