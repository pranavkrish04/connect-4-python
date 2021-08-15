import tkinter as tk
from typing import Text
import colors as c
import numpy as np

'''
self - keyword used to access everything in a class.
__init__ - constructor [ when class is called the init gets called ].
tkinter Frame - widget helpful to organise the things on screen.
'''

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Connect 4")

        self.main_grid = tk.Frame(self, bg=c.background_color, bd=3, width=700, height=900)
        self.main_grid.grid(pady=(80, 0))
        self.make_GUI()
        
        self.player = 1
        self.array = np.zeros([7,7])

        self.master.bind("<KP_1>", lambda event, a=1:self.addbob(a))
        self.master.bind("<KP_2>", lambda event, a=2:self.addbob(a))
        self.master.bind("<KP_3>", lambda event, a=3:self.addbob(a))
        self.master.bind("<KP_4>", lambda event, a=4:self.addbob(a))
        self.master.bind("<KP_5>", lambda event, a=5:self.addbob(a))
        self.master.bind("<KP_6>", lambda event, a=6:self.addbob(a))
        self.master.bind("<KP_7>", lambda event, a=7:self.addbob(a))
        

        self.mainloop()
    
    def make_GUI(self):
        self.cells = []
        for i in range(7):
            row = []
            for j in range(7):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg=c.emp,
                    width=100,
                    height=100
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Label(self.main_grid, bg=c.emp)
                cell_number.grid(row=i, column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

    def check(self, array, x, y, pl):
        if (self.checkhori(array, x, y, pl) >= 4):
            self.endgame(pl)
        if (self.checkverti(array, x, y, pl) >= 4):
            self.endgame(pl)
        if (self.checkdial(array, x, y, pl) >= 4):
            self.endgame(pl)
        if (self.checkdiar(array, x, y, pl) >= 4):
            self.endgame(pl)
        pass

    def checkhori(self, a, x, y, pl):
        self.tot = 1
        self.p = 1
        while(True):
            if ((y-self.p) == -1):
                break
            elif(a[x,y-self.p] == pl):
                print(a[x,y-self.p])
                self.tot +=1
                self.p += 1
            else:
                break
        p = 1
        while(True):  
            if ((y+p) == 7):
                break
            elif(a[x,y+p] == pl):
                self.tot +=1
                p += 1
            else:
                break
        return self.tot

    def checkverti(self, a, x, y, pl):
        tot = 1
        p = 1
        while(True):
            if ((x-p) == -1):
                break
            elif(a[x-p,y] == pl):
                tot +=1
                p += 1
            else:
                break
        p = 1
        while(True):  
            if ((x+p) == 7):
                break
            elif(a[x+p,y] == pl):
                tot +=1
                p += 1
            else:
                break
        return tot

    def checkdial(self, a, x, y, pl):
        tot = 1
        p = 1
        while(True):
            if ((x-p) == -1 or (y-p)==-1):
                break
            elif(a[x-p,y-p] == pl):
                tot +=1
                p += 1
            else:
                break
        p = 1
        while(True):  
            if ((x+p) == 7 or (y+p) == 7):
                break
            elif(a[x+p,y+p] == pl):
                tot +=1
                p += 1
            else:
                break
        return tot

    def checkdiar(self, a, x, y, pl):
        tot = 1
        p = 1
        while(True):
            if ((x+p) == 7 or (y-p)==-1):
                break
            elif(a[x+p,y-p] == pl):
                tot +=1
                p += 1
            else:
                break
        p = 1
        while(True):  
            if ((x-p) == -1 or (y+p)==7):
                break
            elif(a[x-p,y+p] == pl):
                tot +=1
                p += 1
            else:
                break
        return tot

    def addbob(self, num):
        if (self.array[0, num-1] != 0):
            pass
        else:
            self.p = 7
            for x in range(7):
                if (self.array[self.p-1, num-1] == 0):
                    if(self.player == 1):
                        self.array[self.p-1, num-1] = 1
                        self.cells[self.p-1][num-1]["frame"].configure(bg=c.pl1)
                    else:
                        self.array[self.p-1, num-1] = 2
                        self.cells[self.p-1][num-1]["frame"].configure(bg=c.pl2)
                    self.check(self.array, self.p-1, num-1,self.player)
                    break
                else:
                    self.p -= 1
            if(self.player == 1):
                self.player = 2
            else:
                self.player = 1

    def endgame(self, pl):
        text = tk.Label(self.main_grid, text=f"{pl} has won the game", font=("Helvetica", 30), anchor= "center")
        text.place(x=100,y=400)

if __name__ == "__main__":
    Game()