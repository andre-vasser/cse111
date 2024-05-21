#Ask for numbers Integers
num1 = int(input("What\'s the first number?  "))
num2 = int(input("What\'s the second number?  "))

#compare numbers using if/else statements
if num1 > num2:
    print("The first number is greater")
else:
    print("The first number is not greater") 

if num1 == num2:
    print("The numbers are equal")
else:
    print("The numbers are not equal")
if num2 > num1:
    print("The second number is greater")
else: 
    print("The second number is not greater")
    
#Ask for the favorite animal
favorite_animal = input("What\'s your favorite animal?  ")

#Compare the favorite animal with the programers favorite animal
programmer_favorite = "bear"
if favorite_animal.lower() == programmer_favorite.lower():
    print ("That\'s my favorite animal too! ")
else:
    print ("That\'s not my favorite animal")                      