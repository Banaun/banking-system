import datetime

class Transaction:

    id = 0
    user_id = 0
    acc_num = 0
    date = 0
    amount = 0

    def __init__(self, user_id, acc_num, amount):
        self.user_id = user_id
        self.acc_num = acc_num
        self.amount = amount
        self.date = datetime.datetime.now()