#input number as int
numb=int(input("Enter Number: "))

#make coppy number of input variable

copy_numb=numb

#result container
arm=0
rem=0

#ID armstrong number
while numb !=0:
     rem=numb%10
     arm=arm+int(pow(rem,3))
     numb=int(numb/10)


#Print output
if(arm==copy_numb):
    print("Armstrong")
else:
    print("Not Armstrong")


