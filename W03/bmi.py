#import Datetime used to compute person's age
from datetime import datetime
#get user's gender, birthday, height, and weight
#call the compute_age, kg_from_lb, cm_from_in, 
#body_mass_index, basal_metabolic_rate
#print the result
def main():
    gender = input("What\'s your gender? ")
    birth_str = input("What\'s your birth? YYYY-mm-dd")
    pounds = float(input("How many pounds do you have? "))
    inches = float(input("What\'s your heigh in inches? "))
    
    years = compute_age(birth_str)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, years)
 
    
    print (f"Age (years): {years}")
    print (f"Weight (kg): {kg:.2f}")
    print (f"Height (cm): {cm:.1f}")
    print (f"Body mass index: {bmi:.2f}")
    print (f"Basal metabolic rate (Kcal/day) {bmr:.0f}")


"""Compute and return person's age in years.
Parameter birth_str: a person birthday sotred as a string in this format: YYYY-MM-DD
return: A person's age in Years"""
#convert a persons birthday from a string to a date object
def compute_age(birth_str): 
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")  
    today = datetime.now()
#Compute the difference between today and the person's birthday in years
    years = today.year - birthdate.year
#If necessary, subtract one from the difference
  
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
        birthdate.day > today.day):
        years -=1
    return years
    
"""Convert mass in pounds to kg 
Parameter: pounds: 
Return: The mass in Kg"""
def kg_from_lb(pounds):
    kg =  pounds * 0.45359237
    return kg
    
"""Convert lenght in inches to centimeters
Parameter: inches: a lenght in inches
Return: the lenght in centimeters"""
def cm_from_in(inches):
    cm = inches * 2.54
    return cm
"""Compute return a person's body mass index
Parameters 
weight: a person's weight in Kg
height: a person's height in centimeters"""  

def body_mass_index(weight, height):
    bmi = weight / (height) ** 2 * 10000
    return bmi

"""Compute and return a persons basal metabolic rate
Parameters: 
weight: a person's weight in Kg
height: a person height in cm
age: a person's age in years
Return: a person's basal metabolic rate in kcals per day"""
def basal_metabolic_rate(gender, weight, height, age):
    if gender.upper() =="F":
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330
    else:
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    return bmr
main()
        