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

    def get_accounts(self):
        for x in self.customer_data:
            self.account_data[x[0]] = x[3:]
        
        return self.account_data
