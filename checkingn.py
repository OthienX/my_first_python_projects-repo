class Employee:

    def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.lst_name = last_name



class supervisor(Employee):
    def __init__(self, password):
        super().__init__(first_name, last_name)
        self.password = password 



class chef_employee(Employee):
    def leave_request(self, days):
       return "may i take a leave "+str(days)+ "days"

othieno = Employee("othieno", "o")
ronnie  = chef_employee ("ronnie", "o")
# ronnie = chef_employee("ronnie", "o")

print(ronnie.first_name)