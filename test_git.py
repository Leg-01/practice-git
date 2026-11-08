car_price =  int(input("enter car price: "))
if car_price >= 70:
    print ("Classical car")
elif car_price >= 60:
    print ("Expensive car")
elif car_price >= 50:
    print ("Middle Class car")
else:
    print ("Budget")