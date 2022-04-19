from hidden import *


def atm():
    attempts = 3
    using_service = False

    print("Please enter your pincode, or enter q to quit:")
    while not using_service:
        pin = input("--->: ")
        print("----" * 8)
        if pin.isdigit():
            if len(pin) != 4:
                print("Invalid input. Only 4 digits is allowed")
                continue
            else:
                if pin != str(pincode):
                    attempts -= 1
                    if attempts < 1:
                        print("Access denied, Your pin card has been blocked")
                    else:
                        print(f"Try again, you have {attempts} attempts")
                        continue
                else:
                    service(amount, using_service)
        elif "q" in pin.lower():
            print("Process has been stopped. Thank you for coming")
            break
        else:
            print("Invalid input. Only digits or q key (to stop the process) are allowed")
            continue
        using_service = True


def service(budget, current_service):
    insufficient = False
    print(f"Select a number and press enter to proceed:")
    print("----" * 8)
    print("option 1: Withdraw\n"
          "option 2: Deposit\n"
          "option 3: Check amount\n"
          "option 4: Quit")
    selection_input(budget, insufficient, current_service)


def selection_input(budget, insufficient, current_service):
    while not current_service:
        try:
            selection = int(input('--->: '))
            if selection == 1:
                # Run func check_amount
                check_amount(budget, insufficient, current_service)
            elif selection == 2:
                try:
                    amount_val = int(input("How much would you like to deposit: "))
                    budget += amount_val
                    print(f"You have deposit {amount_val}. The current amount is {budget} euro")
                    current_service = True
                except ValueError:
                    print("Invalid input, please use digits ony")
                    continue
            elif selection == 3:
                yes = "Y"
                no = "N"

                print(f"The current amount of money is:\n"
                      f" \n"
                      f"{budget} euro.\n")
                print("Would you like to proceed?\nWrite down \"Y\" for yes or \"N\" for no.")
                while not current_service:
                    answer = input("-->: ")
                    if yes.lower() in answer:
                        service(budget, current_service)
                    elif no.lower() in answer:
                        print("Process has been stopped. Thank you for coming")
                        current_service = True
                    else:
                        if len(str(answer)) > 1:
                            print("Invalid input. Only one digit between 1 or 5 is allowed\n"
                                  "\n"
                                  "Please try again")
                            continue
                        if answer is not yes or no:
                            print("Invalid input. Only one digit between 1 or 5 is allowed\n"
                                  "\n"
                                  "Please try again")
                            continue
            elif selection == 4:
                print("Process has been stopped. Thank you for coming")
                current_service = True
            else:
                print("Invalid input. Please enter a number between 1 and 5")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5")
            continue


def check_amount(budget, insufficient, current_service):
    print("How much would you like too withdraw")
    while not insufficient:
        print("----" * 9)
        amount_val = int(input("--->: "))

        if amount_val > budget:
            print(f"Insufficient amount please choose lower than or equal as {budget}")
            continue
        else:
            receipt(amount_val, current_service)
            current_service = True
        insufficient = True


def receipt(budget, current_service):
    print("Would you like to receive a receipt?")
    while not current_service:
        print_receipt = input("Fill in Y for Yes or N for No: ").lower()
        print("----" * 8)
        if len(print_receipt) > 2:
            print("Invalid")
            continue
        else:
            if "y" in print_receipt:
                print(f"Receipt has been printed. You have withdrawn {budget} euro's\n"
                      f"\n"
                      f"Have a nice day")
            elif "n" in print_receipt:
                print(f"Receipt has been printed. You have withdrawn {budget} euro's\n"
                      f"\n"
                      f"Have a nice day")
            else:
                print("Invalid")
                continue
        current_service = True


atm()
