n_list = []
for i in range(9):
    N = int(input())
    n_list.append(N)
ans = max(n_list)
# max의 인덱스를 찾고 싶을 때!! list.index()를 사용하자!
ans_idx = n_list.index(ans)
print(ans)
print(ans_idx+1)