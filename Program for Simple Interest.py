#python program for simple intrest

principle_amount=float(input("Enter the principle amount :="))
tenure_time=int(input("Enter the time given :="))
intrest=float(input("Enter the intrest :="))

simple_intrest=(principle_amount*intrest*tenure_time)/100

print("the simple intrest for the principle amount  ",principle_amount,"  for the tenure time of  ",tenure_time,"  with the intrest of ",intrest,"is ",simple_intrest)
