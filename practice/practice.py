#%% CLASSES AND INSTANCeS (allow to group data)
import datetime
class Employee:
    num_of_emps=0
    raise_amt= 1.04
    def __init__(self, first, last, pay): #u can call 'self' anything but it is convention to call it self
        self.first= first
        self.last= last
        self.pay = pay
        self.email= first + '.' + last + '@company.com'
        Employee.num_of_emps+=1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amt)  #increase salary by 4%
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt= amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay= emp_str.split('-')
        return cls(first, last ,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True
emp_1=Employee(' RIshabh',' agrawal', 40000)
emp_2=Employee(' test','  user', 30000)#  pass in values right here ....__init__ behaves like a regular function
'''print(emp_1) 
print(emp_2) #observations: both are instances of employee class and both have different memory locations but the same class

emp_1.first = 'Rishabh'
emp_1.last = 'Agrawal'
emp_1.email = 'Rishabh.Agrawal@gmail.com'
emp_1.pay = 500000

emp_2.first = 'test'
emp_2.last= 'user'
emp_2.email= 'test.user@gmail.com'
emp_2.pay= 60000
print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last)) #prints full name but this is lengthy

print(emp_1.fullname()) #better method , aruguement automatically gets passed

#OR

Employee.fullname(emp_1)''' #can be saved in variable, we have to pass an arguement

'''print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)# this only does 4% but we will need to access raise amount
# so we create raise amount class variable
print(emp_1.raise_amt)
print(emp_1.__dict__) #observation: raise amount is not present in emp_1.dict

#to change raise amount
Employee.raise_amt=1.05 #changes the raise amount value for every instance ie emp_1 emp_2
#but if we say emp_1.raise_amount=1.05 it only modifies emp_1 ka raise amount'''
# ANOTHER METHOD TO MAKE EMPLOYEE

emp_str_1='JOHN-DOE-70000'
'''emp_str_2='STEVE-SMITH-90000'
emp_str_3='JANE-DOE-990000'
first, last, pay= emp_str_1.split('-')
new_emp_1= Employee(first, last ,pay)
print(new_emp_1.__dict__)# but this is too many lines so we will make a function for it'''

new_emp_1= Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)

my_date= datetime.date(2016,7,11)
print(Employee.is_workday(my_date))# because every weekday is working
