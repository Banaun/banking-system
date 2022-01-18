from bank import Bank

bank = Bank()
bank._load()

#Keep running until user chooses 'Exit'
running = True
while running:
    print("""\nChoose an option:
    
    1. Print all current customers.
    2. Add new customer.
    3. Change customer name.
    4. Delete customer.
    5. Add an account to existing customer.
    6. Print all transactions from specific account.
    7. Exit
    """)

    #User chooses an option
    choice = int(input("Choose an option with the corresponding number: "))

    #Print all current customers
    if choice == 1:
        print()
        print("Name and SSN")
        for x in bank.customers:
            print(x)

    #Add new customer
    elif choice == 2:
        print()
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        ssn = str(input("Enter SSN (8 digits): "))

        if len(ssn) != 8:
            print("Incorrect number of digits.")
        else:
            customer_creation = bank.add_customer(first_name, last_name, ssn)
            if customer_creation:
                print("\nCustomer with SSN {} has been added.".format(ssn))
            else:
                print("\nCustomer with SSN {} already exists.".format(ssn))

    #Change customer name
    elif choice == 3:
        print()
        ssn = str(input("Enter SSN (8 digits): "))
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        
        if bank.change_customer_name(first_name + " " + last_name, ssn):
            print("Customer with SSN {} has been updated.".format(ssn))
        else:
            print("No customer with SSN {}.".format(ssn))

    #Delete customer
    elif choice == 4:
        print()
        ssn = str(input("Enter SSN (8 digits): "))
        if len(ssn) != 8:
            print("Incorrect number of digits.")
        else:
            returned_list = bank.remove_customer(ssn)
            print("\nCustomer with SSN {} has been deleted.".format(ssn))
            if len(returned_list) == 3:
                print("\nDeleted accounts:")
                print(returned_list[0])
                print(returned_list[1])
            elif len(returned_list) == 2:
                print("\nDeleted accounts:")
                print(returned_list[0])
            print("\n${} has been refunded.".format(returned_list[-1]))

    #Add an account to existing customer
    elif choice == 5:
        print()
        ssn = str(input("Enter SSN (8 digits): "))
        if len(ssn) != 8:
            print("Incorrect number of digits.")
        else:
            acc_num = bank.add_account(ssn)
            if acc_num != -1:
                print("Account created with account number {}.".format(acc_num))
            else:
                print("Failed to add account to customer with SSN {}.".format(ssn))

    #Print all transactions from specific account
    elif choice == 6:
        for i in range(len(bank.accounts)):
            print(bank.accounts[i])
    
    #Exit
    elif choice == 7:
        print()
        print("Exiting program...")
        running = False