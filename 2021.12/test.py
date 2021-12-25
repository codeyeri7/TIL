# import string
# import random
# import pickle
# password = input("암호화를 할 파일 이름을 입력하세요: ")
# password = password.replace(".txt", "")
# print(password)
# a = string.ascii_letters
# b = string.digits
# aa = list(map(str, a))
# bb = list(map(str, b))
# random.shuffle(aa)
# random.shuffle(bb)
# a = list(map(str, a))
# b = list(map(str, b))
# alpha_pass = dict(zip(a, aa))
# num_pass = dict(zip(b, bb))
# print(alpha_pass)
# print(num_pass)
#
# with open(f'{password}.pwd', 'wb') as fw:
#     pickle.dump(alpha_pass, fw)
#     pickle.dump(num_pass, fw)
#
# f = open("./record.txt", "a+")
# f.write(f'{password}.txt\n')
# strings = f.readlines()
# print(strings)
# f.close()


file = open("hana/wantchange.txt", "r")
strings = file.readlines()
str_st = strings[0]
print(str_st, type(str_st))
file.close()