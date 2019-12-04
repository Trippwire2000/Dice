from tkinter import *
from PIL import ImageTk, Image
from random import randint
import pickle

users = pickle.load(open("users.p", "rb"))
# users = {'d': 290}
# username = 'd'

# init window
window = Tk()
window.title('Dice')
window.geometry("640x320")
window.resizable(0, 0)


betmsgbox = Entry(window, width=50)
verify = Entry(window, width=42)

choosenum = Label(window, text='   Choose your number')
choosehilo = Label(window, text='               Will the rolled total be Higher or Lower than your chosen number?')
rollbutton = Button(window, text='Set the bet', command=lambda: [clear2, setbet(predict)])

# init buttons

button2 = Button(window, text='2', command=lambda: setpredict(2))
button3 = Button(window, text='3', command=lambda: setpredict(3))
button4 = Button(window, text='4', command=lambda: setpredict(4))
button5 = Button(window, text='5', command=lambda: setpredict(5))
button6 = Button(window, text='6', command=lambda: setpredict(6))
button7 = Button(window, text='7', command=lambda: setpredict(7))
button8 = Button(window, text='8', command=lambda: setpredict(8))
button9 = Button(window, text='9', command=lambda: setpredict(9))
button10 = Button(window, text='10', command=lambda: setpredict(10))
button11 = Button(window, text='11', command=lambda: setpredict(11))
button12 = Button(window, text='12', command=lambda: setpredict(12))

hibutton = Button(window, text='Higher', command=lambda: [clear1(), sethilo('higher')])
lobutton = Button(window, text='Lower', command=lambda: [clear1(), sethilo('lower')])
precisebutton = Button(window, text='Precise', command=lambda: [clear1(), sethilo('precisely')])
# buttonquit = Button(window, text='Save and exit', command=window.quit)


def login():
    global username
    window.grid_columnconfigure((0, 1, 2), weight=1)
    window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    usernamelabel=Label(window,text="What is your username? ")
    usernameinput=Entry(window, width=22)
    loginbutton=Button(window, text='Login', command=lambda: getusername())
    usernamelabel.grid(row=1, column=1)
    usernameinput.grid(row=2, column=1)
    loginbutton.grid(row=3, column=1)

    def getusername():
        global username
        username = usernameinput.get()

        if username in users:
            welcomemessage = Label(text='Welcome back ' + username + '\n' + 'Remaining balance is ' + str(users[username]))
            balance = (users[username])
        if username not in users:
            welcomemessage = Label(text='Hi ' + username + ', You start with 100 credit')
            users[username] = 100

        # Clears the screen
        usernamelabel.grid_forget()
        usernameinput.grid_forget()
        loginbutton.grid_forget()

        welcomemessage.grid(row=1, column=1)
        startbutton=Button(text='Start', command=lambda: [startbutton.grid_forget(), welcomemessage.grid_forget(), start()])
        startbutton.grid(row=2, column=1)


def start():
    # reset grid config
    window.grid_columnconfigure((0, 1, 2), weight=0)
    window.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)

    balancedisplay = Label(window, text='Credits - ' + str(users[username]))  # Balance is in dict users

    # Placing widgets onscreen
    balancedisplay.grid(row=0, column=0, columnspan=5)
    choosenum.grid(row=1, columnspan=9, column=1)
    button2.grid(row=2, column=0, padx=10, pady=10)
    button3.grid(row=2, column=1, padx=10, pady=10)
    button4.grid(row=2, column=2, padx=10, pady=10)
    button5.grid(row=2, column=3, padx=10, pady=10)
    button6.grid(row=2, column=4, padx=10, pady=10)
    button7.grid(row=2, column=5, padx=10, pady=10)
    button8.grid(row=2, column=6, padx=10, pady=10)
    button9.grid(row=2, column=7, padx=10, pady=10)
    button10.grid(row=2, column=8, padx=10, pady=10)
    button11.grid(row=2, column=9, padx=10, pady=10)
    button12.grid(row=2, column=10, padx=10, pady=10)


