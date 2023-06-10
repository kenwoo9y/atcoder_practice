N = int(input())
T, A = map(int, input().split())
H = [int(i) for i in input().split()]

diff_min = 1000000
point_number = 0

for i in range(len(H)):
    temperature = T - H[i] * 0.006
    if abs(temperature - A) <= diff_min:
        diff_min = abs(temperature - A)
        point_number = i + 1

print(point_number)