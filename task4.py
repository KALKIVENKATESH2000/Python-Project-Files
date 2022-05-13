# Python program to Check Leap year
year = int(input("Enter any year: "))

if year%4 == 0:
    print(year, "is Leap Year")
else:
    print(year, "is Not a Leap Year")
