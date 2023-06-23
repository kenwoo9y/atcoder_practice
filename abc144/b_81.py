N = int(input())

result = False

for i in range(1, 10):
    for j in range(1, 10):
        if N == i * j:
            result = True

print('Yes' if result else 'No')