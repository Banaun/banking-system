class Datasource:

    file_customers = "customer_data.txt"
    file_transactions = "transactions_data.txt"

    def datasource_conn(self):
        try:
            f = open(self.file_customers)
            ds = (True, "Connection successful", self.file_customers)
        except:
            ds = (False, "Connection failed", self.file_customers)
        finally:
            f.close(self.file_customers)
        
        return ds

    #Get all lines from customers file and return list with separated values
    def get_all_customers(self):
        data = []

        try:
            f = open(self.file_customers, "r")
            for x in f:
                line = x.strip().split(":")
                data.append(line)
        finally:
            f.close()

        return data

    #Get all lines from transactions file and return list with separated values
    def get_all_transactions(self):
        data = []

        try:
            f = open(self.file_transactions, "r")
            for x in f:
                line = x.strip().split("#")
                data.append(line)
        finally:
            f.close()

        return data

    #Get highest id from lines in customers file
    def get_last_id(self):
        id = []

        try:
            f = open(self.file_customers, "r")
            for x in f:
                line = x.strip().split(":")
                id.append(line[0])
            last_id = id[-1]
        finally:
            f.close()
        
        return last_id
    
    #Add new line in customers file
    def add_line_customers(self, id, name, ssn):
        new_line = str(id) + ":" + name + ":" + str(ssn)

        try:
            f = open(self.file_customers, "a")
            f.write("\n" + new_line)
        finally:
            f.close()

    #Update name in customers file
    def update_line_name(self, name, ssn):
        f = open(self.file_customers, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                full_name = line.split(":")[1]
                new_line = line.replace(full_name, name)
                lines[index] = new_line

        f = open(self.file_customers, "w")
        f.writelines(lines)
        f.close()

    #Add account to line in customers file
    def update_line_acc(self, account, ssn):
        f = open(self.file_customers, "r")
        lines = f.readlines()
        f.close() 

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                lines[index] = line.rstrip("\n")
                lines[index] = lines[index] + account

        f = open(self.file_customers, "w")
        f.writelines(lines)
        f.close()

    def update_line_transaction(self, acc_num, amount):
        f = open(self.file_customers, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(acc_num) in line:
                index = lines.index(line)
                if line.split(":")[3] == str(acc_num):
                    if "#" in line:
                        current_amount = float(line.split(":")[5].split("#")[0])
                        current_amount += amount
                        new_line = line.replace(line.split(":")[5], str(current_amount) + "#" + line.split(":")[5].split("#")[1])
                        lines[index] = new_line
                    else:
                        current_amount = float(line.split(":")[5])
                        current_amount += amount
                        new_line = line.replace(line.split(":")[5], str(current_amount))
                        if line != lines[-1]:
                            new_line += "\n"
                        lines[index] = new_line
                elif line.split(":")[5].split("#")[1] == str(acc_num):
                    current_amount = float(line.split(":")[-1])
                    current_amount += amount
                    new_line = line.replace(line.split(":")[-1], str(current_amount))
                    if line != lines[-1]:
                        new_line += "\n"
                    lines[index] = new_line

        f = open(self.file_customers, "w")
        f.writelines(lines)
        f.close()

    #Remove entire line in customers file
    def remove_line(self, ssn):
        f = open(self.file_customers, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                del lines[index]
  
        lines[len(lines)-1] = lines[len(lines)-1].rstrip("\n")

        f = open(self.file_customers, "w")
        f.writelines(lines)
        f.close()

    #Remove single account from line in customers file
    def remove_line_acc(self, acc_num):
        f = open(self.file_customers, "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(acc_num) in line:
                index = lines.index(line)
                if "#" in line:
                    customer_info = line.strip().split("#")[0].split(":")[:3]
                    first_acc = line.strip().split("#")[0].split(":")[3:]
                    second_acc = line.strip().split("#")[1].split(":")

                    new_line_customer = customer_info[0] + ":" + customer_info[1] + ":" + customer_info[2]
                    
                    if str(acc_num) not in first_acc:
                        new_line_acc = ":" + first_acc[0] + ":" + first_acc[1] + ":" + first_acc[2]
                    else:
                        new_line_acc = ":" + second_acc[0] + ":" + second_acc[1] + ":" + second_acc[2]
                    new_line = new_line_customer + new_line_acc

                else:
                    customer_info = line.strip().split(":")[:3]
                    new_line = customer_info[0] + ":" + customer_info[1] + ":" + customer_info[2]
                
                if line != lines[-1]:
                    new_line += "\n"
                    
                lines[index] = new_line
                f = open(self.file_customers, "w")
                f.writelines(lines)
                f.close()
                return True
        return False
                
    def add_line_transactions(self, user_id, acc_num, amount, date):
        new_line = str(user_id) + "#" + str(acc_num) + "#" + str(amount) + "#" + str(date)

        try:
            f = open(self.file_transactions, "a")
            f.write("\n" + new_line)
        finally:
            f.close()