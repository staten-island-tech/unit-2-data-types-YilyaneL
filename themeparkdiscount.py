def discount(isMember, age, isResident):
    if age <12 or age >=65 and isResident or isMember:
        print("you get a discount")
    else:
        print("no discount for you bum")

discount(False, 42, True)