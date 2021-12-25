import os.path
import string
import random
import pickle

# 시작화면
start_message = """암호화/복호화 프로그램입니다 ^o^
1. 암호화
2. 복호화
3. 종료
"""
print(start_message)
num_input = int(input("원하시는 기능을 선택하세요: "))
if type(num_input) == int:
    # 암호화 선택
    if num_input == 1:
        password = input("암호화를 할 파일 이름을 입력하세요: ")
        # 암호화 할 파일 명
        file = f'./{password}'
        # 암호화 할 파일이 같은 폴더 내에 있다면
        if os.path.isfile(file):
            # record.txt를 열어서
            open_file = open("record.txt", "r+")
            strings = open_file.readlines()
            confirm = password + "\n"
            open_file.close()
            # confirm이 record.txt에 적혀있다면 이미 암호화 완료된 것
            if confirm in strings:
                print("이미 암호화가 완료된 파일입니다.")
                print(start_message)
                num_input = int(input("원하시는 기능을 선택하세요: "))
            else:
                password = password.replace(".txt", "")
                # 딕셔너리 만들기
                a = string.ascii_letters
                b = string.digits
                aa = list(map(str, a))
                bb = list(map(str, b))
                aabb = aa + bb
                random.shuffle(aabb)
                a = list(map(str, a))
                b = list(map(str, b))
                ab = a + b
                decbook = dict(zip(ab, aabb))  # 암호화용 딕셔너리
                encbook = {}
                print(decbook)
                # 암호화 시작
                for i in decbook:
                    val = decbook[i]
                    encbook[val] = i  # encbook은 복호화용
                print(password)
                # 암호화 할 파일을 열고(읽기 전용)
                code_file = open(f'{password}.txt', "r")
                # txt파일을 읽을 때 리스트로 읽혀지니까
                code_strings = code_file.readlines()
                # 리스트에서 꺼내서 str으로 변환
                code_strings = code_strings[0]
                code_strings = list(map(str, code_strings))
                print(code_strings)
                code_file.close()  # 파일 닫아주기
                # 다시 암호화 할 파일 열기(수정용)
                write_code = open(f'{password}.txt', "w+")
                result_code = []
                # txt안에 있는 문자열이 리스트로 나오니까
                # 리스트 속 문자를 하나하나 대입해 암호화 후
                # 다시 새로운 리스트(result_code)에 집어 넣기
                for j in code_strings:
                    if j in decbook:
                        code_strings = j.replace(j, decbook[j])
                        result_code.append(code_strings)
                    else:
                        result_code.append(j)
                # 리스트를 str로 변환
                result_code = "".join(result_code)
                print(result_code)
                # 암호화 할 파일에 암호화 된 문자열로 바꿔서 넣기
                write_code.write(result_code)
                write_code.close()  # 파일 닫기
                # 딕셔너리 pwd에 저장
                fw = open(f'{password}.pwd', 'wb')
                pickle.dump(decbook, fw)
                # 암호화 완료해서 record.txt에 목록 추가
                f = open("./record.txt", "a+")
                f.write(f'{password}.txt\n')
                f.close()
                print("암호화를 완료했습니다.")
    else:
        print("파일이 존재하지 않습니다.")
        print(start_message)
        num_input = input("원하시는 기능을 선택하세요: ")
else:
    print("잘못된 입력입니다.")
    print(start_message)
    num_input = input("원하시는 기능을 선택하세요: ")