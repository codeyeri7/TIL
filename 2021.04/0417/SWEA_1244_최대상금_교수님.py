def change(cnt):
    global ans
    curr = int("".join(money))
    print(curr, 'curr')

    if [curr, cnt] in visited:
        return

    visited.append([curr, cnt])

    if cnt == K:
        ans = max(ans, int(curr))
        return

    for i in range(len(money) - 1):
        for j in range(i + 1, len(money)):
            money[i], money[j] = money[j], money[i]
            change(cnt + 1)
            money[i], money[j] = money[j], money[i]


for tc in range(1, int(input()) + 1):
    money, K = input().split()
    money = list(money)
    print(money, 'money')
    visited = []
    K = int(K)
    ans = 0

    change(0)

    print("#{} {}".format(tc, ans))