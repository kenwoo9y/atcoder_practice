from math import ceil, floor

N = int(input())

numbers = []
total_amount = 0

numbers.append(N)

while True:
    x = next(filter(lambda i: i >= 2, numbers), None)

    if x == None:
        break

    total_amount += x

    numbers.remove(x)

    ceil_number = ceil(x/2)
    floor_number = floor(x/2)
    numbers.append(ceil_number)
    numbers.append(floor_number)
    
    continue

print(total_amount)