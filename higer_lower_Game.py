import random
from ascii import logo,vs
from game_data import data
# from replit import clear



def format_data(account):
    """takes the account data and returns the  printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a{account_descr}, from {account_country}"

def check_answer(guess,a_follower,b_follower):
    """takes the user guess and follower counts and returns if they got it right."""
    if a_follower>b_follower:
        return guess =='a'
    else:
        return guess =='b'

# display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatble

while game_should_continue:
        
    #Generate a  random account from the game data 
    
    # making account at position B become the next account at postion A
    account_a = account_b
    account_b = random.choice(data)


    while account_a == account_b:
        account_b = random.choice(data)


    print(f"compare A : {format_data(account_a)} \n")

    print(vs)

    print(f"compare B : {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? type 'A' or 'B'!")    

    # check if user is correct 

    # get the follower count of each account
    a_follower_count =  account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    
    # clear the screen between rounds
    # clear()
    print(logo)
    # give user feedback on their guess
    # score keeping 

    if is_correct:
        score +=1
        print(f"you're right! your score is {score}")
    else:
        game_should_continue = False
        print(f"you're wrong! your score is {score}")




