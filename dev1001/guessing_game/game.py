import random as r
import datetime as d
import colorama as c

guesses = []
sec_num = r.randint(1,20)

def guess_outcome(guess):
    if guess > sec_num:
        print('Too high!')
    elif guess < sec_num:
        print('Too low!')
    else: 
        print(c.Fore.GREEN + f'Heck yeah partner! You guessed correctly in {len(guesses)} guesses! You\'re a great cowdoy!')
        end_time = d.datetime.now()
        print(f'You played for {end_time - start_time} seconds!')
        print(c.Style.RESET_ALL)
        quit()

print(c.Fore.MAGENTA + 'Howdy partner! Y\'all ready to play some cowboy guessin\'?' + '\n' + 'I\'ve rustled up a number \'tween 1 and 20! You got y\'rself 5 guesses partner!' + c.Style.RESET_ALL)
start_time = d.datetime.now()

while True:  
    guess = int(input(f'Guess {len(guesses)+1}: '))
    if guess >= 1 and guess <= 20:
        guesses.append(guess)
        guess_outcome(guess)
        print(c.Fore.RED + f'Guesses remaining: {5 - len(guesses)}' + c.Style.RESET_ALL)
        if len(guesses) >=5: 
            print(c.Fore.RED + f'You missed out this time there partner! \n' + f'The secret number was: {sec_num}!')
            end_time = d.datetime.now()
            print(f'You played for: {(end_time - start_time)} seconds!')
            print(c.Style.RESET_ALL)
            break
    else:
        print('Your number is not quite right there partner, try again!')




