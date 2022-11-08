# Multiplication table
def table():
    user = int(input("Num : "))
    i = 0
    go_to = int(input("To which step : "))
    while i != go_to:
        i += 1
        print(f"{user} * {i} = {user * i}")

    print("Program Ended...")


table()


def use_again():
    again = " "
    while again != "n":
        again = input("Do you want to use again ? (y/n) : ").lower()
        if again == "y":
            table()

    print("You have exited.")


use_again()

