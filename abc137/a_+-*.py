A, B = map(int, input().split())

sum = A + B
diff = A - B
product = A * B

print(max(sum, diff, product))