H, M = map(int, input().split())
m_minus = 0
if M < 45:
    m_minus = M - 45
    M = 60 + (m_minus)
    if H == 0:
        H = 24 - 1
    else:
        H -= 1
else:
    M -= 45
print(H, M)