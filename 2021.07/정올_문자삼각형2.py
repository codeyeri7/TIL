n = int(input())
total = 0
cnt = 0
for i in range(1, n+1, 2):
    cnt += 1
    total += i
# print(total - (n-1), end=" ")

for k in range(cnt):
    a = n - 1
    for l in range(k):
        if k < 1:
            print(total + k, end=" ")
        elif k >= 1:
            print(total + k - a, end=" ")
            a -= 2
        print()
for k in range(n - cnt):
    a = n - 1
    for l in range(k, 0, -1):
        if k < 1:
            print(total + k, end=" ")
        elif k >= 1:
            print(total + k - a, end=" ")
            a -= 2
        print()
