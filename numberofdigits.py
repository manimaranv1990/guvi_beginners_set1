nu = int(input("Enter Number:"))
nu_old=nu
count=0

while(nu > 0):
    count=count+1
    nu=nu//10
    
print("The Number of digits in the Number: ",count)
