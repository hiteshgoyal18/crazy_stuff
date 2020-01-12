class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def full_name(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "{} {} Employee".format(self.first, self.last)


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, emp_num=None):
        if emp_num is None:
            self.emp_num = []


emp1 = Employee("Hitesh", "Goyal", 50000)
print(emp1.full_name())
