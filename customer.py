class Customer:

    id = 0
    ssn = 0
    first_name = ""
    last_name = ""
    accounts = {}

    def __init__(self, id, first_name, last_name, ssn):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.ssn = ssn

    #def add_account(self, ssn):
        #self.accounts[""]