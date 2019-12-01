import tkinter
from PIL import ImageTk,Image


predict = 0

window = tkinter.Tk()
window.title('Dice')

balancedisplaytitle = tkinter.Label(window, text='Credits - ')
balancedisplay = tkinter.Entry(window)
choosenum = tkinter.Label(window, text='Choose your number')

rollbutton = tkinter.Button(window, text='ROLL THE DICE')

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

hibutton = tkinter.Button(window, text='Higher')
lobutton = tkinter.Button(window, text='Lower')
precisebutton = tkinter.Button(window, text='Precise')


balancedisplaytitle.grid(row=0, column=8)
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
    predict = (num)



def hiorlow():
    hibutton.grid(row=4, column=0)
    precisebutton.grid(row=5, column=0)
    lobutton.grid(row=6, column=0)



#hiorlow()






window.mainloop()
