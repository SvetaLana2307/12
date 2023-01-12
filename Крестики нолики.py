from tkinter import *

frm = []; btn = []; who = True
playArea = []
standings = []                          # Турнирная таблица (положение)

def play(n):
    global who
    btn[n].config(text= 'X' if who else 'O', state=DISABLED)
    playArea[n] = 1 if who else -1
    standings[0] = playArea[0] + playArea[1] + playArea[2]
    standings[1] = playArea[3] + playArea[4] + playArea[5]
    standings[2] = playArea[6] + playArea[7] + playArea[8]
    standings[3] = playArea[0] + playArea[3] + playArea[6]
    standings[4] = playArea[1] + playArea[4] + playArea[7]
    standings[5] = playArea[2] + playArea[5] + playArea[8]
    standings[6] = playArea[0] + playArea[4] + playArea[8]
    standings[7] = playArea[2] + playArea[4] + playArea[6]
    print(n, standings[0:8])
    for i in range(8):
        if standings[i] == 3:
            print('X win')
        elif standings[i] == -3:
            print('O win')
    who = not(who)

for i in range(3):
    frm.append(Frame())
    frm[i].pack(expand=YES, fill=BOTH)
    for j in range(3):
        btn.append(Button(frm[i], text=' ', font=('mono', 20, 'bold'), width=3, height=2))
        btn[i*3+j].config(command=lambda n=i*3+j:play(n))
        btn[i*3+j].pack(expand=YES, fill=BOTH, side=LEFT, padx=1, pady=1)
        playArea.append(0)
        standings.append(0)

mainloop()

