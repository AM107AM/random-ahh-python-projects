print("Hello, welcome to probably the worst calculator app ever.")

operation = ""
valid_operations = {"x", "+", "-", "/", "^", ""}
while True:
    while True:
        first_number = input("Please select your first number:")
        try:
            first_number = float(first_number)
            break
        except ValueError:
            print("invalid number")
    while operation == "":
        operation = input("please select an operation (X + - / ^):").strip().lower()

    while operation not in valid_operations:
        print("Invalid operation")
        operation = input("please select a valid operation(X + - / ^):").strip().lower()

    while True:
        second_number = input("Please select your second number:")
        try:
            second_number = float(second_number)
            break
        except ValueError:
            print("invalid number")

    if operation.strip().lower() == "x":
        result = float(first_number) * float(second_number)
    elif operation == "+":
        result = float(first_number) + float(second_number)
    elif operation == "-":
        result = float(first_number) - float(second_number)
    elif operation == "^":
        result = float(first_number) ** float(second_number)
    elif operation == "/":
        result = float(first_number) / float(second_number)

    print("result is:" + str(result).removesuffix(".0"))
    first_number = ""
    second_number = ""
    operation = ""
