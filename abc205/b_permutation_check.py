N = int(input())
A = list(map(int, input().split()))

A.sort()
result = True

for i in range(len(A)):
    if A[i] != i + 1:
        result = False

print('Yes' if result else 'No')