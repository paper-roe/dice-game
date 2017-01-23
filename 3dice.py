import random
import sys
import os

def val_error():
    print('* Must enter a number')

def roll_dice(dice_kept):
    # keeping extra code which is currently unnecessary because i want to run this
    # function instead of reroll_dice()
    # Clear all dice, check how many the player has kept and re-roll remaining
    die = []
    dice_available = 6 - len(dice_kept)
    while dice_available > 0:
        die.append(random.randint(1,6))
        dice_available -= 1

    # check if all dice rolled same number
    perfect_roll = 0
    any_dice = die[0]
    for dice in die:
        if any_dice != dice:
            perfect_roll = 0
            break
        perfect_roll = 1
    if perfect_roll == 1:
        dice_kept = [-1]
        end_game_results(dice_kept)   
        
    return die

def reroll_dice(dice_kept):
    # Clear all dice, check how many the player has kept and re-roll remaining
    die = []
    dice_available = 6 - len(dice_kept)
    while dice_available > 0:
        die.append(random.randint(1,6))
        dice_available -= 1

    print('Dice rolled:', die)
    keep_dice(dice_kept, die)

def keep_dice(dice_kept, die):
    num_kept = 0

    # player must keep at least 1 dice
    while num_kept == 0:
        # horrible try/except block that takes up soo many lines
        # because there are multiple input sections. need better way
        while True:
            try:
                keep = int(input('Keep which dice value? (Must choose at least 1)\n'))
                break
            except ValueError:
                val_error()
                continue
        # check if player selected a value that was rolled
        while valid_dice_check(keep, die) != 1:
            while True:
                try:
                    keep = int(input('Invalid dice, choose again\n'))
                    break
                except ValueError:
                    val_error()
                    continue
        # increment dice kept this roll, add dice to player's collection,
        # remove dice from available dice to keep
        num_kept += 1
        dice_kept.append(keep)
        die = remove_dice(die, keep)
        # if choice was last dice available
        if len(die) == 0:
            end_game_results(dice_kept)
        print_score(dice_kept)
        print('Dice left:', die)

    # check for additional dice to keep
    while keep != 0:
        while True:
            try:
                keep = int(input('Keep which dice value? (0 to re-roll unkept dice)\n'))
                break
            except ValueError:
                val_error()
                continue
        # if player wants to keep a dice
        if keep != 0:
            # check if player selected a value that was rolled
            while valid_dice_check(keep, die) != 1:
                while True:
                    try:
                        keep = int(input('Invalid dice value, choose again (0 to re-roll)\n'))
                        break
                    except ValueError:
                        val_error()
                        continue
                if keep == 0:
                    break
            # increment dice kept this roll, add dice to player's collection,
            # remove dice from available dice to keep
            num_kept += 1
            dice_kept.append(keep)
            die = remove_dice(die, keep)
            # if choice was last dice available
            if len(die) == 0:
                end_game_results(dice_kept)
            print_score(dice_kept)
            print('Dice left:', die)
        else:
            break

    print_score(dice_kept)
    
    # re roll dice. would like to rerun main as it sets everything
    # nicely, but dice_kept becomes forgotten rerunning main because
    # init is now set to 1 and rerunning init_gmae() will clear kept values
    reroll_dice(dice_kept)

def valid_dice_check(keep, die):
    for dice in die:
        if keep == dice:
            return 1

def remove_dice(die, keep):
    index = 0
    for dice in die:
        if keep == dice:
            del die[index]
            break
        index += 1
    return die

def print_score(dice_kept):
    score = 0
    for val in dice_kept:
        if val == 3:
            continue
        score += val
    print('\n=========')    
    print('Score:', score)
    print('=========')  

def end_game_results(dice_kept):
    play_again = -1

    print_score(dice_kept)

    # will not accept 1 or 0. why? i don't know. it prints the entry 1 or 0
    # but still loops
    #while play_again != 1 or play_again != 0:
        #play_again = int(input('\n1 to Play again, 0 to exit'))

    while True:
        try:
            play_again = int(input('\n1 to play again, any number to exit: '))
            break
        except ValueError:
            val_error()
            continue
    
    if play_again == 1:
        global init
        init = 0
        os.system('cls')
        main()
    else:
        sys.exit()

def init_game():
    dice_kept = []
    score = 0
    global init
    init = 1

    return dice_kept, score
        
def main():
    if init == 0:
        dice_kept, score = init_game()
    
    die = roll_dice(dice_kept)
    print('Dice rolled:', die)

    # send currently kept dice and currently rolled dice to
    # check which ones to keep
    dice_kept = keep_dice(dice_kept, die)

init = 0
main()