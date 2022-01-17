from datasource import Datasource

class Bank:

    ds = Datasource()
    customers = []
    customer_data = []
    account_data = {}
    accounts = []

    def _load(self):
        self.customer_data = self.ds.get_all()

    def add_customer(self, first_name, last_name, ssn):

        for customer in self.customer_data:
            if ssn in customer:
                return False
            
        customer_id = int(self.ds.get_last_id()) + 1
        name = first_name + " " + last_name

        self.customer_data.append([customer_id, name, ssn])
        self.ds.add_line(customer_id, name, ssn)
        return True

    def change_customer_name(self, name, ssn):
        for x in self.customers:
            if ssn == x.ssn:
                x.first_name = name.split()[0]
                x.last_name = name.split()[1]
                self.ds.update_line(name, ssn)
                self._load()
                return True

        return False
        
    def remove_customer(self, ssn):
        returned_balance = 0.0
        to_remove = []

        for x in self.customers:
            if ssn == x.ssn:
                index = self.customers.index(x)
                user_id = x.id
                try:
                    self.account_data.pop(user_id)
                except:
                    pass
                self.customers.pop(index)

        for y in self.accounts:
            if user_id == y.user_id:
                to_remove.append(self.accounts.index(y))
                returned_balance += float(y.balance)
                
        for r in reversed(to_remove):
            self.accounts.pop(r)

        self.ds.remove_line(ssn)
        self._load()

        return returned_balance

    def get_accounts_from_data(self):
        for x in self.customer_data:
            self.account_data[x[0]] = x[3:]
        
        return self.account_data
    
    #def get_account(self, user_id):

    #def add_account(self, ssn):

    #def deposit(self, user_id, amount):

    #def withdraw(self, user_id, amount):

    #def close_account(self, user_id):

    #def get_all_transactions_from_account(self, user_id):



