# from class:

numbers = [951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,615, 83, 165, 141, 501,
           263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566,
           597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
           815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753,
           854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]
for i in numbers:
    if i<500 and i%2==0:
        print(i)

# E
age = int(input("What is your age? "))
last_name = input("What is your first letter of your last name? ")
flew = input("Did you flew abroad (true/flase) ")
currency = input("What is your current currency? (Shekels/Dollar? ")
apartment_num = int(input("What is your apartment number? "))

print(currency + age)
#we recive an error - we cannt add str and int
print(currency, age)
#fixing the issue

import subprocess as sp
while (flew != "true" and flew != "false"):
    print("You had a typo, please write true or false currectly. Let's try again:")
    flew = str(input("Did you flew abroad (true/false) "))
    tmp = sp.call('clear', shell=True)


if flew == "true":
    print("Your age is:", age)
    print("Your last letter of your last name is:", last_name)
    print("Your currency is:", currency)
    print("You flew abroad and you liked it")
    print("Your apartment number is:", apartment_num)
elif flew == "false":
    print("Your age is:", age)
    print("Your last letter of your last name is:", last_name)
    print("Your currency is:", currency)
    print("You didn't flew abroad and you realy want to.")
    print("Your apartment number is:", apartment_num)

# K

for i in numbers:
    if i<500 and i%2==0:
        print(i)

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print("")
# * * * *
# * * * *
# * * * *
# * * * *

for rows in range(5):
    print("*"*rows)
# *
# **
# ***
# ****

for rows in range(5):
    print(" "*(4-rows) + "*"*rows)
#    *
#   **
#  ***
# ****

for rows in range(4):
    for coloums in range(4-rows):
        print("*",end=" ")
    print("")
# * * * *
# * * *
# * *
# *

y=int(input("please enter a number of coluoms: "))
x=int(input("please enter a number of rows: "))
for rows in range(x):
    for coloums in range(y-rows):
        print("*",end=" ")
    print("")
#or
for rows in range(x):
    for coloums in range(rows+y):
        print("*",end=" ")
    print("")


for rows in range(5):
    print(" "*(4-rows) + "* "*rows)

for rows in range(6,0,-1):
    print(" "*(4-rows) + "* "*rows)
#    *
#   * *
#  * * *
# * * * *

for rows in range(5):
    print(" "*(4-rows) + "* "*rows)
for rows in range(rows,0,-1):
    print(" "*(4-rows) + "* "*rows)
#    *
#   * *
#  * * *
# * * * *
# * * * *
#  * * *
#   * *
#    *

for rows in range(5):
    print(" "*(4-rows) + "* "*rows)
for rows in range(rows-1,0,-1):
    print(" "*(4-rows) + "* "*rows)
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *

for rows in range(6,0,-1):
    print("  "*(6-rows) + "* "*rows)
# * * * * * *
#   * * * * *
#     * * * *
#       * * *
#         * *
#           *
for rows in range(5):
    print("* "*rows)
for rows in range(rows-1,0,-1):
    print("* "*rows)
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *

for rows in range(5):
    print("  " *(6-rows) + "* "*rows)
for rows in range(rows-1,0,-1):
    print("  " *(6-rows) + "* "*rows)

#          *
#        * *
#      * * *
#    * * * *
#      * * *
#        * *
#          *

# L

j=6
i=0

for row in range(7):
    for col in range(7):
        if row==i and col==j:
            print("*",end="")
            i=i+1
            j=j-1
        elif row==col:
            print("*",end="")
        else:
            print(end=" ")
    print("")

# M
def get_num(num=0):
    num=int(input("please inesrt a number "))
    return num
sum_digits = get_num()

def sum():
    sum_digits = get_num()
    result=0
    while sum_digits>0:
        result=result+(sum_digits%10)
        sum_digits = sum_digits//10
    print("sum is", result)

# Loop exercise from mail
#1.
for i in range(1,10):
    print(i**2)

#2.
res=0
for i in range(1,11):
    if i%2==0:
        res=(res+i)
        print(res)
#3.
a=int(input("please inesrt a number "))
b=int(input("please inesrt a number "))
c=int(input("please inesrt a number "))
if a<b:
    for i in range(a,b):
        if i%c==0:
            print(i, i/c)
elif a>b:
    for i in range(b,a):
        if i%c==0:
            print(i, i/c)
else:
    print(a, "and", b,"is the same value")



