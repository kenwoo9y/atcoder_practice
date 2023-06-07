from math import sqrt

N, D = map(int, input().split())

counter = 0

for i in range(N):
    X, Y = map(int, input().split())
    if sqrt(X ** 2 + Y ** 2) <= D:
        counter += 1

print(counter)