N = int(input())
A = int(input())

result = False

if N % 500 <= A:
    result = True

print('Yes' if result else 'No')