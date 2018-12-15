year = int(input("Enter the Year: "))

if ((year % 400 == 0) or ((year % 4 == 0) and (year%100 != 0))):
    print("{0} is a Leap Year".format(year))
    
else:
    print("%d is Not the Leap Year" %year)
