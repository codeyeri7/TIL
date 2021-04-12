binary = ''
nums = list(map(str, input()))
eng = ['A', 'B', 'C', 'D', 'E', 'F']
alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
result = []
for i in range(len(nums)):
    if nums[i] not in eng:
        x = int(nums[i])
    else:
        x = alp[nums[i]]
    result.append(x)
for i in range(len(result)):
    binary = []
    k = result[i]
    while k > 0:
        div = k // 2
        mod = k % 2
        x = div
        binary.append(mod)
    print(binary)
# 2진수 4자리로 바꾸는 법을 모르겠습니다...
# 비트연산 너무 어려워요....
