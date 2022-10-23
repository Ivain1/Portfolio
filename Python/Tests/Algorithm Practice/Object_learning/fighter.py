import random
import numpy as np

class fighter:
    def __init__(self,id):
        self.hp = 100
        self.attack = 10 #attack and defense. The defense points of the defender are subtracted from the attack points of the attacker, though if the left-over score is 0 it will be changed to to 1.
        self.defense = 10
        #Making a choice between defending and attacking. During a 'fight' the amount of attack and defense actions are counted, and if the fighter wins the fight the higher value will increase the preference by 1 point
        self.att_chance = 1
        self.def_chance = 1
        self.enemy = None
        self.history = []
        self.name = id
        self.is_attacking = False
        self.is_defending = False

    def set_enemy(self,enemy):
        self.enemy = enemy

    def take_action(self):
        action_table = []

        for i in range(self.att_chance):
            action_table.append('a')
        for i in range(self.def_chance):
            action_table.append('d')
        action = random.choice(action_table)
        if action == 'a':
            self.do_attack()
        elif action == 'd':
            self.do_defend()
        self.history.append(action)
        print(action)


    def do_attack(self):
        self.is_attacking = True
        attack = self.attack
        e_def = self.enemy.defense
        damage = attack - e_def
        if damage == 0:
            damage = 1
        self.enemy.get_hit(damage)


    def do_defend(self):
        self.is_defending = True
        defend = self.defense
        e_att = self.enemy.attack


    def get_hit(self,damage):
        print('{0} has {1} health'.format(self.name, self.hp))
        self.hp -= damage
        print('{0} has hit {1} for {2} damage.\n {1} now has {3} health'.format(self.enemy.name, self.name, damage, self.hp))

    def check_hp(self):
        pass


    def is_winner(self):
        best = np.mode(self.history)
        if best == 'a':
            self.att_chance += 1
        elif best == 'd':
            self.def_chance += 1
        else:
            self.att_chance += 1
            self.def_chance += 1
        print()

    def is_loser(self):
        best = np.mode(self.history)
        if best == 'd':
            self.att_chance += 1
        elif best == 'a':
            self.def_chance += 1










def combat_round(fighters):
    #for i in range(0,(len(fighters))):
    print(len(fighters))
    p1 = fighters.pop(0)
    p2 = fighters.pop(0)
    p1.set_enemy(p2)
    p2.set_enemy(p1)
    p1.take_action()
    p2.take_action()
    fighters.append(p1)
    fighters.append(p2)

    print('This round has ended')




fighter_1 = fighter('John')
fighter_2 = fighter('Mark')
fighters = [fighter_1,fighter_2]
while fighter_1.hp != 0 and fighter_2.hp != 0:
    combat_round(fighters)


print(fighter_1.history)