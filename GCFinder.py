num1 = int(input("put your first number (smaller) "))
num2 = int(input("put your second number (bigger) "))
def gcf_finder():
    gcf = 0
    if num1 > num2:
            print("please make sure your first number is smaller than the second... or else")
    for i in range(2, num2):
        if (num1 % i == 0 and num2 % i == 0):
            gcf = i
    print(gcf)
gcf_finder()