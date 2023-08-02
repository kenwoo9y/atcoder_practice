A= list(map(int, input().split()))

A.sort(reverse=True)
diff = []

for i in range(len(A) - 1):
    diff.append(A[i] - A[i + 1])

result = True
for i in range(len(diff) - 1):
    if diff[i] != diff[i - 1]:
        result = False

print('Yes' if result else 'No')