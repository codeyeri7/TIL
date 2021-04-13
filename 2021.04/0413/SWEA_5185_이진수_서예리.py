for T in range(1, int(input())+1):
    nums = list(map(str, input().split()))  # N과 16진수 같이 인풋
    N = int(nums.pop(0))  # N 따로 저장
    sixteen = list(nums[0])
    eng = ['A', 'B', 'C', 'D', 'E', 'F']
    alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = []
    final_ans = []
    print(nums)
    print(sixteen)
    # 16진수의 알파벳을 숫자로 바꾸기
    for i in range(N):
        if sixteen[i] not in eng:
            x = int(sixteen[i])
        else:
            x = alp[sixteen[i]]
        result.append(x)
    print("#{}".format(T), end=' ')
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
    for i in final_ans:
        print(i, end='')
    print()