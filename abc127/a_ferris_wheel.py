A, B = map(int, input().split())

result = 0

if A >= 13:
    result = B
elif 6 <= A <= 12:
    result = B // 2

print(result)