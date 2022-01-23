from bank import Bank

bank = Bank()
bank._load()

def main():
    run_prompt()

def run_prompt():
    running = True
    while(running):
        print("""\nChoose an option:
    
        1. Print all current customers.
        2. Print specific customer.
        3. Add new customer.
        4. Change customer name.
        5. Delete customer.
        6. Add an account to existing customer.
        7. Close account.
        8. Withdraw/Deposit from/to account.
        9. Print all transactions from specific account.
        0. Exit.
        """)

        try:
            choice = int(input("Choose an option with the corresponding number: "))
            if len(str(choice)) != 1:
                print("That's too many numbers, please refrain from using your imagination.")
        except ValueError:
            print("That's not a number, dummy.")

        #Print all current customers
        if choice == 1:
            print("\nName and SSN")
            for x in bank.customers:
                print(x)

        #Print specific customer
        elif choice == 2:
            ssn = ssn_input()
            print(bank.get_customer(ssn))

        #Add new customer
        elif choice == 3:
            first_name = str(input("\nEnter first name: ")).capitalize()
            last_name = str(input("Enter last name: ")).capitalize()
            ssn = ssn_input()
            customer_creation = bank.add_customer(first_name, last_name, ssn)
            if customer_creation:
                print("\nCustomer with SSN {} has been added.".format(ssn))
            else:
                print("\nCustomer with SSN {} already exists.".format(ssn))

        #Change customer name
        elif choice == 4:
            ssn = ssn_input()
            first_name = str(input("Enter first name: ")).capitalize()
            last_name = str(input("Enter last name: ")).capitalize()
            if bank.change_customer_name(first_name + " " + last_name, ssn):
                print("Customer with SSN {} has been updated.".format(ssn))
            else:
                print("No customer with SSN {}.".format(ssn))

        #Delete customer
        elif choice == 5:
            ssn = ssn_input()
            returned_list = bank.remove_customer(ssn)
            if returned_list:
                print("\nCustomer with SSN {} has been deleted.".format(ssn))
                if len(returned_list) == 3:
                    print("\nDeleted accounts:")
                    print(returned_list[0])
                    print(returned_list[1])
                elif len(returned_list) == 2:
                    print("\nDeleted accounts:")
                    print(returned_list[0])
                print("\n${} has been refunded.".format(returned_list[-1]))
            else:
                print("No customer found with SSN {}.".format(ssn))


        #Add an account to existing customer
        elif choice == 6:
            ssn = ssn_input()
            acc_num = bank.add_account(ssn)
            if acc_num != -1:
                print("Account created with account number {}.".format(acc_num))
            else:
                print("No customer found with SSN {} with available account slots.".format(ssn))  

        #Close account
        elif choice == 7:
            ssn = ssn_input()
            acc_num = acc_num_input()
            print(bank.close_account(ssn, acc_num))

        #Withdraw/Deposit
        elif choice == 8:
            print("""
            1. Withdraw from chosen account.
            2. Deposit to chosen account.
            """)

            try:
                w_d_choice = int(input("Choose an option with the corresponding number: "))
                if len(str(w_d_choice)) != 1:
                    print("That's too many numbers, please refrain from using your imagination.")
            except ValueError:
                print("That's not a number, dummy.")
        
            #Withdraw/Deposit from/to account
            if w_d_choice == 1 or 2:
                ssn = ssn_input()
                acc_num = acc_num_input()
                try:
                    amount = float(input("Enter amount: "))
                    if amount > 0:
                        if w_d_choice == 1:
                            if bank.withdraw(ssn, acc_num, amount):
                                print("\n${} withdrawn from account {}.".format(amount, acc_num))
                            else:
                                print("\nWithdrawal declined.")
                        else:
                            if bank.deposit(ssn, acc_num, amount):
                                print("\n${} deposited to account {}.".format(amount, acc_num))
                            else:
                                print("\nDeposit declined.")
                    else:
                        print("You can only withdraw/deposit a positive amount.")

                except ValueError:
                    print("The amount must be specified with numbers only.")

        #Print all transactions from specific account
        elif choice == 9:
            ssn = ssn_input()
            acc_num = acc_num_input()

            returned_transactions = bank.get_all_transactions_from_account(ssn, acc_num)
            if returned_transactions == -1:
                print("Could not print transactions from account number {}.".format(acc_num))
            else:
                for x in returned_transactions:
                    print(x)

        #Exit
        elif choice == 0:
            print("\nExiting program...")
            exit()

def ssn_input():
    try:
        ssn = int(input("\nEnter SSN (8 digits): "))
        while(len(str(ssn)) != 8):
            ssn = int(input("Enter SSN (8 digits): "))
        return ssn     
    except ValueError:
        print("SSN can only contain numbers.")
    return 0

def acc_num_input():
    try:
        acc_num = int(input("Enter account number (4 digits): "))
        while(len(str(acc_num)) != 4):
            acc_num = int(input("Enter account number (4 digits): "))
        return acc_num
    except ValueError:
        print("Account number can only contain numbers.")
    return 0

if __name__ == "__main__":
    main()