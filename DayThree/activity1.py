order_count = 0

def take_order(crust, topping):
    global order_count
    order_count += 1
    print("This is takeout no {}. {} Pizza with {}.".format(order_count, crust, topping))

orders = True

while orders == True:
    crust = input("What crust would you like?: ")
    topping = input("what topping would you like?: ")

    take_order(crust, topping)
    another = input("type yes, if you would like another order: ")

    if another.lower() != "yes":
        orders = False
