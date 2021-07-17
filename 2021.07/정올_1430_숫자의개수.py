A = int(input())
B = int(input())
C = int(input())
num = A * B * C
ans = [0] * 10
# 숫자를 리스트 형식으로 변환
str_num = list(map(int, str(num)))
# num에서 나온 숫자의 자릿수에 1씩 더해서 개수 세기
for i in str_num:
    ans[i] += 1
# ans의 숫자 하나씩 출력
for j in range(len(ans)):
    print(ans[j])