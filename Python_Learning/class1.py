class Employee:
    def __init__(self, name, salary):
        self.name = name           #public Attribute
        self.__salary = salary     #Private Attribute

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 100000:
            print("Your the Rich earner of Top 5'%' of the world ")
        else:
            print("Your the top 30'%' of the one")
        self.__salary = salary

employee = Employee("Raja", 100000)
print("Employee Name : ", employee.name)
print("Salary Per Month : ", employee.get_salary())
employee.set_salary(100001)
print("Updated salary : ",employee.get_salary())
          