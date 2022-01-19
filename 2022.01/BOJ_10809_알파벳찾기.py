alpha_arr = [-1 for _ in range(26)]  # -1로 이루어진 리스트 만들기
# 알파벳의 자리를 적은 딕셔너리
alpha_index = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10,
    'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17,  's': 18, 't': 19, 'u': 20,
    'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25
}
# 입력받은 문자열을 한 글자씩 리스트에 담는다
word = list(map(str, input()))
for i in range(len(word)):
    # 입력받은 word의 자리 번호를 al_idx에 저장하기
    word_index = word[i]
    al_idx = alpha_index[word_index]
    # -1로 이루어진 리스트에 al_idx 자리에 word의 인덱스 넣기
    # 이 때 이미 word의 인덱스가 들어가있다면 넘어가기
    if alpha_arr[al_idx] != -1:
        pass
    else:
        alpha_arr[al_idx] = i
for j in range(len(alpha_arr)):
    print(alpha_arr[j], end=' ')
