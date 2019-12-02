import tkinter
from random import randint
import pickle

#from PIL import ImageTk,Image

predict = 0
betok = False
bet = 0

users = {'d': 200}
username = 'd'

window = tkinter.Tk()
window.title('Dice')

balancedisplaytitle = tkinter.Label(window, text='Credits - ')
balancedisplay = tkinter.Entry(window)
balance = 100

betmsgbox=tkinter.Entry(window, width=50)


dice1label = tkinter.Label(window, text='First Die')
dice2label = tkinter.Label(window, text='Second Die')
dicetotallabel = tkinter.Label(window, text='Total')
dice1 = tkinter.Entry(window, width=1)
dice2 = tkinter.Entry(window, width=1)
dicetotal = tkinter.Entry(window, width=2)


verify = tkinter.Entry(window, width=42)

choosenum = tkinter.Label(window, text='Choose your number')
choosehilo = tkinter.Label(window, text='Will the rolled total be Higher or Lower than your chosen number?')
rollbutton = tkinter.Button(window, text='ROLL THE DICE', command=lambda: rolling())

#buttonquit = Button(window, text='Exit program', command= root.quit)


button2 = tkinter.Button(window, text='2', command=lambda: setpredict(2))
button3 = tkinter.Button(window, text='3', command=lambda: setpredict(3))
button4 = tkinter.Button(window, text='4', command=lambda: setpredict(4))
button5 = tkinter.Button(window, text='5', command=lambda: setpredict(5))
button6 = tkinter.Button(window, text='6', command=lambda: setpredict(6))
button7 = tkinter.Button(window, text='7', command=lambda: setpredict(7))
button8 = tkinter.Button(window, text='8', command=lambda: setpredict(8))
button9 = tkinter.Button(window, text='9', command=lambda: setpredict(9))
button10 = tkinter.Button(window, text='10', command=lambda: setpredict(10))
button11 = tkinter.Button(window, text='11', command=lambda: setpredict(11))
button12 = tkinter.Button(window, text='12', command=lambda: setpredict(12))

hibutton = tkinter.Button(window, text='Higher', command=lambda: sethilo('higher'))
lobutton = tkinter.Button(window, text='Lower', command=lambda: sethilo('lower'))
precisebutton = tkinter.Button(window, text='Precise', command=lambda: sethilo('precisely'))


balancedisplaytitle.grid(row=0, column=8)
balancedisplay.delete(0, 99999999)
balancedisplay.insert(0, str(balance))
balancedisplay.grid(row=0, column=9, columnspan=2)

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
    predict = (num)
    showhilo()

def showhilo():
    choosehilo.grid(row=4, columnspan=10, column=0)
    hibutton.grid(row=5, column=1, columnspan=4, padx=20, pady=50)
    lobutton.grid(row=5, column=8, columnspan=4, padx=20, pady=50)
    precisebutton.grid(row=5, column=5, columnspan=4, padx=20, pady=50)


#higher or lower input
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

#show verification and roll button
    verify.grid(row=6, column=0, columnspan=9)
    rollbutton.grid(row=6, column=9, columnspan=3)


def rolling():
    betok = False
    while betok == False:
        betmsgbox.grid(row=7, column=2)

        try:
            betmsgbox.delete(0, 999)
            betmsgbox.insert(0, 'What is your bet?')

            if bet <= (users[username]):
                betok = True
            else:
                betmsgbox.delete(0, 999)
                betmsgbox.insert(0, 'Your balance is too low, max bet is ' + str(users[username]) + '.')
        except:
            betmsgbox.delete(0, 999)
            betmsgbox.insert(0, 'Enter a number only, no decimal.')


#generate random dice roll
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    tot = int(d1 + d2)

#put the elements on screen
    dice1label.grid(row=8, column=0)
    dice1.grid(row=8, column=2)
    dice2label.grid(row=8, column=4)
    dice2.grid(row=8, column=5)
    dicetotallabel.grid(row=8, column=7)
    dicetotal.grid(row=8, column=8)

#clear the elements and insert new values
    dice1.delete(0, 2)
    dice2.delete(0, 2)
    dicetotal.delete(0, 3)
    dice1.insert(0, d1)
    dice2.insert(0, d2)
    dicetotal.insert(0, tot)


window.mainloop()
"""
#dropdown menu for betting
var = StringVar(window)
var.set(str(1)) # initial value

option = OptionMenu(window, var, str(1), str(2), str(5), str(10), str(20), str(50), str(100))
option.pack()

"""
