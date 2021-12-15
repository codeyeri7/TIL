remainder_list = []  # 나머지들이 담길 리스트
for i in range(10):
    N = int(input())
    remainder = N % 42  # 나머지
    # 만약 나머지 리스트에 N의 나머지와 같은 수가 없다면?
    if remainder not in remainder_list:
        # 나머지 리스트에 N의 나머지 추가하기
        # 같은 수가 있으면 추가하지 않는다.
        remainder_list.append(remainder)
# 그렇게 모인 나머지들의 개수만 출력
print(len(remainder_list))