from time import sleep
import sys
import os
import msvcrt

roll = ['._.', '\:', '|:', '/:', '.-.', ':\\', ':|', ':/']

while True:
    ws = ['']
    index = 0
    roll_right = 0
    roll_left = 0

    while roll_right < 2:
        for pic in roll:
            if msvcrt.kbhit():
                break
            
            os.system('cls')
            print(''.join(ws), pic), sys.stdout.flush()
            ws.append(' ')
            if roll_right == 1 and index == 7:
                sleep(0.15)
                os.system('cls')
                print(''.join(ws), roll[0]), sys.stdout.flush()

            index += 1
            if index > 7:
                index = 0
                
            sleep(0.15)
            
        roll_right += 1        

    while roll_left < 2:
        index = 7
        for pic in reversed(roll):
            if msvcrt.kbhit():
                break

            if roll_left == 0 and index == 7:
                os.system('cls')
                print(''.join(ws), roll[0]), sys.stdout.flush()
                sleep(0.15)
            del ws[-1]     
            os.system('cls')
            print(''.join(ws), pic), sys.stdout.flush()

            index -= 1

            sleep(0.15)

        roll_left += 1
