import random
import time
from tkinter import *

class Game:
    def __init__(self,master):
        #super(Game,self).__init__()
        self.master = master
        self.w = 500
        self.h = 500
        self.n = random.randint(0,100)
        self.g = []
        self.p1_guess = 0
        self.p2_guess = 0
        self.p1_name = 'Player 1'
        self.p2_name = 'Player 2'

        #Instantiating the Game Frame
        game_frame = Frame(self.master, bg='black', border=0)
        game_frame.pack(fill=BOTH,expand=True)

        #game_name = Label(game_frame, bg='black', fg='gainsboro', padx = 5, pady = 5)
        #game_name.pack(side=TOP, fill=BOTH, expand=True)

        #Instantiating Player 1's Frame
        number_frame = LabelFrame(game_frame, text='The number is', bg='purple')
        number_frame.pack(side=TOP, fill=BOTH, expand=True)


        self.P1 = Frame(game_frame, bg='darkred', border=0)
        self.P2 = Frame(game_frame, bg='darkblue', border=0)
        self.name_1 = Label(self.P1, text='Player 1', bg='darkred', fg='mistyrose', font=('Verdana',16))
        self.name_2 = Label(self.P2, text='Player 2', bg='darkblue', fg='aliceblue', font=('Verdana',16))


        self.P1_submit = Button(self.P1, text='Submit Guess', padx=10, pady=10, font=('Verdana',16), fg='mistyrose',bg='darkred', command= self.compare)
        self.P2_submit = Button(self.P2, text='Submit Guess', padx=10, pady=10, font=('Verdana', 16), fg='aliceblue',bg='darkblue', command=lambda: compare(True))




        '''
        self.P1.pack(side=LEFT, fill=BOTH, expand=True)
        self.name_1.pack(side=TOP, fill=X, expand=False)
        P1_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)

        self.P2.pack(side=RIGHT, fill=BOTH, expand=True)
        self.name_2.pack(side=TOP, fill=X, expand=False)
        P2_submit_button.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)'''
    def GuessList(self):
        list = self.g
        for i in range(len(list)):
            print(list[i])


    def PlayerOne(self):
        self.P1 = Frame(game_frame, bg='darkred', border=0)
        self.name_1 = Label(self.P1, text='Player 1', bg='darkred', fg='mistyrose', font=('Verdana', 16))
        self.one = Entry(self.P1, text=P1_num, bg='mistyrose', fg='darkred', font=('Verdana', 14))
        self.master.mainloop()


    def Size(self):
        return('{0}x{1}'.format(self.w,self.h))

    def setSize(self,width=500,height=500):
        self.w = width
        self.h = height

    def numberReset(self):
        self.n = random.randint(0,100)

    def P1_turn(self):
        self.P1.pack(side=LEFT, fill=BOTH, expand=True)
        self.name_1.pack(side=TOP, fill=X, expand=False)
        self.P1_submit.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)

    def P2_turn(self):
        self.P2.pack(side=RIGHT, fill=BOTH, expand=True)
        self.name_2.pack(side=TOP, fill=X, expand=False)
        self.P2_submit.pack(side=BOTTOM, padx=10, pady=10, fill=X, expand=False)


    def game_start(self):
        self.master.geometry('{0}x{1}'.format(self.w,self.h))
        self.master.mainloop()

    def compare(self,P2_turn = False):
        if P2_turn == True:  # This is to check whose turn it is.
            player = player_name_2
            other_player = player_name
            P2_turn = False
            print('{0}, it is your turn to guess'.format(player))
        else:
            player = player_name
            other_player = player_name_2
            P2_turn = True
            print('{0}, it is your turn to guess'.format(player))
m = Tk()
game = Game(m)


#m = Tk()
# function defining section
# setting up variables
player_name = 'Player 1'
player_name_2 = 'Player 2'
P2_turn = False
the_number = random.randint(0, 100)  # This one's the most important
player = player_name
other_player = player_name_2
# Score-keeping: I choose to use a list because it allows me to keep track of what the actual guess was, as well as the total amount of guesses (by the length of the list).
score1 = [player_name]
score2 = [player_name_2]
guess = -1
# Decorative printing for in the console. May be removed later if I get a fully functioning Tkinter interface


#1game = Frame(m, bg='darkslateblue')
#p1_Frame = LabelFrame(1game, bg='darkblue', fg='mistyrose', text='Player 1')
#p2_Frame = LabelFrame(1game, bg='darkred', fg='aliceblue', text='Player 2')
#game_content = [m,1game, p1_Frame, p2_Frame]

