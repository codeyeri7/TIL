# input = 01D06079861D79F99F
nums = list(map(str, input()))  # N과 16진수 같이 인풋
eng = ['A', 'B', 'C', 'D', 'E', 'F']
alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
result = []
final_ans = []
# 16진수의 알파벳을 숫자로 바꾸기
for i in range(len(nums)):
    if nums[i] not in eng:
        x = int(nums[i])
    else:
        x = alp[nums[i]]
    result.append(x)
# 2진수로 바꾸기
for i in range(len(result)):
    binary = []
    k = result[i]
    while k > 0:
        div = k // 2
        mod = k % 2
        k = div
        binary.append(mod)
    ans = binary[::-1]
    # 4자리를 맞춰주기 위해 앞에 0 추가
    while len(ans) < 4:
        ans.insert(0, 0)
    for j in ans:
        final_ans.append(j)
tenten = []
for i in range(0, len(final_ans), 7):
    ten_bin = []
    for j in range(i, i+7):
        if j < len(final_ans):
            ten_bin.append(final_ans[j])
    tenten.append(ten_bin)
for k in range(len(tenten)):
    ans = 0
    a = 0
    for x in range(len(tenten[k])-1, -1, -1):
        if tenten[k][x] == 1:
            ans += (2 ** a)
        a += 1
    print(ans)
