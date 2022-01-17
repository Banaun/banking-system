from bank import Bank
from customer import Customer
from account import Account

#Load all customers
bank = Bank()
bank._load()
for x in bank.customer_data:
    customer = Customer(x[0], x[1].split()[0], x[1].split()[1], x[2])
    bank.customers.append(customer)

#Load all accounts
for x, y in bank.get_accounts().items():
    if len(y) > 3:
        first_account = Account(x, y[0], y[1], y[2].split("#")[0])
        second_account = Account(x, y[2].split("#")[1], y[3], y[4])
        bank.accounts.append(first_account)
        bank.accounts.append(second_account)
    else:
        first_account = Account(x, y[0], y[1], y[2])
        bank.accounts.append(first_account)

#Keep running until user chooses 'Exit'
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

    #User chooses an option
    choice = int(input("Choose an option with the corresponding number: "))

    #Print all current customers
    if choice == 1:
        print()
        print("Name and SSN")
        for customer in bank.customers:
            print(customer)
        print()

    #Add new customer
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
                bank.customers.append(Customer(bank.customer_data[-1][0], first_name, last_name, ssn))
                print("\nCustomer with SSN {} has been added.".format(ssn))
            else:
                print("\nCustomer with SSN {} already exists.".format(ssn))
            print()

    #Change customer name
    elif choice == 3:
        print()

    #Delete customer
    elif choice == 4:
        print()

    #Add an account to existing customer
    elif choice == 5:
        print()

    #Print all transactions from specific account
    elif choice == 6:
        print()
    
    #Exit
    elif choice == 7:
        print()
        print("Exiting program...")
        running = False

    #except:
        #print()
        #print("Incorrect input.")
        #print()

        