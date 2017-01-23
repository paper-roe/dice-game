from time import sleep
import sys
import os
import msvcrt

roll = ['._.', '\:', '|:', '/:', '.-.', ':\\', ':|', ':/', '._.']

while True:
    ws = ['']
    index = 0
    for pic in roll:
        if msvcrt.kbhit():
            break
        os.system('cls')
        print(''.join(ws), pic), sys.stdout.flush()
        if index != 8:
            ws.append(' ')
        index += 1
        sleep(0.3)

    for pic in reversed(roll):
        if msvcrt.kbhit():
            break
        os.system('cls')
        print(''.join(ws), pic), sys.stdout.flush()
        del ws[-1]
        sleep(0.3)
