numbers = list(map(int, input()))
num_list = []
# 숫자를 7개씩 나눠서 리스트에 저장
for i in range(0, len(numbers), 7):
    num = []
    for j in range(i, i+7):
        num.append(numbers[j])
    num_list.append(num)
# 7개씩 나눈 숫자에 2의 제곱들을 곱한 후 더해서 10진수 만들기
for i in range(len(num_list)):
    ans = 0
    a = 0
    for j in range(6, -1, -1):
        if num_list[i][j] == 1:
            ans += (2 ** a)
        a += 1
    print(ans)
