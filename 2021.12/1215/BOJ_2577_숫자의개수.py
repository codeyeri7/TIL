A = int(input())
B = int(input())
C = int(input())
ans_list = [0] * 10
N = A * B * C
# 정수를 리스트로 변환하는 방법
N_list = list(map(int, str(N)))
for i in N_list:
    ans_list[i] += 1
for i in ans_list:
    print(i)
