N = 3
arr = [[73, 21, 21], [11, 59, 40], [24, 31, 83]]
ans = 0
visit_r = [0] * N
visit_c = [0] * N
min_ans = 99 * N


def dfs(r, c):
    global min_ans, ans
    visit_r[r] = 1
    visit_c[c] = 1
    ans += arr[r][c]
    i = 0
    while i < N:
        if visit_c[i] == 0 and visit_r[r] == 0:
            dfs(r+1, i)
            ans -= arr[r][c]
            visit_r[r] = 0
            visit_c[c] = 0
            i = 0
            continue
        i += 1
    if ans <= min_ans:
        min_ans = ans
    ans -= arr[r][c]
    visit_r[r] = 0
    visit_c[c] = 0
    return
dfs(0, 0)