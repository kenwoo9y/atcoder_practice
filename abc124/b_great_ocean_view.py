N = int(input())
H = list(map(int, input().split()))

counter = 0

for i in range(len(H)):
    judge = True
    for j in range(i):
        if H[i] < H[j]:
            judge = False
    if judge:
        counter += 1

print(counter)