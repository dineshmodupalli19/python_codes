#Python Program to check Armstrong Number

number=int(input("Enter the number :-"))
inputnumber=number
orderN=len(str(number))

digitsum=0
while number!=0:
    digit=number%10
   
    digitsum=digitsum+(digit**orderN)
   

    number=number//10
if inputnumber==digitsum:
    print("True")
else:
    print("False")
