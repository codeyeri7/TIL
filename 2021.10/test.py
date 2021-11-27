import random
from itertools import combinations

# 랜덤한 수 20개 리스트에 담기
nums = []
for i in range(20):
    x = random.randint(-300, 300)
    nums.append(x)
print(nums)

# 리스트에서 3개의 수 조합 구하기 (combinations를 사용하면 중복되지 않은 조합을 구할 수 있다.)
a = list(combinations(nums, 3))
print(a)

# 3개의 수 합의 절댓값 중 가장 큰 수를 구하고, 그 수가 음수라면 음수로 출력
# three_max가 3개의 수 합의 절댓값 중 가장 큰 수
# ans가 three_max를 음수, 양수에 맞게 출력
three_max = 0
max_ans = 0
for i in a:
    three_sum = abs(sum(i))
    if three_sum >= three_max:
        three_max = three_sum
        max_ans = sum(i)
print(three_max, max_ans)

# 3개의 수 합의 절댓값 중 가장 작은 수를 구하고, 그 수가 음수라면 음수로 출력
# three_min이 3개의 수 합의 절댓값 중 가장 작은 수
# ans가 three_min을 음수, 양수에 맞게 출력
three_min = 987654321
min_ans = 0
for i in a:
    three_sum = abs(sum(i))
    if three_sum <= three_min:
        three_min = three_sum
        min_ans = sum(i)
print(three_min, min_ans)