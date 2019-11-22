from random import randint
import inquirer

bet = int(0)
roll = int(0)
username = ''
balance = int(99)
yes = ('Y', 'y', 'yes', 'YES', 'Yes', '')
no = ('N', 'n', 'no', 'NO', 'No', ' ')
#predict = int(0)
print('DICE - \n')


def login():
    username = input('Username - ')
    balance = input('Starting balance - ')


def start():
    global balance
    global predict
    hilo = ''
    d1 = 0
    d2 = 0
    betok = False
    predict = 0
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
        if bet <= balance:
            betok = True
        else:
            print('Your balance is too low. Max bet at the moment is ' + str(balance) + '.')
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
            balance = balance + payout
        else:
            print('You lose')
            print('Old balance - ' + str(balance))
            balance = balance - int(bet)
            if balance < 1:
                print('You are out of cash!     -     GAME OVER!!')
                exit()

    else:
        if (tot > predict and greater_than == True) or (tot < predict and greater_than == False):
            print('You win')
            print('Old balance - ' + str(balance))
            balance = balance + int(bet)
        elif (tot < predict and greater_than == True) or (tot > predict and greater_than == False):
            print('You lose')
            print('Old balance - ' + str(balance))
            balance = balance - int(bet)
            if balance < 1:
                print('You are out of cash!     -     GAME OVER!!')
                exit()                

    print('Bet was ' + str(bet))
    print('New balance = ' + str(balance) + '\n')

    questions = [
                inquirer.List('playagain',
                                    message = 'Play again? ',
                                    choices=['Yes', 'No']
                            ),
            ]
    answers = inquirer.prompt(questions)
    if answers['playagain'] == 'Yes':
        for i in range(1, 5):        
            print('\n')
        start()
    else:
        print('Goodbye, progress saved.')
        exit()


start()







