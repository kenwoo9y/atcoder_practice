N, X = map(int, input().split())
m = [int(input()) for i in range(N)]

counter = 0

for i in range(len(m)):
    X -= m[i]
    counter += 1

counter += (X // min(m))

print(counter)