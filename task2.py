# Python program to Convert Kilometer to Miles
# logic : 1 km = 0.62137 miles and mile = km * 0.62137

kilometre = float (int(input ("Eenter the speed of car in Kilometre: ")))  
conversion_ratio = 0.621371  
miles = kilometre * conversion_ratio

print ("The speed value of car in Miles: ", miles )
print ("The speed value of car in Miles: ", f'{miles:.2f}') # value in two decimals