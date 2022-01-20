from datasource import Datasource
from customer import Customer
from account import Account

class Bank:

    ds = Datasource()
    customers = []
    customer_data = []
    account_data = {}
    accounts = []

    def _load(self):
        self.customer_data = self.ds.get_all()

        #Load all customers
        for x in self.customer_data:
            try:
                customer = Customer(x[0], x[1].split()[0], x[1].split()[1], x[2])
                self.customers.append(customer)
            except:
                print("Something went wrong when loading {}.".format(x))

        #Load all accounts
        for y in self.customer_data:
            self.account_data[y[0]] = y[3:]

        for x, y in self.account_data.items():
            if len(y) > 3:
                first_account = Account(x, y[0], y[1], y[2].split("#")[0])
                second_account = Account(x, y[2].split("#")[1], y[3], y[4])
                self.accounts.append(first_account)
                self.accounts.append(second_account)
            elif len(y) == 3:
                first_account = Account(x, y[0], y[1], y[2])
                self.accounts.append(first_account)
            else:
                pass

    def add_customer(self, first_name, last_name, ssn):

        for customer in self.customer_data:
            if str(ssn) in customer:
                return False
            
        customer_id = int(self.ds.get_last_id()) + 1
        name = first_name + " " + last_name

        self.customer_data.append([customer_id, name, ssn])
        self.customers.append(Customer(customer_id, first_name, last_name, ssn))
        self.ds.add_line(customer_id, name, ssn)
        return True

    def add_account(self, ssn):
        account_temp = []
        user_id = 0
        acc_num = int(self.accounts[-1].acc_num) + 1
        acc_type = "debit account"
        acc_balance = 0.0

        for x in self.customers:
            if str(ssn) == x.ssn:
                user_id = x.id

        for y in self.accounts:
            if user_id == y.user_id:
                account_temp.append(y)
        
        if len(account_temp) == 2:
            return -1
        elif len(account_temp) == 1:
            acc = "#" + str(acc_num) + ":" + acc_type + ":" + str(acc_balance) + "\n"
            new_acc = Account(user_id, acc_num, acc_type, acc_balance)
            self.accounts.append(new_acc)
            self.ds.update_line_acc(acc, ssn)
            return acc_num
        else:
            acc = ":" + str(acc_num) + ":" + acc_type + ":" + str(acc_balance) + "\n"
            new_acc = Account(user_id, acc_num, acc_type, acc_balance)
            self.accounts.append(new_acc)
            self.ds.update_line_acc(acc, ssn)
            return acc_num

    def change_customer_name(self, name, ssn):
        for x in self.customers:
            if str(ssn) == x.ssn:
                x.first_name = name.split()[0]
                x.last_name = name.split()[1]
                self.ds.update_line_name(name, ssn)
                self.customer_data = self.ds.get_all()
                return True
        return False
        
    def remove_customer(self, ssn):
        returned_balance = 0.0
        to_remove = []
        to_return = []

        for x in self.customers:
            if str(ssn) == x.ssn:
                index = self.customers.index(x)
                user_id = x.id
                try:
                    self.account_data.pop(user_id)
                except:
                    pass
                self.customers.pop(index)

        for y in self.accounts:
            if user_id == y.user_id:
                to_return.append(y)
                to_remove.append(self.accounts.index(y))
                returned_balance += float(y.balance)
                
        for r in reversed(to_remove):
            self.accounts.pop(r)

        self.ds.remove_line(ssn)
        self.customer_data = self.ds.get_all()
        
        to_return.append(returned_balance)
        return to_return

    def get_customer(self, ssn):
        returned_list = []

        for x in self.customers:
            if str(ssn) == x.ssn:
                returned_list.append(x.first_name + " " + x.last_name)
                returned_list.append(x.ssn)
            
                for y in self.accounts:
                    if x.id == y.user_id:
                        account = "Account number: " + str(y.acc_num) + ", Balance: " + str(y.balance)
                        returned_list.append(account)
                
                return returned_list
            
        return "\nNo customer found with SSN {}".format(ssn)
    
    def get_account(self, ssn, acc_num):
        for x in self.customers:
            if str(ssn) == x.ssn:
                for y in self.accounts:
                    if str(acc_num) == y.acc_num:
                        return "\nAccount number: {}\nBalance: {}\nAccount type: {}".format(acc_num, y.balance, y.acc_type)
                return "\nNo account found with account number {}.".format(acc_num)
        return "\nNo customer found with SSN {}".format(ssn)

    def close_account(self, ssn, acc_num):
        to_remove = []
        returned_balance = 0

        for x in self.customers:
            if str(ssn) == x.ssn:
                for y in self.accounts:
                    if str(acc_num) == y.acc_num:
                        returned_balance = y.balance
                        self.account_data.pop(x.id)
                        to_remove.append(self.accounts.index(y))
                if not to_remove:
                    return "\nNo account found with Account number {}.".format(acc_num)
                else:
                    for r in to_remove:
                        self.accounts.pop(r)
                        return "\nAccount closed. ${} refunded.".format(returned_balance)
        return "\nNo customer found with SSN {}".format(ssn)
        
    def deposit(self, user_id, amount):
        print("hej")

    #def withdraw(self, user_id, amount):

    #def get_all_transactions_from_account(self, user_id):