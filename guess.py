import random

def lotto_numbers():
    lotto_nums = []
    for num in range(10):
        lotto_nums.append(random.randint(1,10))    
    return lotto_nums

def guess():
    guessCount = 0
    user_guesses = []
    while guessCount <= 2:
        user_guesses.append(input('Enter your guess from 1 to 10 (guess ' + str(guessCount+1) + '/3)'))
        guessCount += 1
    return user_guesses

def compareGuesses(numbers,guesses):
    result = []
    for num in numbers:
        guess_loop = 0
        for guess in guesses:
            if int(guess) == int(num):
                result.append(num)
                break
            else:
                guess_loop += 1
                if guess_loop == 3:
                    result.append(0)
    return result

def main():
    numbers = lotto_numbers()
    guesses = guess()
    results = compareGuesses(numbers,guesses)
    
    print('\nLotto        :',numbers)
    print('Results      :',results)

main()