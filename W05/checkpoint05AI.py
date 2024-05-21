# Ask the user for two integers
num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))

# Compare the numbers using if/else statements
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

# Ask the user for their favorite animal
favorite_animal = input("What is your favorite animal? ")

# Compare the user's favorite animal with the programmer's favorite animal
programmer_favorite = "bear"
if favorite_animal.lower() == programmer_favorite.lower():
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")