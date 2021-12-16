T = int(input())
for tc in range(T):
    stu_point = list(map(int, input().split()))
    # 학생의 수
    stu_num = stu_point[0]
    # 점수 리스트에서 학생의 수는 뺀다.
    stu_point.pop(0)
    # 평균 넘은 학생의 수를 카운트한다.
    good_stu = 0
    # 점수 평균
    average = sum(stu_point) / stu_num
    for i in range(stu_num):
        # 평균을 넘은 점수라면
        if stu_point[i] > average:
            # 평균 넘은 학생 수 +1
            good_stu += 1
    # 평균 넘은 학생의 비율 구하기
    ans = good_stu / stu_num * 100
    # 소수점 3자리까지 출력 (40.0이어도 40.000이 되기 위해서는 format을 활용)
    ans = format(ans, ".3f")
    # 또 format을 활용해 숫자와 문자가 함께 출력되도록했다.
    print("{}%".format(ans))