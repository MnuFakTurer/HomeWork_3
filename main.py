# task 1
# v 1
try:
    number_day = int(input("Enter the day of the week number: "))

    if number_day == 1:
        print("Monday")
    elif number_day == 2:
        print("Tuesday")
    elif number_day == 3:
        print("Wednesday")
    elif number_day == 4:
        print("Thursday")
    elif number_day == 5:
        print("Friday")
    elif number_day == 6:
        print("Saturday")
    elif number_day == 7:
        print("Sunday")
    else:
        print("Incorrect action")

# v 2

    match number_day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect action")

except ValueError as error:
    print("Incorrect action")
except Exception as error:
    print(f"Incorrect action{error}")
finally:
    print("End program\n")


# task 1

try:
    equal_number1 = int(input("Enter the first number: "))
    equal_number2 = int(input("Enter the second number: "))

    if equal_number1 == equal_number2:
        print("The entered numbers are equal!")
    elif equal_number1 < equal_number2:
        print(equal_number1, equal_number2)
    else:
        print(equal_number2, equal_number1)

except ValueError as error:
    print("Incorrect action")
except Exception as error:
    print(f"Incorrect action{error}")
finally:
    print("End program\n")
