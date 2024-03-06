pay = 0
due = 50
while due > 0:
    pay = int(input("Insert Coin: "))
    if pay == 25 or pay == 10 or pay == 5:
        due -= pay
        if due > 0:
            print(f"Amount Due: {due}")
        if due <= 0:
            print(f"Change Owed: {due * -1}")
    else:
        print(f"Amount Due: {due}")