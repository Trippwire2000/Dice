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

    questions = [
                    inquirer.List('hiloq',
                                        message = 'Will the roll of the dice be higher than this?',
                                        choices=['Yes', 'No']
                                ),
            ]
    answers = inquirer.prompt(questions)
    if answers['hiloq'] == 'Yes':
        greater_than = True
    else:
        greater_than = False
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
    if (tot > predict and greater_than == True) or (tot < predict and greater_than == False):
        print('You win')
        print('Old balance - ' + str(balance))
        balance = balance + int(bet)
    if (tot < predict and greater_than == True) or (tot > predict and greater_than == False):
        print('You lose')
        print('Old balance - ' + str(balance))
        balance = balance - int(bet)
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
        print('\n')
        start()
    else:
        print('Goodbye, progress saved.')
        exit()


start()
