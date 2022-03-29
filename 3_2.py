# grade=90
# condition= grade>=90
# if condition:
#     print("Your grade is A")
# else:
#     print("Your grade is not A")


# num1=input("Enter the first number:")
# num2=input("Enter the second number:")
# print("1", num1, "2", num2)

# # print(isinstance(num1,int))

# if isinstance(num1, str)
#     print("Data type not allowed! Please specify a numerical value")

# if num1>num2:
#     largerVal=num1
# else:
#     largerVal=num2
# print("The larger value is"+str(largerVal))

# answer=eval(input("How many gallons does a ten-gallon hat hold"))
# if (1.5<=answer<=1):
#     print("Good, ",end="")
# else:
#     print("No,",end="")
# print("It holds about 3/4 of a gallon")


# numbers=[]
# first_num=eval(input("Enter first number:"))
# numbers.append(first_num)
# second_num=eval(input("Enter second number:"))
# numbers.append(second_num)
# third_num=eval(input("Enter the third number:"))
# numbers.append(third_num)
# msg="The largest of the three numbers is: "+str(max(numbers)) + ","
# print(msg)

## interpret weather beacon.
# Obtain color and mode
# color=input("Enter a color(Blue or Red): ")
# mode =input("Enter a mode (Steady or Flashing): ")
# color=color.upper()
# mode=mode.upper()
# #Anaylze responses and display ether forecast
# result=""
# if color== "Blue":
#     if mode == "Steady":
#         result="Clear View."
#     else: #mode is Flashing
#         result="Clouds Due."
# else: # color is red
#     if mode=="steady":
#         result="Rain Ahead. "
#     else: #mode is flashing
#         result="Snow Ahead."
# print("The weather forcast is", result)


# ## Evaluate profit.
# #Obtain input form user
# costs=eval(input("Enter total costs: "))
# revenue=eval(input("Enter total revenue: "))
# #Determine and display profit or loss
# if costs==revenue:
#     result="Break even."
# else:
#     if costs<revenue:
#         profit=revenue-costs
#         result="Profit is ${0:,.2f}.".format(profit)
#     else:
#         loss=costs-revenue
#         result="Loss is${0:,.2f}.".format(loss)
# print(result)

# ##Determine the larger of the two numbers.
# #Obtain the two numbers from the user.
# num1=eval(input("Enter the first number: "))
# num2=eval(input("Enter the Second number: "))
# #Determine and display the larger the value
# if num1>num2:
#     print("The larger value is", str(num1) + ".")
# elif num2>num1:
#     print("The larger value is", str(num2) + ".")
# else:
#     print("The two values are equal.")



# ##Bestow graduation honors.
# #Request grade point average.
# gpa=eval(input("Enteryour gpa: "))
# #Determine if the honors are warranted.
# if gpa>=3.9:
#     honors = "Summa Cum laude."
# elif gpa>=3.6:
#     honors = "Magna cum Laude."
# elif gpa>=3.3:
#     honors="Cum Laude"
# else:
#     honors="."
# #Display conclusion.
# print("You graduated " + honors)


# ##Request two numbers and find their sum. Validate the input.
# num1=input("Enter the first number: ")
# num2=input("Enter the second number: ")
# #Displaysum if entries are valid. Otherwise, inform 
# #the user where invalid entries were made.
# if num1.isdigit() and num2.isdigit():
#     print("The sum is", str(eval(num1) +eval(num2)) + ".")
# elif not num1.isdigit():
#     if not num2.isdigit():
#         print("Neither entry was a proper number.")
#     else:
#         print("The first entry was not a proper number.")
# else:
#     print("The scond entry was not a porper number.")


# if 7:
#     print("This will run...")
# if[]:
#     print("This will not run...")
# if[1, 2, 99]:
#     print("This will run...")
# if True:
#     print("This will run...")
# if False:
#     print("This will not run...")

