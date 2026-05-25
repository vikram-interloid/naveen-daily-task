Name="Naveen"
print(Name)
a = 45
b = 18

print(f"{a} is bigger than {b}") if a > b else print(f"{b} is bigger") 

def func(fname,/,mname=" ",*,lname):
  print(fname + mname + lname)
  
func("sathasivam",lname="naveen")

  
user =[{
    "name":"naveen",
    "age":24
  }]

def add_user():
      newuser = {
      "name": input("Enter a name : "),
      "age" : int(input("Enter a age : ")) 
      }
      user.append(newuser)
      print("User added succesfully")
    
def view_user():
      print(user)

def delete_user():
      deluser = input("Enter a name to be deleted : ")
      for i in user:
        if i['name'] == deluser:
          user.remove(i)
      print('User deleted successfully')

while True :
  menu = ["Add User","View User","Delete User","Exit"]
  for i,do in enumerate(menu,start=1):
    print(f"{i} . {do}")
  choice=int(input("Enter your choice : "))
  
  if choice == 1 :
    add_user()
  
  elif choice == 2 :
    view_user()
  
  elif choice == 3 :
    delete_user()
  
  elif choice == 4 :
    break

else :
  print("Invalid choice")
  
  
  
  