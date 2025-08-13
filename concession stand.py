snacks = {"Popcorn": 2.5, "Cotton candy": 2.0, "Chips": 2.0, "Candy": 3.0}
snacks_list = ["Popcorn", "Cotton candy", "Chips", "Candy"]
x = 1

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
            print("Please select a valid number")

    if int(bought_item) not in range(1, 5):
        print("Please select a number from 1 to 4")
    elif (
        int(bought_item) == 3
    ):  # another condition so that the grammer is right with chips
        print(f"{snacks_list[int(bought_item) - 1]} have been added")
        cart.append(snacks_list[int(bought_item) - 1])
        total += snacks.get(snacks_list[int(bought_item) - 1])
    else:
        print(f"{snacks_list[int(bought_item) - 1]} has been added")
        cart.append(snacks_list[int(bought_item) - 1])
        total += snacks.get(snacks_list[int(bought_item) - 1])
bought_set = set(cart)

print("---------your items----------")
for snack in bought_set:
    print(f"{cart.count(snack)} x {snack}")
print("-----------------------------")
print(f"your total is {total} $")
