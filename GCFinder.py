num1 = int(input("put your first number "))
num2 = int(input("put your second number "))
def gcf_finder():
    gcf = 0
    for i in range(2, num2 + 1):
        if (num1 % i == 0 and num2 % i == 0):
            gcf = i
    print(gcf)
gcf_finder()