'''> python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 liters'''
#import data
import math

#Enter Data
#tire_width = w
#tire_ratio = a
#wheel_diameter = d
#Volume = v
w = int(input("Enter the width of the tire in mm (ex 205):  "))
a = int(input("Enter the aspect ratio of the tire (ex 60):  "))
d = int(input("Enter the diameter of the wheel in inches (ex 15):  "))

#Calculus

v = round((math.pi * (w ** 2)) * a * (w * a + 2540 * d) / 10000000000, 2)

#Results

print (f"The approximate volume is {v} in liters")