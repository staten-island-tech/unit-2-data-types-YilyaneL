num1 = int(input("put your first number "))
num2 = int(input("put your second number "))
def gcfinder():
    x = 1
    for i in range(x, num1, num2):
        if num1 % x and num2 % x == 0:
            print(x)
    x = x + 1
gcfinder()