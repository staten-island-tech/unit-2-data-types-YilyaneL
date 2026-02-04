def tip_offer():
    bill = float(input("what is your bill "))
    service_quality = input("how was your service (bad, okay, good, or great) ")

    if service_quality == "bad":
        tip = float(bill*0)
        print("you should tip 0%, total tip", tip,"$")
    
    elif service_quality == "okay":
        tip = float(bill*0.15)
        print("you should tip 15%, total tip", tip,"$")
    
    elif service_quality == "good":
        tip = float(bill*0.20)
        print("you should tip 20%, total tip", tip,"$")
    
    elif service_quality == "great":
        tip = float(bill*0.25)
        print("you should tip 25%, total tip", tip,"$")

tip_offer()