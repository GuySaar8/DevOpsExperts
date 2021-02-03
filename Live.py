#####################
# Define functions
#####################
def singin():       # say hello to new user
    print("Hello Rookie and welcome to the World Of Games (WoG)")
    print("Before we begin, the best experience of your life")
    print("You need to create a new account")
    pass

def welcome():      # say hello to user
    print("Hello " + logonname +  " and welcome to the World Of Games (WoG)")
    print("Here you can find many cool games to play")

def check_if_number():    # check if var is integer
    choose_num = input("Please insert a number: ")
    if_digit = choose_num.isdigit()
    if if_digit == True:
        choose_num = int(choose_num)
        return [choose_num, if_digit];
    else:
        choose_num = str(choose_num)
        return [choose_num, if_digit];

def game_list():    # print game list
    print("Which game would you like to play?")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def reset_var():    # Define variables that will be used in the script function
    if_digit = 'false'
    out_of_loop = 1
    difficulty_list = 'Null'
    game_name = 'Null'
    check_list = 'Null'
    return [if_digit,out_of_loop,difficulty_list,game_name,check_list]


def load_game():
    # Define variables
    reset_var()
    get_list = reset_var()
    out_of_loop = get_list[1]
    choose_num = 0

    # Choose a game
    import subprocess as sp  # clear screen
    tmp = sp.call('clear', shell=True)
    game_list()
    print("Please choose a game from: (choose number 1-3)")
    check_list = check_if_number()
    choose_num = check_list[0]
    if_digit = check_list[1]

    tmp = sp.call('clear', shell=True) # clear screen

    # check if input is valid
    while True:
        if if_digit == True and choose_num <= 3 and choose_num >= 1:
            print("have fun")
            import time
            time.sleep(5)
            import subprocess as sp  # clear screen
            tmp = sp.call('clear', shell=True)
            break
        else:
            if out_of_loop < 3:
                print("")
                print("Dont insert a string ")
                print("And make sure you insert a number between 1 - 3,")
                out_of_loop = out_of_loop + 1
                game_list()
                print("")
                game_int = check_if_number()
                choose_num = check_list[0]
                if_digit = check_list[1]

                tmp = sp.call('clear', shell=True) # clear screen

            if out_of_loop >= 3:
                print("")
                print("DONT INSERT A STRING! ")
                print("MAKE SURE IT'S BETWEEN 1-3 YOU MTF!!!")
                out_of_loop = out_of_loop + 1
                game_list()
                print("")
                check_list = check_if_number()
                choose_num = check_list[0]
                if_digit = check_list[1]

                tmp = sp.call('clear', shell=True) # clear screen

            if out_of_loop > 6:
                print('DO NOT MESS WITH THE GAME MASTER')
                print('BYE BYE')
                exit()

    # Define variables
    reset_var()
    get_list = reset_var()
    out_of_loop = get_list[1]

    # Define game name
    if choose_num == 1:
        game_name = 'Memory Game'
    elif choose_num == 2:
        game_name = 'Guess Game'
    elif choose_num == 3:
        game_name = 'Currency Roulette'

    # Choose difficulty
    print("You will play " + game_name)
    print("Please choose game difficulty from 1 to 5: ")
    difficulty_list = check_if_number()
    choose_num = difficulty_list[0]
    if_digit = difficulty_list[1]

    tmp = sp.call('clear', shell=True)  # clear screen

    while True:
        if if_digit == True and choose_num >= 1 and choose_num <= 5:
            print("you choose game " + game_name + " and difficicuty level ", choose_num)
            break
        else:
            if out_of_loop < 6:
                out_of_loop = out_of_loop + 1
                print("try again")
                print("You will play " + game_name)
                print("Please choose game difficulty from 1 to 5: ")
                difficulty_list = check_if_number()
                choose_num = difficulty_list[0]
                if_digit = difficulty_list[1]

                import subprocess as sp  # clear screen
                tmp = sp.call('clear', shell=True)
            else:
                print('DO NOT MESS WITH THE GAME MASTER')
                print('BYE BYE')
                import time
                time.sleep(10)
                import sys
                sys.exit()

    difficulty = choose_num
    return [game_name,difficulty]
    print(logonname)

#####################
# START
#####################

# Accounts DB will be loeded and saved to JSON file
accounts={'username':['info'],'DevOps':['Experts']}

logonname = input("What is your log on name: ")     # Get Logon name

# check if username exist
# need to add check log on name by UPPER
while True:
    try:
         if accounts[logonname]:
            welcome()
            break
    except KeyError:        # if user does not exist user will be created
        singin()
        account_name = 'null'
        account_name = input("Insert your new account name: ")
        account_name = account_name.upper()
        accounts[account_name]='account_info'
        logonname = account_name



load_game()


# Need to catch SYSTEM EXIT error