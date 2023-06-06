A, B = map(int, input().split())

price = 1

while price * 10 // 100 <= B:
    if price * 8 // 100 == A:
        if price * 10 // 100 == B:
            print(price)
            break
    price += 1

else:
    print(-1)