import sys
N = int(input())
number = list(map(int, sys.stdin.readline().split()))
print(min(number), max(number))