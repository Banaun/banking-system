from bank import Bank

bank = Bank()
bank._load()

#Keep running until user chooses 'Exit'
running = True
while running:
    print("""\nChoose an option:
    
    1. Print all current customers.
    2. Print specific customer.
    3. Add new customer.
    4. Change customer name.
    5. Delete customer.
    6. Add an account to existing customer.
    7. Close account.
    8. Print all transactions from specific account.
    9. Exit
    """)

    allowedNumbers = '12345678'

    #User chooses an option
    try:
        choice = int(input("Choose an option with the corresponding number: "))
        if len(str(choice)) != 1:
            print("That's too many numbers, please refrain from using your imagination.")
        elif str(choice) not in allowedNumbers:
            print("You had to pick a number that's not represented... Please read before you write.")
    except ValueError:
        print("That's not a number, dummy.")
    #Print all current customers
    if choice == 1:
        print("\nName and SSN")
        for x in bank.customers:
            print(x)

    #Print specific customer
    elif choice == 2:
        try:
            ssn = int(input("\nEnter SSN (8 digits): "))
            while(len(str(ssn)) != 8):
                ssn = int(input("Enter SSN (8 digits): "))
            try:
                acc_num = int(input("Enter account number (4 digits): "))
                while(len(str(acc_num)) != 4):
                    acc_num = int(input("Enter account number (4 digits): "))
            
                print(bank.get_account(ssn, acc_num))

            except ValueError:
                print("Account number can only contain numbers.")
            
        except ValueError:
            print("SSN can only contain numbers.")

    #Add new customer
    elif choice == 3:
        first_name = str(input("\nEnter first name: ")).capitalize()
        last_name = str(input("Enter last name: ")).capitalize()
        try:
            ssn = int(input("Enter SSN (8 digits): "))
            if len(str(ssn)) != 8:
                print("Incorrect number of digits.")
            else:
                customer_creation = bank.add_customer(first_name, last_name, str(ssn))
                if customer_creation:
                    print("\nCustomer with SSN {} has been added.".format(ssn))
                else:
                    print("\nCustomer with SSN {} already exists.".format(ssn))

        except ValueError:
            print("SSN can only contain numbers.")

    #Change customer name
    elif choice == 4:
        try:
            ssn = int(input("\nEnter SSN (8 digits): "))
            while(len(str(ssn)) != 8):
                ssn = int(input("Enter SSN (8 digits): "))

            first_name = str(input("Enter first name: ")).capitalize()
            last_name = str(input("Enter last name: ")).capitalize()
        
            if bank.change_customer_name(first_name + " " + last_name, str(ssn)):
                print("Customer with SSN {} has been updated.".format(ssn))
            else:
                print("No customer with SSN {}.".format(ssn))
        except ValueError:
            print("SSN can only contain numbers.")

    #Delete customer
    elif choice == 5:
        try:
            ssn = int(input("\nEnter SSN (8 digits): "))
            while(len(str(ssn)) != 8):
                ssn = int(input("Enter SSN (8 digits): "))
            
            returned_list = bank.remove_customer(str(ssn))
            print("\nCustomer with SSN {} has been deleted.".format(ssn))
            if len(returned_list) == 3:
                print("\nDeleted accounts:")
                print(returned_list[0])
                print(returned_list[1])
            elif len(returned_list) == 2:
                print("\nDeleted accounts:")
                print(returned_list[0])
            print("\n${} has been refunded.".format(returned_list[-1]))
        except ValueError:
            print("SSN can only contain numbers.")

    #Add an account to existing customer
    elif choice == 6:
        try:
            ssn = int(input("\nEnter SSN (8 digits): "))
            while(len(str(ssn)) != 8):
                ssn = int(input("Enter SSN (8 digits): "))

            acc_num = bank.add_account(str(ssn))
            if acc_num != -1:
                print("Account created with account number {}.".format(acc_num))
            else:
                print("Failed to add account to customer with SSN {}.".format(ssn))
        except ValueError:
            print("SSN can only contain numbers.")   

    #Close account
    elif choice == 7:
        try:
            ssn = int(input("\nEnter SSN (8 digits): "))
            while(len(str(ssn)) != 8):
                ssn = int(input("Enter SSN (8 digits): "))

            try:
                acc_num = int(input("Enter account number (4 digits): "))
                while(len(str(acc_num)) != 4):
                    acc_num = int(input("Enter account number (4 digits): "))
                
                print(bank.close_account(str(ssn), str(acc_num)))

            except ValueError:
                print("Account number can only contain numbers.")
        except ValueError:
            print("SSN can only contain numbers.")

    #Print all transactions from specific account
    elif choice == 8:
        ssn = int(input("\nEnter SSN (8 digits): "))
        acc_num = int(input("Enter Account number: "))
        print(bank.close_account(str(ssn), str(acc_num)))
    
    #Exit
    elif choice == 9:
        print()
        print("Exiting program...")
        running = False