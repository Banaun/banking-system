class Transaction:

    def __init__(self, user_id, acc_num, amount, date):
        self.user_id = user_id
        self.acc_num = acc_num
        self.amount = amount
        self.date = date

    def __str__(self):
        if self.amount < 0:
            return "\nAccount number: {}\nWithdrawal amount: {}\nDate: {}".format(self.acc_num, self.amount * 1, self.date)
        else:
            return "\nAccount number: {}\nDeposit amount: {}\nDate: {}".format(self.acc_num, self.amount, self.date)