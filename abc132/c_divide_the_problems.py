N = int(input())
d = list(map(int, input().split()))

d.sort()
answer = d[N // 2] - d[N // 2 - 1]

print(answer)