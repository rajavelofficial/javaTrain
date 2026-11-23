class person:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

emp = person("Ramu", 1000)
print(emp.name, emp._person__salary)  #Not Recomended
        