def setpredict(num):
    global predict
    predict = num

    # place buttons
    choosehilo.grid(row=4, columnspan=10, column=0)
    hibutton.grid(row=5, column=0, columnspan=4, padx=20, pady=50)
    precisebutton.grid(row=5, column=4, columnspan=4, padx=20, pady=1)
    lobutton.grid(row=5, column=8, columnspan=4, padx=20, pady=50)


def clear1():
    button2.grid_remove()
    button3.grid_remove()
    button4.grid_remove()
    button5.grid_remove()
    button6.grid_remove()
    button7.grid_remove()
    button8.grid_remove()
    button9.grid_remove()
    button10.grid_remove()
    button11.grid_remove()
    button12.grid_remove()
    choosenum.grid_remove()
    choosehilo.grid_remove()
    hibutton.grid_remove()
    lobutton.grid_remove()
    precisebutton.grid_remove()


# higher or lower input
def sethilo(hilopr):
    hi = lo = pr = False
    if hilopr == 'higher':
        hi = True
    elif hilopr == 'lower':
        lo = True
    elif hilopr == 'precisely':
        pr = True
    verify.delete(0, 99)
    if (hilopr == 'higher') or (hilopr == 'lower'):
        verify.insert(0, 'You have chosen that the roll will be ' + hilopr + ' than ' + str(predict))
    elif hilopr == 'precisely':
        verify.insert(0, 'You have chosen that the roll will be exactly ' + str(predict))

    verify.grid(row=6, column=0, columnspan=6)
    rollbutton.grid(row=6, column=9, columnspan=3)


def setbet(prediction):    # fix me
        betok = False
        while betok != True:
            whatbet = Label(text='What is your bet?')
            whatbet.grid(row=2, column=3)
            betentry = Entry(width=5)
            betentry.grid(row=2, column=4)
            go = Button(text='OK', command=lambda: bbet())
            go.grid(row=2, column=5)

            def bbet():
                bet = betentry.get()


            if bet <= (users[username]):
                betok = True
            else:
                betmsgbox.delete(0, 999)
                betmsgbox.insert(0, 'Your balance is too low, max bet is ' + str(users[username]) + '.')



def diceroll():
    # generate random dice roll
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    tot = d1 + d2


    # init dice images

    if d1 == 1:
        dice1 = ImageTk.PhotoImage(Image.open('1.png'))
    elif d1 == 2:
        dice1 = ImageTk.PhotoImage(Image.open('2.png'))
    elif d1 == 3:
        dice1 = ImageTk.PhotoImage(Image.open('3.png'))
    elif d1 == 4:
        dice1 = ImageTk.PhotoImage(Image.open('4.png'))
    elif d1 == 5:
        dice1 = ImageTk.PhotoImage(Image.open('5.png'))
    else:
        dice1 = ImageTk.PhotoImage(Image.open('6.png'))

    diceshow1 = Label(image=dice1, padx=5, pady=5)

    if d2 == 1:
        dice2 = ImageTk.PhotoImage(Image.open('1.png'))
    elif d2 == 2:
        dice2 = ImageTk.PhotoImage(Image.open('2.png'))
    elif d2 == 3:
        dice2 = ImageTk.PhotoImage(Image.open('3.png'))
    elif d2 == 4:
        dice2 = ImageTk.PhotoImage(Image.open('4.png'))
    elif d2 == 5:
        dice2 = ImageTk.PhotoImage(Image.open('5.png'))
    else:
        dice2 = ImageTk.PhotoImage(Image.open('6.png'))

    diceshow2 = Label(image=dice2, padx=5, pady=5)

    clear2()

    diceshow1.grid(row=0, column=0)
    diceshow2.grid(row=0, column=1)
    dicetotal=Label(width=10, text='Total - ' + str(tot))
    dicetotal.grid(row=1, column=0)


def clear2():
    verify.grid_remove()
    rollbutton.grid_remove()

login()

# pickle.dump(users, open("users.p", "wb"))
window.mainloop()
