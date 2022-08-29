'''
@author: Jordin Kolman
@date: 08/28/2022
@Purpose: basic program comparing minimum price to price list
'''

def minPrice():
    count = 0
    sum = 0

    print("Welcome User")
    name = input("Please enter your full name: ")
    min_price = float(input("Please enter your minimum price: "))

    price_list = [72.1, 94.5, 67.4, 83.0, 99.8, 78.2, 99.9, 77.7, 92.1, 81.6]

    for price in price_list:
        sum = price + sum
        if price > min_price:
            count += 1
    
    print("Hello", name, "the minimum price is", min_price)
    print("There are", count, "prices greater than the minimum price")
    print("The total price is", sum)

minPrice()
