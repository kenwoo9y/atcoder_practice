N = int(input())

for x in range(N + 1):
    for y in range(N - x + 1):
        for z in range(N - x - y + 1):
            if (x + y + z) <= N:
                print(x, y, z)