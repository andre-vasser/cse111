#You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
# which are the store’s slowest sales days. On Tuesday and Wednesday, 
# if a customer’s subtotal is $50 or greater, 
# the store will discount the customer’s subtotal by 10%.
#1 - Your program asks the user for the subtotal but does not ask the user for the day of the week. 
#Your program gets the day of the week from your computer’s operating system.
#2 - Your program correctly computes and prints the discount amount if applicable.
#3 - Your program correctly computes and prints the sales tax amount and the total amount due.
import datetime

current_date_and_time = datetime.datetime.now().weekday()
day_of_week = current_date_and_time.weekday()
#Total = input("Whats the total to pay?    ")

print(day_of_week)
'''def discount(d):
    if datetime.now()
    


