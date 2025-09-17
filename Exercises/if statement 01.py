# #------------Exercise1---------
# num= int(input("skriv ett tal"))

# if num < 0:
#     print("its negative")
# elif num > 0:
#     print("its positive")
# else:
#     print("its 0")

# #--------------Exercise2-----------

# a =int(input())
# b =int(input())

# if a > b:
#     print("a is bigger")
# else:
#     print("b is bigger")

# #--------------Exercise3-----------


# a = int(input())
# b = int(input())
# c = int(input())

# if a + b + c == 180 and a == 90 or b == 90 or c == 90:
#     print("u have a right angled triangle")
# elif a + b + c == 180:
#     print("u made a triangle")
# else:
#     print("error")

# #--------------Exercise4-----------


# weight = int(input("skriv din vikt"))
# age = int(input("din ålder"))

# if age > 12 and weight > 40:
#     print("1 to 2 pillz")
# elif 12 > age > 7 and 40 > weight > 26:
#     print("½ to 1 pillz")
# else:
#     print("½ pill")


# #--------------Exercise5-----------

# num = int(input("nummer tak"))

# if num % 5 == 0 and num % 2 != 0:
#     print("number is odd and dev by 5")
# elif num % 5 == 0 and num % 2 == 0:
#     print("number is dev by 5 and even")
# elif num % 2 == 0:
#     print("number is even")


# # The maximum allowed luggage size for boarding an airplane is:
# # weight: 8kg 
# # dimensions: 55x40x23cm (length x width x height)
# # Let the user input weight, length, width and height of the luggage.
# # The program should check if the luggage is allowed or not.


# max_length = 55
# max_width = 40
# max_height = 23
# max_weight = 8


# ulength = int(input("Enter your luggage length (cm): "))
# uwidth = int(input("Enter your luggage width (cm): "))
# uheight = int(input("Enter your luggage height (cm): "))
# uweight = float(input("Enter your luggage weight (kg): "))

# if ulength <= max_length and uwidth <= max_width and uheight <= max_height and uweight <= max_weight:
#     print("Luggage is allowed.")
# else:
#     print("Luggage is NOT allowed.")
    