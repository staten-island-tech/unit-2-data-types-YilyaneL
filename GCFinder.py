num1 = int(input("put your first number "))
num2 = int(input("put your second number "))
def gcf_finder():
    x=1
    y=1
    for i in (range(x, num1)):
        if (num1 % x == 0):
            num1f = x
    for i in (range(y, num2)):
        if (num2 % y == 0):
            num2f = y
    x = x + 1
    y = y + 1
    if num2f == num1f:
        print(max(num2f))
gcf_finder()