#####################
# import modules
#####################
import random
import time
import subprocess as sp
import sys


#####################
# Define functions
#####################

#check if its a number
def check_if_number():    # check if var is integer
    choose_num = input("-> ")
    if_digit = choose_num.isdigit()
    if if_digit == True:
        choose_num = int(choose_num)
        user_chosen_nums.append(choose_num)
        return [choose_num, if_digit,user_chosen_nums];
    else:
        choose_num = str(choose_num)
        user_chosen_nums.append(choose_num)
        return [choose_num, if_digit,user_chosen_nums];

def byebye():
    print('Thanks for playing')
    print('BYE BYE')
    time.sleep(10)
    sys.exit()


def print_hello():
    tmp = sp.call('clear', shell=True)
    print ("Hello! to Guess Game")
    print ("you will compete with the all mighty GAME MASTER")
    print ("what are the odds you are willing to risk?")
    print ("(for example if you chose the number 5 the odds will be 1 to 5)")

def reset_var(): # Define variables that will be used
    odds = 0
    secret = 0
    Play_again = "no"
    out_of_loop = 1
    user_chosen_nums = []
    return [Play_again,out_of_loop,secret,odds,user_chosen_nums];

def again():
    tmp = sp.call('clear', shell=True)
    print("Would you like to try again?")
    print("Choose y to play again; else you will be logged out")
    Play_again = input("What is your choice? ")
    if Play_again == "y":
        print("you will play again")
        time.sleep(7)
        guess_game()
    else:
        byebye()


def guess_game():
    # Define variables that will be used
    reset_list = reset_var()
    Play_again = reset_list[0]
    out_of_loop = reset_list[1]
    secret = reset_list[2]
    odds = reset_list[3]
    user_chosen_nums = reset_list[4]

    # Choosing the odds block
    print_hello()
    checking_list = check_if_number()
    choose_num = checking_list[0]
    if_digit = checking_list[1]
    user_chosen_nums = checking_list[2]

    # checking if odds is a number
    while True:
        if if_digit == True:
            print("may the odds be ever in your favor")
            odds = choose_num
            out_of_loop = 1
            user_chosen_nums.clear()
            time.sleep(5)
            break
        else:
            if out_of_loop >= 6:
                byebye()
            else:
                print("You inserted a string")
                print("Please insert a number")
                time.sleep(5)
                out_of_loop = out_of_loop + 1
                print_hello()
                checking_list = check_if_number()
                choose_num = checking_list[0]
                if_digit = checking_list[1]
                tmp = sp.call('clear', shell=True)

    # Start Geussing game
    secret = random.randint(1, int(odds))  # random number

    tmp = sp.call('clear', shell=True)
    print("Let the game begin!")
    print("Guess the number the GAME MASTER has Chosen")
    print("Choose a number between 1 to ", odds)
    checking_list = check_if_number() # get number from user
    choose_num = checking_list[0]
    if_digit = checking_list[1]
    user_chosen_nums = checking_list[2]

    while True:
        if if_digit == True and choose_num == secret:
            print("YOU WON THE GAME!!!")
            print("Kodus for winning on 1 to ", choose_num, " odds")
            print("Trail Number ", out_of_loop, " of 5")
            print("The number that was chosen was: ", secret)
            time.sleep(5)
            tmp = sp.call('clear', shell=True)
            again()

        elif out_of_loop >= 5: #get number of trails
            print("You lost to the GAME MASTER")
            print("The number that was chosen was: ", secret)
            time.sleep(5)
            again()

        elif if_digit == True and choose_num > odds:
            tmp = sp.call('clear', shell=True)
            print("your choices so far", user_chosen_nums)
            print("Trail Number ", out_of_loop, " of 5")
            print("What are you doing?")
            print("Choose a number between 1 to ", odds)

            checking_list = check_if_number()
            choose_num = checking_list[0]
            if_digit = checking_list[1]
            out_of_loop = out_of_loop + 1
            tmp = sp.call('clear', shell=True)

        elif if_digit == False:
            tmp = sp.call('clear', shell=True)
            print("What is wrong with you?? ENTER A NUMBER AND NOT A STRING")
            print("your choices so far", user_chosen_nums)
            print("Trail Number ", out_of_loop, " of 5")
            print("Choose a number between 1 to ", odds)

            checking_list = check_if_number()
            choose_num = checking_list[0]
            if_digit = checking_list[1]
            user_chosen_nums = checking_list[2]
            out_of_loop = out_of_loop + 1

            tmp = sp.call('clear', shell=True)

        elif if_digit == True and choose_num <= odds and choose_num != secret:
            tmp = sp.call('clear', shell=True)
            print("nice try")
            print("your choices so far", user_chosen_nums)
            print("Trail Number ", out_of_loop, " of 5")
            print("Choose a number between 1 to ", odds)
            checking_list = check_if_number()
            choose_num = checking_list[0]
            if_digit = checking_list[1]
            user_chosen_nums = checking_list[2]
            out_of_loop = out_of_loop + 1

            tmp = sp.call('clear', shell=True)

guess_game()
