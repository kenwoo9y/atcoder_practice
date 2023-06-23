N = int(input())

result = False

for i in range(N + 1):
    for j in range(N + 1 -i):
        if N == 4 * i + 7 * j:
            result = True

print('Yes' if result else 'No')