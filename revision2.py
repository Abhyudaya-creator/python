# print("hello world\nhello world")

# name="abhi"
# print(len(name))



#PROJECT TIP CALCULATOR
# print("WELCOME TO TIP CALCULATOR")
# bill=float(input("What was the bill?"))
# tip=float(input("how would you like to tip? 10, 12 or 15??"))
# people=float(input("how many people are splitting the bill?"))

# exact_bill= round((tip + bill)/people , 2)

# print(f"each one of you has to pay {exact_bill}")


#DAY 3


# if height>120:
#     print("you can ride the roller coaster")
# else:
#     print("you cant ride")


# weight = 85
# height = 1.85

# bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

# if bmi<18.5:
#     print("underweight")
    
# elif bmi>=18.5:
#     print("normal weight")
    
# elif bmi<25:
#     print("normal weight")
        
# else:
#     print("overweight")


#TREASURE ISLAND PROJECT

# print("welcome to treasure island")

# first=input("would you go left or right")

# if first=="left":
#     print("congrats, you move to the second round")
#     second=input("will you swim or wait")

#     if second=="wait":
#         print("congrats you have crossed this level")
#         third= input("you now have come across 3 doors, red, yellow, blue...choose one of these color to see which one you'll open:")
#         if third=="yellow":
#             print("woohooo, you've won the game")

#         else:
#             print("game over")


#     elif second=="swim":
#         print("sorry, the whale ate you, game over")

#     else:
#         print("sorry invalid choice")

# elif first=="right":
#     print("sorry, wrong choice game over")
# else:
#     print("unvalid choice")


#DAY4

# import random
# import my_module_for_revision

# random_integer=random.randint(1,100)

# print(random_integer)
# print(my_module_for_revision.fav_no)

# random= random.random(0,100) 
# # "0 will be included but 100 won"t be"

# random2= random.uniform(0,100)
# #" 0 and 100 both will be included"

#HEADS OR TAILS

# import random

# a=random.randint(0,1)
# if a==1:
#     print("heads")
# else:
#     print("tails")


#lists:
# fruits = ["apple", "mango", "vlurberry", "green_apple", "cherry", "banana"]


# print(fruits[0])

# fruits[1] = "grapes"
# print(fruits[1])

# fruits.append("papaya")
# #adds an item to the end of the list

# fruits.insert(2, "pineapple")
# print(fruits[2])

#ROCK, PAPER, SCISSORS
import random

comp_choice = random.randint(1,3)
print("Welcome to rock paper scissors")

user_choice=int(input("what do you choose? type 1 for paper, 2 for rock, 3 for scissors:"))

print(f"your choice is {user_choice}")

print(f"the computer's choice is {comp_choice}")

if user_choice== 1 and comp_choice==2:
    print("you won")
elif user_choice== 2 and comp_choice==3:
    print("you won")
elif user_choice== 3 and comp_choice==1:
    print("you won")

elif user_choice==1 and comp_choice==3:
    print("you lost")
elif user_choice== 2 and comp_choice==1:
    print("you lost")
elif user_choice== 3 and comp_choice==2:
    print("you lost")
elif user_choice==comp_choice:
    print("its a draw")
else:
    print("invalid input")