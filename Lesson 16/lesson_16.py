class Worker:

    def __init__(self, salary):
        self.salary = salary

    def work(self):
        pass

    def get_salary(self):
        pass

class Doctor(Worker):

    __categories = {'intern': 1.1, 'middle': 1.2, 'highest': 1.5}

    def __init__(self, salary, category):
        super().__init__(salary)
        self.category = category

    def work(self):
        return 'Heal'

    def get_salary(self):
        try:
            return self.salary * Doctor.__categories[self.category]
        except KeyError:
            raise ValueError("Category is not valid")

class Teacher(Worker):

    def __init__(self, salary, experi):
        super().__init__(salary)
        self.experi = experi

    def work(self):
        return 'Teach'

    def get_salary(self):
        if not isinstance(self.experi, int):
            return "Experi is not valid"


doctor_1 = Doctor(500, 'midle')
print(doctor_1.get_salary())


