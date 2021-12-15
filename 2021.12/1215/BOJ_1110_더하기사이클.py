N = int(input())
cycle = 0  # 사이클
new = N  # 우선 새로운 수에 N을 대입
while True:
    front = new // 10  # 앞 자리 수
    back = new % 10  # 뒷 자리 수
    n_back = (front + back) % 10  # 앞, 뒷 자리 수 합친 수의 뒷 자리 수
    new = back * 10 + n_back  # 새로운 수
    cycle += 1  # 사이클 추가
    if new == N:  # 새로운 수와 N이 같다면?
        print(cycle)  # 사이클 출력
        break  # while문 종료


