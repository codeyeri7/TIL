def find_min(string):
    # 제일 작은 문자열 임의 선정
    s_min = string[0]
    for j in range(len(string)):
        # 문자열 대소 비교
        if string[j] <= s_min:
            # 제일 작다면 s_min 교체
            s_min = string[j]
    return s_min

def delete_element(string, element):
    # s_dlt를 element가 위치한 인덱스 값으로 설정
    s_dlt = string.index(element)
    # 해당 인덱스의 앞뒤로 문자열을 자른 후 다시 합친다.
    ans = string[:s_dlt] + string[s_dlt+1:]
    return ans

def reverse(string):
    s_reverse = ''
    # 문자열을 뽑아 뒤로 붙여서 다시 저장
    for j in string:
        s_reverse = j + s_reverse
    print(s_reverse)

def delete_numbers(string, empty_list):
    s_empty = ''
    # 숫자만 따로 s_int에 저장
    s_int = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for j in string:
        # 문자열 중 숫자가 아닌 경우에
        if j not in s_int:
            # 빈 문자열에 알파벳만 저장
            s_empty += j
        # 숫자가 나온 경우에
        else:
            # s_empty가 비어있는 경우
            if s_empty != '':
                # empty_list에 s_empty 추가
                empty_list.append(s_empty)
                # 다시 빈 문자열로 되돌리기
                s_empty = ''
    return empty_list

a = 'a1!!Abb22B@cC3#dd$$4'
t = ''
for i in range(len(a)):
    tt = find_min(a)
    a = delete_element(a, tt)
    t = tt + t
    print(a)
    print(t)
    print()

reverse(t)
print()
b = 'a123ba23aca343zz8'
strings = []
delete_numbers(b, strings)
print(strings)