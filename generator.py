# Write a generator evens_upto(n) that yields all even numbers from 0 to n — without building a list.
def evens_upto(n):
    for i in range(n):
        if i % 2 == 0 :
            yield i

even=evens_upto(6)
print(next(even))
print(next(even))
print(next(even))
print(" ")

# Write a generator running_total(numbers) that takes a list and yields the cumulative sum after each number. So [1, 2, 3, 4] → yields 1, 3, 6, 10.
def running_total(numbers):
    count = 0
    for element in numbers:
        count+=element
        yield count
        
nums = [1, 2, 3, 4]
cum = running_total(nums)
print(next(cum))
print(next(cum))
print(next(cum))
print(" ")


num = (x*x for x in range(5))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


#csv reader using generator add with context manager
from contextlib import contextmanager

@contextmanager
def gen( file_path):
	f = open(file_path,'r')
	try : 
		yield f
	finally:
		f.close()
		print("\nClosing file safely...")

with  gen('/home/intercpu009/Downloads/myFile0.csv' ) as f:
	for line in f:
		print(line)