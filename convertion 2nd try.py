print("Hello, welcome to the weight convertion program")
valid_convertions = {"1", "2"}
while True:
    convertion = input("Lbs-->Kgs type:1 / Kgs-->Lbs type:2 : (q to quit)")
    if convertion.lower() == "q":
        break
    while True:
        if convertion not in valid_convertions:
            convertion = input("PLease select a valid convertion: ")
        else:
            break
    if convertion == "1":
        weight_in_lbs = input("Please select a weight in Lbs: ")

        while True:
            try:
                weight_in_lbs = float(weight_in_lbs)
                break
            except ValueError:
                weight_in_lbs = input("Please select a valid number: ")
        resultkg = weight_in_lbs / 2.205
        print(f"{weight_in_lbs:.2f} Lbs = {resultkg:.2f} Kgs")

    if convertion == "2":
        weight_in_kgs = input("Please select a weight in kgs: ")
        while True:
            try:
                weight_in_kgs = float(weight_in_kgs)
                break
            except ValueError:
                weight_in_kgs = input("Please select a valid number: ")
        resultlbs = weight_in_kgs * 2.205
        print(f"{weight_in_kgs:.2f} Kgs = {resultlbs:.2f} Lbs")
