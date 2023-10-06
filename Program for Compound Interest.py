# Python3 program to find compound
principal = int(input("Enter the principal amount: "))
rate = int(input("Enter rate of interest: "))
time = int(input("Enter time in years: " ))

Amount = principal * ((1+(rate/100))**time)

compound_intrest=Amount-principal

print("Compound Intrest ,",compound_intrest)
