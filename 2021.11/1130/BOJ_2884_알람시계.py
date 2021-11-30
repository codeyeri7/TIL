H, M = map(int, input().split())
m_minus = 0

# M이 45분보다 작을 때
if M < 45:
    # M에서 45분을 뺸 후 60에서 남은 분을 빼준다.
    m_minus = M - 45
    M = 60 + (m_minus)
    # 0시라면 24시에서 1시간을 빼 23시로 만든다.
    if H == 0:
        H = 24 - 1
    # 아니라면 H에서 1시간을 빼준다.
    else:
        H -= 1
# M이 45분보다 높으면 M에서 45분만 빼면 된다.
else:
    M -= 45
    
print(H, M)