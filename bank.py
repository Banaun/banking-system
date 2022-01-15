from datasource import Datasource

class Bank:

    ds = Datasource()
    customers = []
    name = "BananaBank"

    def _load(self):
        self.customers = self.ds.get_all()

    def add_customer(self, first_name, last_name, ssn):

        for customer in self.customers:

            if ssn in customer:
                return False

        customer_id = int(self.ds.get_last_id()) + 1
        name = first_name + " " + last_name

        self.customers.append([customer_id, name, ssn])
        self.ds.add_line(customer_id, name, ssn)
        return True