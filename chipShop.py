#chipShop.py
# a program to display the menu with
# prices in a chip shop then increases
# the prices by 20% and then
# displays the menu with new prices again
# D.H. January 2005

# Place in a list the food 
food = ["soup", "chips", "fish", "chicken", "sausage"]

#Place in a parallel list the prices of each item of food

priceOf = [0.90, 1.00, 2.70, 2.40, 1.20]

# Display the price list

print "Item No Item Item Price"
for i in range (5):
    print i+1,food[i],priceOf[i]
print

#increase the prices by 20%
for i in range(5):
    priceIncrease = priceOf[1] * 20/100.0
    priceOf[i] = priceOf[i] + priceIncrease

# display the new prices
print "Prices have increased by 20%"
print
print "Ther new prices are:"
print "Item No Item Item Price"
for i in range(5):
    print i+1,food[i],priceOf[i]
    
    
    
    ----------------------------------------------------------------
    ----------------------------------------------------------------
    
   Traceback (most recent call last):
  File "C:/Program Files/IBM/SPSS/Statistics/25/chipShop.py", line 9, in <module>
    food ["soup", "chips", "fish", "chicken", "sausage"]
NameError: name 'food' is not defined
>>> ================================ RESTART ================================
>>> 
Item No Item Item Price
1 soup 0.9
2 chips 1.0
3 fish 2.7
4 chicken 2.4
5 sausage 1.2

Prices have increased by 20%

Ther new prices are:
Item No Item Item Price
1 soup 1.1
2 chips 1.2
3 fish 2.94
4 chicken 2.64
>>> ================================ RESTART ================================
>>> 
Item No Item Item Price
1 soup 0.9
2 chips 1.0
3 fish 2.7
4 chicken 2.4
5 sausage 1.2

Prices have increased by 20%

Ther new prices are:
Item No Item Item Price
1 soup 1.1
2 chips 1.2
3 fish 2.94
4 chicken 2.64
5 sausage 1.44
>>>  
