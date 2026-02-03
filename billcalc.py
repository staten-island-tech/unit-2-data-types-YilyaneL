
def billcalc():
    bill = float(input("put your bill number here "))
    tip = int(input("put your tip percentage "))
    total = (bill + bill*(tip/100))
    print(total)

billcalc()