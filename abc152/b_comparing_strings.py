a, b = map(str, input().split())

if a * int(b) <= b * int(a):
    print(a * int(b))
else:
    print(b * int(a))