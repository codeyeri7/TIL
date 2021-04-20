for T in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    visit = [0] * N
    min_ans = 99 * N

