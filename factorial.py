# input number as int
numb = int(input("Enter Number: "))

# factorial container
fact = 1

# loop for calculating factorial
for i in range(1, numb + 1):
    fact = fact * i

# print output to screen
print("Factorial is : ", fact)

