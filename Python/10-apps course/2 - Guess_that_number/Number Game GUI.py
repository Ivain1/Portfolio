import random
from tkinter import *

class Game:
    def __init__(self,master):
        #super(Game,self).__init__()
        self.master = master
        self.s = False #Is the game running?
        self.w = 500 #Gemoetry of the game 'object', aka the frame
        self.h = 500
        self.n = random.randint(0,100) #The number to be guessed
        self.g1 = [] #The list of guesses for player 1, started with the player's name
        self.g2 = [] #Ditto for player 2
        self.p1_name = StringVar() #The name variable for player 1, starts out  as named exactly that.
        self.p2_name = StringVar()
        print(self.s)
        self.game_frame = Frame(self.master, bg='black', border=0)

        self.menu = Frame(self.master, bg='black', border=1)


        self.title = Label(self.menu, text='Guess that Number Game', bg='purple', fg='lavender', font=('Verdana', 16))  # The title of the game
        self.player_name_1 = Label(self.menu,text='Player 1',bg='purple', fg='lavender', font=('Verdana', 16))  # The layout of the player names and the option to change them
        self.name1 = Entry(self.menu, textvariable=self.p1_name, fg='mistyrose', bg='darkred')
        self.player_name_2 = Label(self.menu, text='Player 2', bg='purple', fg='lavender', font=('Verdana', 16))
        self.name2 = Entry(self.menu, textvariable=self.p2_name, fg='aliceblue', bg='darkblue')

        self.p1_name = self.name1.get()
        self.p2_name = self.name2.get()
        self.title.pack(fill=BOTH, expand=True, padx=20,pady=5)
        self.player_name_1.pack(fill=BOTH,expand=True, padx=20,pady=5)
        self.name1.pack(fill=BOTH,expand=True,padx=20,pady=5)
        self.player_name_2.pack(fill=BOTH,expand=True,padx=20,pady=5)
        self.name2.pack(fill=BOTH,expand=True,padx=20,pady=5)





        if self.s == False: #If the game is not running, then it is in the menu.

            self.menu.pack(fill=BOTH,expand=True)
            '''
            self.title = Label(menu_frame, text='Guess that Number Game') #The title of the game
            self.player_name_1 = Label(menu_frame, text=self.p1_name) #The layout of the player names and the option to change them
            self.name1 = Entry(menu_frame, textvariable=self.p1_name ,fg='mistyrose', bg='darkred')
            self.player_name_2 = Label(menu_frame, text=self.p2_name)
            self.name2 = Entry(menu_frame, textvariable=self.p2_name, fg='aliceblue', bg='darkblue')
            self.p1_name = self.name1
            self.p2_name = self.name2
            '''
        else:
            self.game_frame.pack(fill=BOTH,expand=True)



        #Instantiating the Game Frame
        '''if self.s == True:

            game_frame.pack(fill=BOTH,expand=True)'''

        #game_name = Label(game_frame, bg='black', fg='gainsboro', padx = 5, pady = 5)
        #game_name.pack(side=TOP, fill=BOTH, expand=True)

        #Instantiating Player 1's Frame
        number_frame = LabelFrame(self.game_frame, text='The number is', bg='purple')
        number_frame.pack(side=TOP, fill=BOTH, expand=True)


        self.P1 = Frame(self.game_frame, bg='darkred', border=0)
        self.P2 = Frame(self.game_frame, bg='darkblue', border=0)
        name_1 = Label(self.P1, text=self.p1_name, bg='darkred', fg='mistyrose', font=('Verdana',16))
        name_2 = Label(self.P2, text=self.p2_name, bg='darkblue', fg='aliceblue', font=('Verdana',16))

        self.P1.pack(side=LEFT, fill=BOTH, expand=True)
        self.P2.pack(side=RIGHT, fill=BOTH, expand=True)
        name_1.pack(side=TOP, fill=X, expand=False)
        name_2.pack(side=TOP,fill=X,expand=False)


        #Instantiating the buttons
        #P1_submit_button = Button(self.P1, text='Submit Guess', padx=10, pady=10, font=('Verdana',16), fg='mistyrose',bg='darkred')
        #P2_submit_button = Button(self.P2, text='Submit Guess', padx=10, pady=10, font=('Verdana', 16), fg='aliceblue',bg='darkblue')

        #P1_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)
        #P2_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)
    def submit_names(self):
        print(self.p1_name)
        print(self.p2_name)

    def GuessList(self):
        list = self.g
        for i in range(len(list)):
            print(list[i])


    def PlayerOne(self):
        self.P1 = Frame(game_frame, bg='darkred', border=0)
        self.name_1 = Label(self.P1, text=self.p1_name, bg='darkred', fg='mistyrose', font=('Verdana', 16))
        self.one = Entry(self.P1, text=P1_num, bg='mistyrose', fg='darkred', font=('Verdana', 14))


    def Size(self):
        return('{0}x{1}'.format(self.w,self.h))

    def setSize(self,width=500,height=500):
        self.w = width
        self.h = height

    def numberReset(self):
        self.n = random.randint(0,100)

    def gameStart(self):
        print(self.p1_name,self.p2_name)
        self.s = True
        self.menu.pack_forget()
        self.game_frame.pack(fill=BOTH,expand=True)


