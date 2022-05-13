number = int(input("Enter any value: "))
'''
if number>1:
    for i in range(2, number):
        if (number % i) == 0: 
            print(number, "is not a prime number")
        else:
            print(number, "is prime number")
            break
else:
     print(number, "is not a prime number")
    
'''
if number%2 ==0:
    print("not prime number")

else:
    print("prime number")