from random import randint
import inquirer
import os

bet = int(0)
roll = int(0)
users = {}
print('DICE - \n')
username = ''
balance = 0

def login():
    global username
    global balance
    username = input('Username - ')
    username = (username.upper())
    if username in users:
        print('Welcome back ' + username + '\n' + 'Remaining balance is ' + str(users[username]))
        balance = (users[username])
    if username not in users:
        balance = 100
        print('Hi ' + (username.title()) + '\nYou start with 100 credit')
        users[username] = balance
    print(users[username])


def start():
    global predict
    hilo = ''
    d1 = 0
    d2 = 0
    betok = False
    predict = 0
    mult = 0
    playagain =''
    questions = [
            inquirer.List('predict',
                                message = 'Pick a number between 3 and 11 - ',
                                choices=[3, 4, 5, 6, 7, 8, 9, 10, 11]
                        ),
        ]
    answers = inquirer.prompt(questions)
    predict = answers['predict']
    print('You have chosen ' + str(answers['predict']) + '.\n')

    questions = [inquirer.List('hiloq', message = 'Will the roll of the dice be Higher, Lower or Precise?', choices=['Higher', 'Precise', 'Lower']),]
                              
    answers = inquirer.prompt(questions)
    if answers['hiloq'] == 'Higher':
        greater_than = True
        precise = False
    elif answers['hiloq'] == 'Lower':
        greater_than = False
        precise = False
    else:
        precise = True

    while betok == False:
        bet = int(input('\nWhat is your bet? - '))
        if bet <= (users[username]):
            betok = True
        else:
            print('Your balance is too low. Max bet at the moment is ' + str(users[username]) + '.')
    d1 = randint(1,6)
    d2 = randint(1,6)
    tot = int(d1 + d2)
    print('\n' + str(d1) + ' ' + str(d2))
    print('Total ' + str(tot) + '\n')
  
    if precise == True:
        if predict == tot:            
            if (predict == 2) or (predict == 12):
                mult = 26
            elif (predict == 3) or (predict == 11):
                mult = 23
            elif (predict == 4) or (predict == 10):
                mult = 21
            elif (predict == 5) or (predict == 9):
                mult == 18
            elif (predict == 6) or (predict ==8):
                mult = 15
            elif predict == 7:
                mult = 12
            payout = (bet * (1 + mult))
            print('You win - multiplier is ' + str(mult) + 'x.')
            print('Payout is ' + str(payout) + '.')
            (users[username]) += payout
        else:
            print('You lose ')
            print('Old balance - ' + str(users[username]))
            (users[username])  = (users[username]) - int(bet)
            if (users[username]) < 1:
                print('You are out of cash!     -     GAME OVER!!')
                exit()

    else:
        if (tot > predict and greater_than == True) or (tot < predict and greater_than == False):
            print('You win ')
            print('Old balance - ' + str(users[username]))
            (users[username]) += int(bet)
        elif (tot < predict and greater_than == True) or (tot > predict and greater_than == False) or (tot == predict):
            print('You lose')
            print('Old balance - ' + str(users[username]))
            (users[username]) -= int(bet)
            if balance < 1:
                print('You are out of cash!     -     GAME OVER!!')
                exit()                

    print('Bet was ' + str(bet))
    print('New balance = ' + str(users[username]) + '\n')

    questions = [
                inquirer.List('playagain',
                                    message = 'Play again? ',
                                    choices=['Yes', 'No']
                            ),
            ]
    answers = inquirer.prompt(questions)
    if answers['playagain'] == 'Yes':
        for i in range(1, 5):        
            os.system('clear')
            print('\n       Balance - ' + str(users[username]) + '\n')
        start()
    else:
        print('Goodbye, progress saved.')
        exit()


login()
start()







