# input = 0DEC
# pw_info = list(map(str, input()))
# result = []
# sixteen = []
# breaker = False  # 다중 for문을 빠져나오기 위한 변수 설정
# sixteen_num = []
# for i in range(N-1, -1, -1):
#     for j in range(M-1, -1, -1):
#         if pw_info[i][j] != '0':
#             # 뒤에서부터 돌아서 0이 아닌 것을 만나면
#             # for k in range(15):
#             for z in range(j, j-6, -1):
#                 sixteen.append(pw_info[i][z])
#             # if len(sixteen_num) != 0 and len(sixteen_num) % 15 == 0:
#             #     sixteen.append(sixteen_num)
#             #     sixteen_num = []
#             breaker = True
#             break
#     if breaker == True:
#         break
# sixteen = sixteen[::-1]
# # print(sixteen)
# eng = ['A', 'B', 'C', 'D', 'E', 'F']
# alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
# result = []
# final_ans = []
# # 16진수의 알파벳을 숫자로 바꾸기
# for i in range(len(sixteen)):
#     if sixteen[i] not in eng:
#         x = int(sixteen[i])
#     else:
#         x = alp[sixteen[i]]
#     result.append(x)
# print("#{}".format(T), end=' ')
# # 2진수로 바꾸기
# for i in range(len(result)):
#     binary = []
#     k = result[i]
#     while k > 0:
#         div = k // 2
#         mod = k % 2
#         k = div
#         binary.append(mod)
#     ans = binary[::-1]
#     # 4자리를 맞춰주기 위해 앞에 0 추가
#     while len(ans) < 4:
#         ans.insert(0, 0)
#     for j in ans:
#         final_ans.append(j)
# sixteen_final = []
# for i in final_ans:
#     sixteen_final.append(i)
# print(*sixteen_final)