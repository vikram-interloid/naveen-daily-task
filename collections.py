# Average of numbers


count=0

num = int(input("Enter a len of list : "))
# lst = [int(input(f"Enter a {num} of items: ")) for i in range(num)]
for i in range(num):
   item = int(input(f"Enter a {num} of items: "))
   count+=item
   avg = count/num
   
print(avg)


# maximun and minimum in list

lst=[]
num = int(input("Enter a len of list : "))
lst = [int(input(f"Enter a {num} of items: ")) for i in range(num)]

max = lst[0]
min = lst[0]

for i in lst:
    if i > max:
        max = i
    elif i < min:
        min = i
        
print(f"The Maximum is {max} and minimum is {min}")


# reverse a number without built-in 

nums = int(input("Enter a number to reverse : "))

reverse = 0
while nums != 0 :
    digit = nums % 10
    reverse = reverse * 10 + digit
    nums = nums // 10
    
print(reverse)



rows = int(input("Enter a rows : "))

for i in range(1 ,rows + 1):
    print("* " * i)


rows = int(input("Enter a rows : "))

for i in range(rows + 1,0,-1):
    for j in range(0,i-1):
        print("*" ,end=" ")
    print(" ")
 