N = int(input())

sum_X = 0
sum_Y = 0

for i in range(N):
    X,Y = map(int, input().split())

    sum_X += X
    sum_Y += Y

if sum_X > sum_Y:
    print("Takahashi")
elif sum_Y > sum_X:
    print("Aoki")
else:
    print("Draw")