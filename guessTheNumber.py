import os
import random

class Function():

    def screenClear():
        os.system('clear' if os.name == 'posix' else 'cls')

    def lineBreak():
        print('')

class Header():

    def title():
        print(str('Guess the Number Game').upper())

    def levelStat():
        print('Level:',str(level))

    def game():
        Header.title()
        Function.lineBreak()
        Header.levelStat()
        Function.lineBreak()

    def gameOvr():
        Header.title()
        Function.lineBreak()
        print('Game Over!')

class Game():

    def setup():
        global level,points,minNum,maxNum,guesses

        level = 0
        points = 0
        minNum = 0
        maxNum = 5
        guesses = 4

    def generateNewRandomNum():
        global randomNum
        randomNum = random.randint(minNum,maxNum)

    def gameOver():
        Function.screenClear()
        Header.gameOvr()
        Function.lineBreak()
        print('The randomly choosen number was:',str(randomNum))
        for line in range(2):
            Function.lineBreak()
        cont = input('Would you like to play again? (y/n) ')
        if cont == 'y':
            Game.setup()
            Game.main()
        elif cont == 'n':
            Game.setup()
            Game.mainMenu()

    def main():
        global guesses,randomNum,points,maxNum,level
        Function.screenClear()
        Header.game()
        Game.generateNewRandomNum()
        print('Your computer has chosen a number between'+' '+str(minNum)+' '+'and'+' '+str(maxNum)+'.')
        print('Try and guess the number!')
        while guesses > 0:
            Function.lineBreak()
            guess = int(input('Enter your guess: '))
            if guess == randomNum:
                if points == 3:
                    level += 1
                    maxNum += 5
                    points = 0
                    Game.generateNewRandomNum()
                    Function.screenClear()
                    Header.game()
                    print('Your computer has chosen a number between'+' '+str(minNum)+' '+'and'+' '+str(maxNum)+'.')
                else:
                    print('Your guess is correct!')
                    guesses = 4
                    points += 1
                    Game.generateNewRandomNum()
                    print('Your computer has chosen a new number between'+' '+str(minNum)+' '+'and'+' '+str(maxNum))
            else:
                print('Oops, the number that you guessed is not the chosen number.')
                guesses -= 1
        Game.gameOver()

    def mainMenu():
        options = ['Exit','Start game']
        Function.screenClear()
        Header.title()
        for line in range(2):
            Function.lineBreak()
        print('Program options:')
        Function.lineBreak()
        for counter,option in enumerate(options):
            print('  '+str(counter)+'.'+' '+option)
        Function.lineBreak()
        userInput = input('Enter selection: ')
        if userInput == '0':
            Program.quit()
        elif userInput == '1':
            Game.main()

class Program():

    def quit():
        Function.screenClear()
        exit()

    def start():
        Game.setup()
        Game.mainMenu()

Program.start()
