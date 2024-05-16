#import data
import math
from datetime import datetime

#Dictionary tire prices
tire_prices={
    (185, 50, 14): 99.99,
    (205, 60, 15): 109.99,
      
}

#Call the now() method to get the current
#date and time as a datetime object from
#the computer's operating system.
current_date_and_time = datetime.now()
t_width = int(input('Enter with the tire width: '))
a_ratio = int(input('Enter with the aspect of the radio: '))
d_wheel = int(input('Enter with the diameter of the wheel: '))

#calculus
volume = round((math.pi * (t_width ** 2)) * a_ratio * (t_width * a_ratio + 2540 * d_wheel) / 10000000000, 2)

#print 
print (f"{current_date_and_time:%Y-%m-%d}, {t_width}, {a_ratio}, {d_wheel}, {volume}")

#find tire price
tire_key = (t_width, a_ratio, d_wheel)
if tire_key in tire_prices:
    price = tire_prices[tire_key]
    print (f"The price for tires with these dimentions is ${price:.2f}")
else:
    print("Sorry, we don\'t have pricing information for those tire dimentions.")
    
#Ask if you want buy tires
buy_tires = input("Do you want to buy tires with these dimensions? (yes/no)").lower()
if buy_tires == "yes":
    name = input("Please enter your name")
    phone_number = input('Please enter your phone number: ')
    
    print(f"{current_date_and_time:%Y-%m-%d}, {t_width}, {a_ratio}, {d_wheel}, {volume}, {name}, {phone_number}\n")
    print("Thank you for your interest! We will contact you soon")
else:
    print("Thank you for using our program!")