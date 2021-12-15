N = int(input())
point = list(map(int, input().split()))
M = max(point)
for i in range(N):
    point[i] = point[i] / M * 100
average = sum(point) / N
print(average)