if __name__ == "__main__":

    root = Tk()

    root.title("Guess that Number game")

    #root.geometry('600x800')
    #menu = Frame(root, bg='purple')
    #menuTitle = Label(menu, text='Guess that Number Game', font=('Verdana', 16, 'bold'), bg='purple', fg='lavender')

#    menu.pack()

    game = Game(root)
    game.setSize(500,500)
    root.geometry(game.Size())
    P2_turn = False
    game.submit = Button(game.menu, text='Submit', command=game.gameStart)
    game.submit.pack(fill=BOTH, expand=True, padx=20, pady=5)
    #game.submit.config(command=game.gameStart())



    P1_num = -1
    P2_num = -1
    # Initiating the guessing Frames
    game.one = Entry(game.P1, textvariable=P1_num, bg='mistyrose', fg='darkred', font=('Verdana', 14))
    game.two = Entry(game.P2, textvariable=P2_num, bg='AliceBlue', fg='darkBlue', font=('Verdana', 14))

    game.one.pack(side=TOP, padx=10, pady=10, fill=X, expand=True)
    game.two.pack(side=TOP, padx=10, pady=10, fill=X, expand=True)

    def swapTurn(turn = False):
        if turn == True:
            game.P1.pack_forget()
            game.P2.pack(side=RIGHT,expand=True,fill=BOTH)
            print('It is now the turn of player 2')

        else:
            game.P2.pack_forget()
            game.P1.pack(side=LEFT,expand=True,fill=BOTH)
            print('it is now the turn of player 1')

    swapTurn()

    def P1_guess():
        p1_guess = int(game.one.get())
        the_number = int(game.n)
        print(the_number)
        print(p1_guess)
        game.g1.insert(0, p1_guess)
        print(game.g1)
        if p1_guess > the_number:
            print('too high')
        elif p1_guess < the_number:
            print('too low')
        else:
            print('correct!')
            return(True)
        swapTurn(True)
        P1_num = 0

    def P2_guess():
        p2_guess = int(game.two.get())
        the_number = int(game.n)
        print(the_number)
        print(p2_guess)
        game.g2.insert(0,p2_guess)
        print(game.g2)
        if p2_guess > the_number:
            print('too high')
        elif p2_guess < the_number:
            print('too low')
        else:
            print('correct!')
            return(True)
        swapTurn(False)
        P2_num = 0

    #submission buttons
    P1_submit_button = Button(game.P1, text='Submit Guess', padx=10, pady=10, font=('Verdana', 16), fg='mistyrose',bg='darkred', command= lambda: P1_guess())
    P2_submit_button = Button(game.P2, text='Submit Guess', padx=10, pady=10, font=('Verdana', 16), fg='aliceblue',bg='darkblue', command= lambda: P2_guess())

    P1_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)
    P2_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)

    print(game.g1)
    print(game.g2)
    #P1_won = P1_submit_button
    #P2_won = P2_submit_button

    root.mainloop()