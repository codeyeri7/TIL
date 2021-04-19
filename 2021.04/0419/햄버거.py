for T in range(1, int(input())+1):  # 테스트케이스 수 만큼 반복
    N, K = map(int, input().split())
    # 재료의 점수와 칼로리 정보
    material = [list(map(int, input().split())) for _ in range(N)]
    material_points = []
    material_cal = []
    for i in range(1<<N):  # 부분집합 만들기
        point = []
        cal = []
        for j in range(N):
            if i & (1<<j):
                # 재료의 점수 부분집합
                point.append(material[j][0])
                # 재료의 칼로리 부분집합
                cal.append(material[j][1])
        if sum(cal) <= 1000:  # 칼로리가 1000이 넘지 않는 선에서
            material_cal.append(cal)
            material_points.append(sum(point))
    max_point = max(material_points)  # 그 중 최고 점수를 갖고오기
    print("#{} {}".format(T, max_point))
