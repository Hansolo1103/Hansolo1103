class Salary():
    def __init__(self,pay,reward):

        self.pay= pay
        self.reward=reward
    def annual_salary(self):
        return (self.pay*12) + self.reward


class Employee:
    def __init__(self,name,pos,pay,reward):
        self.name=name
        self.pos=pos
        self.finsal = Salary(pay,reward)

    def final_salary(self):
        self.finsal.annual_salary()
emp = Employee("sarang","chutiya jugaadu",1000000,100000)
print(emp.final_salary())