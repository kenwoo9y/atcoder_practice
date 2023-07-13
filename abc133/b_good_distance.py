from math import sqrt

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

counter = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        distance = 0
        for k in range(D):
            distance += (X[i][k] - X[j][k]) ** 2
        if sqrt(distance).is_integer():
            counter += 1

print(counter)