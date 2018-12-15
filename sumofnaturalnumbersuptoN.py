nu = int(input("Enter the N Value: "))

nu_old = nu
sum = 0

if nu <= 0: 
   print("Enter a Positive Number!") 

else: 
   while nu > 0:
        sum = sum + nu
        nu = nu - 1;

   print("Sum of first", nu_old, "natural numbers is: ", sum)
