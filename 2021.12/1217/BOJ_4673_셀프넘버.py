# 각 자리수를 구하고 더하는 함수
def d(n):
    # 각 자리수를 일일히 나눠서...ㅎㅎ 구했었는데 map을 활용해 쉽게 구할 수 있었다ㅠ
    num_list = list(map(int, str(n)))
    ans = n + sum(num_list)
    return ans

# 1부터 10000까지 들어있는 리스트를 만들자
n_list = []
for i in range(1, 10000+1):
    n_list.append(i)

# 그 리스트에서 생성자가 있는 n을 지우자
n = 1
while n <= 10000:
    num = d(n)
    if num in n_list:
        n_list.remove(num)
    else:
        pass
    n += 1

# 생성자 없는 n을 하나씩 출력
for i in n_list:
    print(i)
