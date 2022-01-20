class Datasource:

    def datasource_conn(self):
        try:
            f = open("customer_data.txt")
            ds = (True, "Connection successful", "customer_data.txt")
        except:
            ds = (False, "Connection failed", "customer_data.txt")
        finally:
            f.close("customer_data.txt")
        
        return ds
        
    def get_alla(self):
        data = []

        try:
            f = open("customer_data.txt", "r")
            for x in f:
                line = x.strip().split(":")
                data.append(line)
        finally:
            f.close()

        print(data)
        for x in data:
            for y in x:
                print(type(y))
    #Get all lines from file and return list with separated values
    def get_all(self):
        data = []

        try:
            f = open("customer_data.txt", "r")
            for x in f:
                line = x.strip().split(":")
                data.append(line)
        finally:
            f.close()

        return data

    #Get highest id from lines in file
    def get_last_id(self):
        id = []

        try:
            f = open("customer_data.txt", "r")
            for x in f:
                line = x.strip().split(":")
                id.append(line[0])
            last_id = id[-1]
        finally:
            f.close()
        
        return last_id
    
    #Add new line
    def add_line(self, id, name, ssn):
        new_line = str(id) + ":" + name + ":" + str(ssn)

        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close()

        try:
            f = open("customer_data.txt", "a")
            f.write("\n" + new_line)
        finally:
            f.close()

    #Update name in line
    def update_line_name(self, name, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                full_name = line.split(":")[1]
                new_line = line.replace(full_name, name)
                lines[index] = new_line

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()

    #Add account to line
    def update_line_acc(self, account, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close() 

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                lines[index] = line.rstrip("\n")
                lines[index] = lines[index] + account

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()

    #Remove entire line
    def remove_line(self, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if str(ssn) in line:
                index = lines.index(line)
                del lines[index]
  
        lines[len(lines)-1] = lines[len(lines)-1].rstrip("\n")

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()

    #Remove single account from line
    def remove_line_acc(self, acc_num):
        f = open("customer_data.txt", "r")
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
                f = open("customer_data.txt", "w")
                f.writelines(lines)
                f.close()
                return True
        return False
                