'''
def game_start(content=[]):
    m = content[0]
    game = content[1]
    p1_Frame = content[2]
    p2_Frame = content[3]

    game.pack(fill=BOTH, expand=True)
    p1_Frame.pack(side=LEFT, fill=BOTH, expand=True)
    p2_Frame.pack(side=RIGHT, fill=BOTH, expand=True)

    m.mainloop()


#game_start(game_content)


def setMenu():
    game.pack_forget()
    menu = Frame(m, bg='gray')
    menu_t = Label(menu, text='Guess That Number', bg='darkslategray', fg='gainsboro')
    menu_b = Button(menu, text='Start Game', bg='darkslategray', fg='gainsboro')
    menu_e = Button(menu, text='Exit', bg='darkslategray', fg='gainsboro')
    menu_list = [menu, menu_t, menu_b, menu_e]
    return (menu_list)

def executeMenu(contents=[]):
    menu = contents[0]
    menu_t = contents[1]
    menu_b = contents[2]
    menu_e = contents[3]

    menu.pack(fill=BOTH, expand=True)
    menu_t.pack(fill=BOTH, expand=True)
    menu_b.pack(fill=BOTH, expand=True)
    menu_e.pack(fill=BOTH, expand=True)

    m.mainloop()

def PlayerNames():
    player_name = input('Player 1, please share your name here: ')
    player_name_2 = input('Player 2, please share your name here: ')
    names = [player_name, player_name_2]
    return (names)
    
'''
#The actual game mechanics
Game.n = random.randint(0,100)

if __name__ == '__main__':
    # menu_content = setMenu()
    # executeMenu(menu_content)

    # menu.pack(fill=BOTH, expand = True)
    # menu_t.pack(fill=BOTH, expand = True)
    # menu_b1.pack(fill=BOTH, expand = True)
    # menu_b2.pack(fill=BOTH, expand = True)
    # menu_e.pack(fill=BOTH, expand = True)
    guess = -1
    P2_turn = False
    player_name = 'Player 1'
    player_name_2 = 'Player 2'

    #raw_game_time = time.time()
    # current_time = time.localtime(raw_game_time)
    #game_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(time.time()))
    #print('This game is starting at {0}'.format(game_time))
    # The core 'game loop', this is where the magic happens. It will keep running until guess is equal to the number. After that it will close down.
    while guess != Game.n:
        try:
            one = Entry(game.P1, textvariable=game.p1_guess, bg='mistyrose', fg='darkred', font=('Verdana', 14))
            one.pack(side=TOP, fill=X, expand=False, padx=5, pady=5)

            two = Entry(game.P2, textvariable=game.p2_guess, bg='aliceblue', fg='darkblue', font=('Verdana', 14))
            two.pack(side=TOP, fill=X, expand=False, padx=5, pady=5)


            if P2_turn == True:  # This is to check whose turn it is.
                player = player_name_2
                other_player = player_name
                game.P2_turn()
                P2_turn = False
                # print('{0}, it is your turn to guess'.format(player_name_2))
            else:
                player = player_name
                other_player = player_name_2
                game.P1_turn()
                P2_turn = True

                # print('{0}, it is your turn to guess'.format(player_name))

            '''guess_text = input('{0}, guess a number between 0 and 100: '.format(
                player))  # this is where the player whose turn it is will insert their guess
            guess = int(guess_text)'''
            if guess < the_number:  # Check if the guessed number is lower than the correct number
                print('{0}, your guess of {1} is too low, try higher!'.format(player, guess))

            elif guess > the_number:  # Check ig the guessed number is higher than the correct number
                print('{0}, your guess of {1} is too high, try lower!'.format(player, guess))
            else:  # If neither of the above is true, then the number must be correct, therefore act as if it is.

                if P2_turn == True:
                    guess_total = len(
                        score1)  # Check the total amount of guesses of the winning player, including the current turn.
                    total_2 = len(
                        score2) - 1  # Check the total guesses of the losing player, NOT including the current turn since it would've been their turn next.
                    print(
                        'Correct, the number was {0}, {1} wins with a total of {2} guesses\n, while {3} had {4} guesses'.format(
                            the_number, player, guess_total, other_player, total_2))
                    #game_duration = time.strftime("%H:%M:%S", time.localtime(
                        #time.time() - raw_game_time))  # Faulty attempt at checking the duration of the game.
                    #print(game_duration)
                else:
                    guess_total = len(score2)
                    total_2 = len(score1) - 1
                    print(
                        'Correct, the number was {0}, {1} wins with a total of {2} guesses\n, while {3} had {4} guesses'.format(
                            the_number, player, guess_total, other_player, (total_2)))
                    #game_duration = time.strftime("%H:%M:%S", time.localtime(time.time() - raw_game_time))
                    #print(game_duration)

            if P2_turn == True:  # After each turn, append the score of the person whose turn it is
                score1.append(guess)
                print(score1)
            else:
                score2.append(guess)
                print(score2)

            game.game_start()


        except ValueError:  # In case the input is NOT an integer,
            print('{0}, Your input of {1} is not a number, that cost you your turn, sorry'.format(player, guess_text))
            if P2_turn == True:
                score1.append('N/A')
                print(score1)
            else:
                score2.append('N/A')
                print(score2)
#print('This game has ended at {0}'.format(game_time))

