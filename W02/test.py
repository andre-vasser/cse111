import datetime

today = datetime.datetime.now().weekday()

day_names = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

subtotal = float(input("Enter the subtotal:  "))

if day_names[today] in ["Tuesday" or "Wedesday"] and subtotal >= 50:
    discount = subtotal * 0.1
else:
    discount = 0
    
sales_tax = (subtotal - discount ) * 0.08

total = subtotal - discount + sales_tax

print (f'Subtotal: $ {subtotal:.2f}')
print (f'Discount: $ {discount:.2f}')
print (f'Sales Tax: $ {sales_tax:.2f}')
print (f'Total Amount: $ {total:.2f}')