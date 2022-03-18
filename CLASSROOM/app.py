s = input("Enter the string: ")
num = 0
alpha = 0

for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        num += 1

print("Letters: " + (alpha))
print("Digits: " + (num))