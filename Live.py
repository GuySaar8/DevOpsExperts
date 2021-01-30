# Define functions
def singin():
    print("Hello Rookie and welcome to the World Of Games (WoG)")
    print("Before we begin, the best experience of your life")
    print("You need to create a new account")
    pass

def welcome():
    print("Hello " + logonname +  " and welcome to the World Of Games (WoG)")
    print("Here you can find many cool games to play")

def check_if_number():
    choose_game = input("Please insert a number: choose 1,2 or 3: ")
    x = choose_game.isdigit()
    if x==True:
        game_int = int(choose_game)
    return choose_game
    return game_int


def game_list():
    print("Which game would you like to play?")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

def load_game():
    game_list()
    check()

# Accounts DB should be sent to a file and load from there
accounts={'username':['info']}

# START:
logonname = input("your log on name: ")

# check if username exsit
while True:
    try:
         if accounts[logonname]:
            welcome()
            break
    except KeyError:
        singin()
        account_name = 'null'
        account_name = input("Insert your new account name: ")
        account_name = account_name.upper()
        accounts[account_name]='account_info'
        logonname = account_name



# load_game()

# Check game number
# check_if_number() does not work yet with the loop
# check_if_number() will be used

# Define variables
choose_game='0'
x='false'
t=1
choose_game = input("Please insert a number: choose 1,2 or 3: ")
x = choose_game.isdigit()
if x == True:
    game_int = int(choose_game)

while True:
    if x==True and game_int <= 3 and game_int >= 1:
        print ("have fun")
        break
    else:
        if t >= 1:
            game_list()
            print("")
            print("Dont insert a string ")
            print("And make sure you insert a number between 1 - 3,")
            choose_game = input("Please insert a number: choose 1,2 or 3: ")
            x = choose_game.isdigit()
            if x == True:
                game_int = int(choose_game)
            t = t + 1
        if t > 3:
            game_list()
            print("")
            print("DONT INSERT A STRING! ")
            print("MAKE SURE IT'S BETWEEN 1-3 YOU MTF!!!")
            choose_game = input("Please insert a number: choose 1,2 or 3: ")
            x = choose_game.isdigit()
            if x == True:
                game_int = int(choose_game)

# Difine game name
if game_int ==1:
    game_name= 'Memory Game'
elif game_int==2:
    game_name = 'Guess Game'
elif game_int == 3:
    game_name = 'Currency Roulette'

# choose dificukty
# check_if_number() will be used

# Define variables
difficulty_int =0

print("You will play " + game_name)
print("Please choose game difficulty from 1 to 5: ")
difficulty = input("Please insert a number: choose 1-5: ")
x = difficulty.isdigit()
if x == True:
    difficulty_int = int(difficulty)

while True:
    if difficulty_int >=1 and difficulty_int <=5:
        print ("you choose game " + game_name + " and difficicuty level ", difficulty_int)
        break
    else:
        print("try again")
        print("You will play " + game_name)
        print("Please choose game difficulty from 1 to 5: ")
        difficulty = input("Please insert a number: choose 1-5: ")
        x = difficulty.isdigit()
        if x == True:
            difficulty_int = int(difficulty)
