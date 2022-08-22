def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

num = input("What number would you like to start with: ")
num = int(num)

while num != 1:
    print(num)
    if isEven(num):
        num = num / 2

    else:
        num = num * 3
        num = num + 1

print(num)
close = input("Press Enter to close")