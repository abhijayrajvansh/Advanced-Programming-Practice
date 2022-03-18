value = str(12345)

for num in value:
    num = int(num)
    if num % 2 != 0:
        print("odd")
    else:
        print("even")