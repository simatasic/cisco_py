# def badfun(n):
#     raise


# try:
#     badfun(0)
# except:
#     print("What happened? An error?")
# print("The End")

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("I did it again!")
#         raise


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("I see!")

# print("THE END.")

# import math

# x = int(input("Type a number: "))

# try:
#     assert x
#     x = math.sqrt(x)
# except Exception:
#     print("Somethong vent wrong")
# print("end")

#      **LAB**


# def inrange(min, max, n):
#     try:
#         n = int(n)
#         if min < n < max:
#             return n
#         else:
#             raise

#     except ValueError:
#         print("Error: Wrong value!")


# try:
#     print(inrange(-10, 10, input("Type a number within the range: ")))
# except:
#     print(f"Error: the value is not within permitted range ({min}..{max})")

# n = input("n= ")
# n = n / 0
# print(n)
