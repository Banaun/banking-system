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
                data.append(line[:3])

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
            #f.write("\n" + new_line)
        
        finally:
            f.close()


            



