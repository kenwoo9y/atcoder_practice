N, K = map(int, input().split())
h = [int(input()) for i in range(N)]

h.sort()
result = min(h[i+K -1] - h[i] for i in range(N - K + 1))

print(result)