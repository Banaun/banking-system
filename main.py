from bank import Bank
from customer import Customer
from account import Account

bank = Bank()
bank._load()

running = True

while running:
    print("""Choose an option:
    
    1. Print all current customers.
    2. Add new customer.
    3. Change customer name.
    4. Delete customer.
    5. Add an account to existing customer.
    6. Print all transactions from specific account.
    7. Exit
    """)

    
    choice = int(input("Choose an option with the corresponding number: "))

    if choice == 1:
        print()
        print("Name and SSN")
        for customer in bank.customers:
            print(customer[1:3])
        print()

    elif choice == 2:
        print()
        first_name = str(input("Enter first name: "))
        last_name = str(input("Enter last name: "))
        ssn = str(input("Enter SSN (8 digits): "))

        if len(ssn) != 8:
            print("Incorrect number of digits.\n")
        else:
            customer_creation = bank.add_customer(first_name, last_name, ssn)
            if customer_creation:
                print("\nCustomer with SSN {} has been added.".format(ssn))
            else:
                print("\nCustomer with SSN {} already exists.".format(ssn))
            print()

    elif choice == 3:
        print()

    elif choice == 4:
        print()

    elif choice == 5:
        print()

    elif choice == 6:
        print()
    
    elif choice == 7:
        print()
        print("Exiting program...")
        running = False
    #except:
        #print()
        #print("Incorrect input.")
        #print()

        