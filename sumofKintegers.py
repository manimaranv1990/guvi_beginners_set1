mylist=[]
n=int(input("Enter N value: "))
k=int(input("Enter K value: "))
sum=0

for i in range(n):
    mylist.append(int(input("Enter the Number {0}: ".format(i+1))))

for i in range(k):
    sum = sum + mylist[i]

print(sum)
