# A
x = int(input("define X - please enter a number "))
y = int(input("define Y - please enter a number "))

if x > y:
    print("X is Bigger than y")
else:
    print("X is smaller than y")

# B
while a != 5:
    a+=1
    print(a-1,"was and new a is",a)
    if a == 5:
        print("Done!")

# C
x = "summer"
y = "winter"
z = "fall"
w = "spring"

VariableC = int(input("define f - enter a number between 1-4 "))
if VariableC == 1:
      print(x)
elif VariableC == 2:
    print(y)
elif VariableC == 3:
    print(z)
else:
    print(w)

# D
#1. Loop will run 10 times
#2.
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10

# E
age = int(input("What is your age? "))
last_name = str(input("What is your first letter of your last name? "))
flew = str(input("Did you flew abroad (true/flase) "))
apartment_num = int(input("What is your apartment number? "))

import subprocess as sp
while (flew != "true" and flew != "false"):
    print("You had a typo, please write true or false currectly. Let's try again:")
    flew = str(input("Did you flew abroad (true/false) "))
    tmp = sp.call('clear', shell=True)


if flew == "true":
    print("Your age is:", age)
    print("Your last letter of your last name is:", last_name)
    print("You flew abroad and you liked it")
    print("Your apartment number is:", apartment_num)
elif flew == "false":
    print("Your age is:", age)
    print("Your last letter of your last name is:", last_name)
    print("You didn't flew abroad and you realy want to.")
    print("Your apartment number is:", apartment_num)

# F
phone_num = int(input("What is phone number? "))
print ("Your phone number is", phone_num)

# G
def printHello():
    print("hello")
printHello()

def calculator():
    print(5+3.2)
calculator()

# H
def yourname():
    full_name = str(input("What is your full name? "))
    print (full_name)
yourname()

def calc():
    recive_num = int(input("please enter any number? "))
    print(recive_num/2)
calc()

# I
def calc_two():
    recive_num1 = float(input("please enter your first number; any number? "))
    recive_num2 = float(input("please enter your second; number any number? "))
    print(recive_num2+recive_num1)
calc_two()


def spaces():
    str_one = str(input("Enter your first string (Recommended to add -> Bye Bye) : "))
    str_two = str(input("Enter your second string (Recommended to add -> space) : "))
    all_str = str_one + "  " + str_two
    print(" ".join(all_str.split()))
spaces()

