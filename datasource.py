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
    
    def add_line(self, id, name, ssn):
        new_line = str(id) + ":" + name + ":" + str(ssn)

        try:
            f = open("customer_data.txt", "a")
            f.write("\n" + new_line)
        
        finally:
            f.close()

    def update_line_name(self, name, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if ssn in line:
                index = lines.index(line)
                full_name = line.split(":")[1]
                new_line = line.replace(full_name, name)
                lines[index] = new_line

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()

    def update_line_acc(self, account, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close() 

        for line in lines:
            if ssn in line:
                index = lines.index(line)
                lines[index] = line.rstrip("\n")
                lines[index] = lines[index] + account

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()

    #def update_line_acc_remove(self, account, ssn):

    def remove_line(self, ssn):
        f = open("customer_data.txt", "r")
        lines = f.readlines()
        f.close()

        for line in lines:
            if ssn in line:
                index = lines.index(line)
                del lines[index]
  
        lines[len(lines)-1] = lines[len(lines)-1].rstrip("\n")

        f = open("customer_data.txt", "w")
        f.writelines(lines)
        f.close()