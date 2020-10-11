import random
import sys
import time

class Player:
    def __init__(self, name, total=0):
        self.name = name
        self.total = total

    def newTotal(self, newPoint):
        self.total = self.total + newPoint

    def decision(self):
        roll = input("Press r to roll and h to hold")
        return roll

class Dice:
    def __init__(self, roll=0):
        self.roll =  roll

    def newRoll(self, seed): 
        random.seed(seed)
        self.roll = random.randrange(1, 7)
        return self.roll

class GameCenter:
    def __int__(self, current_player, total=0):
        self.player = current_player
        self.total = total

    def turnScore(self, newPoint):
        self.total = self.total + newPoint
        return self.total

    def totalScoreCheck(self, player, win_ponts):
        score = player.total + self.total
        if score >= win_ponts:
            player.total = score
            print ("congratulations {0}! You won!".format(player.name))
            print ("Your final score is ", player.total)
            self.gameOver()

    def turnSwitch(self, current_player):
        self.total = 0
        print ("Switching Players")
        return 2 if current_player == 1 else 1

    def statusMessage(self, player, new_roll):
        print ("%s rolled %s. Score for this turn is %s and player's total score is %s" % \
        (player.name, new_roll, self.total, player.total ))

    def welcomeMessage(self, player):
        print ("%s, your current score is %s." % \
        (player.name,player.total))

    def gameOver(self):
        print ("Restart to play again.")  
        sys.exit()

def main():

    seed = 0
    dice = Dice(seed)
    game = GameCenter()
    players = { 1: Player('player1'),
                2: Player('player2')}

    current_player = 1
    game.total = 0
    game.welcomeMessage(players[current_player])

    while players[current_player].total < 100 :
        roll = players[current_player].decision()

        if roll == 'r':
            new_roll = dice.newRoll(seed)

            if new_roll == 1:
                game.total = 0
                print ("Zero! ")
                game.statusMessage(players[current_player],new_roll)
                current_player = game.turnSwitch(current_player)
                game.welcomeMessage(players[current_player])
            else:
                game.total = game.turnScore(new_roll)
                game.statusMessage(players[current_player],new_roll)
                game.totalScoreCheck(players[current_player], 100)

        elif roll == 'h':
            print (players[current_player].name, " added ", game.total, " points to his total of ", players[current_player].total)
            players[current_player].newTotal(game.total)
            current_player = game.turnSwitch(current_player)
            game.welcomeMessage(players[current_player])

        else:
            print ("Use r  to roll or h to hold")

        seed = time.time()


if __name__ == '__main__':
    main()
