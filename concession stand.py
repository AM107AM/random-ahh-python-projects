print("-------- Vendor mode --------")
snacks = {}
snacks_list = list(snacks)
price_list = []
x = 1  # just a counter during during listing the items
y = 1  # just a counter during inputing the items in vendor mode
while True:
    item = input(f"PLease input the item to sell {y} (q for buyer mode) : ")
    if item.lower() == "q":
        break
    price = input(f"Please input the price of the item {y}: ")
    while True:
        try:
            price = float(price)
            break
        except ValueError:
            price = input("Please select a valid price: ")
    snacks.update({item: price})
    snacks_list = list(snacks)
    price_list = list(snacks.values())
    y += 1

while True:
    while True:
        start = input("please press (s) to start: ")
        if start.lower().replace(" ", "") == "s":
            break
    print("Hello, welcome to the concession stand!")
    print("Current available items are:")
    for snack, price in snacks.items():
        print(
            f"{x}.{snack} : {price} $"
        )  # x is just a counter for the number before the snack
        x += 1
    cart = []
    total = 0

    while True:
        bought_item = input("Please input the number of your snacks (t for total): ")
        if bought_item.lower().strip() == "t":
            break
        while True:
            try:
                bought_item = int(bought_item)
                break
            except ValueError:
                bought_item = input("Please select a valid number: ")

        if int(bought_item) not in range(len(snacks_list) + 1):
            print(f"Please select a number from 1 to {len(snacks_list)}: ")
        else:
            print(f"{snacks_list[int(bought_item) - 1]} has been added")
            cart.append(snacks_list[int(bought_item) - 1])
            total += snacks.get(snacks_list[int(bought_item) - 1])
    bought_set = set(cart)
    #                    idx 0     idx1        idx2      idx3
    # example of cart: ["popcorn", "Popcorn", "Candy", SugarCan juice]
    # the set of cart : {"candy", "Popcorn", "Sugarcane juice"}
    print("---------your items----------")
    for snack in bought_set:
        # ex:      2                 x Popcorn =             2    x                3.50                      $ =              7.00
        print(
            f"{cart.count(snack)} x {snack} = {cart.count(snack)} x {(price_list[snacks_list.index(snack)])} $ = {(price_list[snacks_list.index(snack)] * cart.count(snack))  } $"
        )
    print("-----------------------------")
    print(f"your total is {total} $")
