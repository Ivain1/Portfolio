import random
import time
from tkinter import *

m = Tk()
m.geometry('500x500')
#function defining section
#setting up variables
player_name = 'Player 1'
player_name_2 = 'Player 2'
P2_turn = False
the_number = random.randint(0,100) #This one's the most important
player = player_name
other_player = player_name_2
#Score-keeping: I choose to use a list because it allows me to keep track of what the actual guess was, as well as the total amount of guesses (by the length of the list).
score1 = [player_name]
score2 = [player_name_2]
guess = -1
#Decorative printing for in the console. May be removed later if I get a fully functioning Tkinter interface
game_running = False

game = Frame(m,bg='darkslateblue')
p1_Frame = LabelFrame(game,bg='darkblue',fg='mistyrose', text='Player 1')
p2_Frame = LabelFrame(game,bg='darkred',fg='aliceblue', text='Player 2')
game_content = [game,p1_Frame,p2_Frame]



def start():
    return(True)

def setMenu():
    game.pack_forget()
    menu = Frame(m, bg='gray')
    menu_t = Label(menu, text='Guess That Number', bg='darkslategray', fg='gainsboro')
    menu_b = Button(menu, text='Start Game', bg='darkslategray', fg='gainsboro', command=start)
    menu_e = Button(menu, text='Exit', bg='darkslategray', fg='gainsboro')
    menu_list = [menu,menu_t,menu_b,menu_e]
    return(menu_list)


def executeMenu(contents = []):
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
    names = [player_name,player_name_2]
    return(names)

def game_start(content=[]):
    game = content[0]
    p1_Frame = content[1]
    p2_Frame = content[2]
    menu.pack_forget()

    game.pack(fill=BOTH, expand=True)
    p1_Frame.pack(side = LEFT, fill = BOTH, expand = True)
    p2_Frame.pack(side = RIGHT, fill = BOTH, expand = True)

    m.mainloop()

#menucontent = setMenu()
#executeMenu(menucontent)

'''if game_running == True:
    game_start(game_content)'''
menu_content = setMenu()
executeMenu(menu_content)

#menu.pack(fill=BOTH, expand = True)
#menu_t.pack(fill=BOTH, expand = True)
#menu_b1.pack(fill=BOTH, expand = True)
#menu_b2.pack(fill=BOTH, expand = True)
#menu_e.pack(fill=BOTH, expand = True)
#decorative prints before the actual game starts

'''
print('')
print('---o-----o-0-O-0-o-----o---')
print('---o Guess That Number o---')
print('---o-----o-0-O-0-o-----o---')
print('')

print('')
print('---o-----o-0-O-0-o-----o---')
print('---o Guess That Number o---')
print('---o {0} vs {1} o---'.format(player_name,player_name_2))
print('---o-----o-0-O-0-o-----o---')
print('-----o  Game Start!  o-----')
print('')
raw_game_time = time.time()
#current_time = time.localtime(raw_game_time)
game_time = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(time.time()))
print('This game is starting at {0}'.format(game_time))
#The core 'game loop', this is where the magic happens. It will keep running until guess is equal to the number. After that it will close down.

while guess != the_number:
    try: #In case some smart-ass tries to insert a non-integer number, this will break their turn and log a N/A in their score.
        if P2_turn == True: #This is to check whose turn it is.
            player = player_name_2
            other_player = player_name
            P2_turn = False
            #print('{0}, it is your turn to guess'.format(player_name_2))
        else:
            player = player_name
            other_player = player_name_2
            P2_turn = True
            #print('{0}, it is your turn to guess'.format(player_name))

        guess_text = input('{0}, guess a number between 0 and 100: '.format(player)) #this is where the player whose turn it is will insert their guess
        guess = int(guess_text)
        if guess < the_number: #Check if the guessed number is lower than the correct number
            print('{0}, your guess of {1} is too low, try higher!'.format(player, guess))

        elif guess > the_number: #Check ig the guessed number is higher than the correct number
            print('{0}, your guess of {1} is too high, try lower!'.format(player, guess))
        else: #If neither of the above is true, then the number must be correct, therefore act as if it is.

            if P2_turn == True:
                guess_total = len(score1) #Check the total amount of guesses of the winning player, including the current turn.
                total_2 = len(score2) -1 #Check the total guesses of the losing player, NOT including the current turn since it would've been their turn next.
                print('Correct, the number was {0}, {1} wins with a total of {2} guesses\n, while {3} had {4} guesses'.format(the_number, player, guess_total, other_player, total_2))
                game_duration = time.strftime("%H:%M:%S",time.localtime(time.time() - raw_game_time)) #Faulty attempt at checking the duration of the game.
                print(game_duration)
            else:
                guess_total = len(score2)
                total_2 = len(score1) -1
                print('Correct, the number was {0}, {1} wins with a total of {2} guesses\n, while {3} had {4} guesses'.format(the_number,player,guess_total,other_player,(total_2)))
                game_duration = time.strftime("%H:%M:%S", time.localtime(time.time() - raw_game_time))
                print(game_duration)



        if P2_turn == True: #After each turn, append the score of the person whose turn it is
            score1.append(guess)
            print(score1)
        else:
            score2.append(guess)
            print(score2)


    except ValueError: #In case the input is NOT an integer,
        print('{0}, Your input of {1} is not a number, that cost you your turn, sorry'.format(player,guess_text))
        if P2_turn == True:
            score1.append('N/A')
            print(score1)
        else:
            score2.append('N/A')
            print(score2)
print('This game has ended at {0}'.format(game_time))
'''