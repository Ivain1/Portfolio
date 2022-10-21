from random import randint
from tkinter import *

class game_controller:
    def __init__(self):
        self.p1 = 'player 1'
        self.p1_guess = 0
        self.p2_guess = 0
        self.number = randint(0,100)
        self.m = Tk()
        self.f = Frame(self.m,bg='purple')
        self.p1_frame = Frame(self.f,bg='red')
        self.p2_frame = Frame(self.f,bg='blue')

    def loop(self):
        self.m.mainloop()

    def set_name(self,player, name):
        p_name = Entry()


    def guess(self,player,guess):
        if player == 1:
            self.p1_guess = Entry(self.p1_frame, text=variable)
            self.p1_guess.pack()




def main():
    game1 = game_controller
    #p1_name = ask_name(root, 1)
    #p2_name = ask_name(root, 2)
    number = set_number()
    while p1_turn != number and p2_turn != number:
        p1_turn()
        p2_turn()
    display_highscore()



def setup_UI():
pass



def ask_name(game_frame, player=1):
    p1_name = Entry(game_frame)

    p1_name = input("Player 1, Choose your name: ")
    print('Player 1 has chosen the name {}'.format(p1_name))
    p2_name = input("Player 2, Choose your name: ")
    print('Player 2 has chosen the name {}'.format(p2_name))
    return([p1_name,p2_name])

def set_number():
    return(randint(0,100))

def p1_turn():
    pass
def p2_turn():
    pass
def display_highschore():
    pass


main()