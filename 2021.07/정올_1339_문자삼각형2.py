import string
n = int(input())
if n < 0 or n > 100 or n % 2 == 0:
    print("INPUT ERROR")
else:
    alpha = string.ascii_uppercase
    total = 0
    b = n // 2
    # 제일 마지막 숫자를 알기 위해
    for i in range(1, n + 1, 2):
        total += i

    # 삼각형을 반으로 나눠서 알파벳이 나타나도록 한다.
    # 여기서는 1 ~ (n//2)+1번째, (n//2)+1 ~ n번째 줄로 나눴다.
    for k in range(b + 1):
        a = n - 1
        ans = total + k - (n - 1)  # 제일 처음 시작하는 수는 total 값에서 n-1를 뺀 값이다.
        for l in range(k + 1):
            if l < 1:
                # 알파벳 A가 0번부터 시작하니 -1을 해줌
                # Z까지 다 돌면 다시 A부터 돌아야하니 26으로 나눈 나머지값을 활용
                print(alpha[(ans - 1) % 26], end=" ")
            elif l >= 1:
                print(alpha[(ans - a - 1) % 26], end=" ")
                ans -= a  # 옆줄로 갈 수록 숫자가 줄어드는데, n-1에서 한줄로 갈 수록 2씩 줄어든다.
                a -= 2
        print()

    for k in range(n - (b + 1) + 1, n):  # 삼각형의 꺾이는 부분
        a = n - 1
        ans = total + k - (n - 1)
        for l in range(b, 0, -1):
            if l >= b:
                print(alpha[(ans - 1) % 26], end=" ")
            elif l < b:
                print(alpha[(ans - a - 1) % 26], end=" ")
                ans -= a
                a -= 2
        b -= 1
        print()
