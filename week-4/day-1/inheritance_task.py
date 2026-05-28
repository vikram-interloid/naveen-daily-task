class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Contact(Person):
    def __init__(self,name,age, email,salary):
        super().__init__(name,age)
        self.email = email
        self.salary = salary

    def __str__(self):
        return f'Name : {self.name} , Age : {self.age} , Email : {self.email} , Salary : {self.salary}'
    
    def __repr__(self):
        return f'Name : {self.name} , Email : {self.email}'
    
    def __lt__(self,others):
        return self.salary < others.salary


# # %%
# class Customer(Contact):
#     def __init__(self):
#         super().__init__()
        
c1 = Contact("Naveen",24,"sparrow@gmail.com",20000)
c2 = Contact("Vikram",25,"vikram@gmail.com",50000)



print(c1.__dict__)
print(c2.__dict__)
print(c2 < c1.salary)


# %%
