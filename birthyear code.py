current_year = int(input("what year is it?"))
age = int(input("How old are you?"))
birthday_this_year = input("Did you have your birthday this year (true or false)")

if birthday_this_year.lower().strip() == "true":
    print("you were born in " + str(current_year - age) + ".")
elif birthday_this_year.lower() == "false":
    print("you were born in " + str(current_year - age - 1) + ".")
