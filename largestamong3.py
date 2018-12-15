nu1 = float(input("Enter First Number: "))
nu2 = float(input("Enter Second Number: "))
nu3 = float(input("Enter Third Number: "))

if (nu1 >= nu2) and (nu1 >= nu3):
   largest = nu1
   
elif (nu2 >= nu1) and (nu2 >= nu3):
   largest = nu2
   
else:
   largest = nu3

print("The Largest Number Between", nu1, ",", nu2, "&", nu3,"is",largest)
