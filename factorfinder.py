def find_factor():
    x = 1
    num = int(input("number you want to find the factors of: "))
    for i in (range(x, num)):
        if (num % x == 0):
            print(x)
    x = x + 1
find_factor()