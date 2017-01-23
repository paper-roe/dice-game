import rooms
import sys

def check_room():
    actual_room = False
    while not actual_room:
        try:
            room_no = int(input('Which room? ' +
                             '\n1) Circle' +
                             '\n2) Square' +
                             '\n3) Triangle' +
                             '\n4) Exit\n'))
        except ValueError:
            continue

        if room_no > 0 and room_no < 5:
            actual_room = True
    return room_no

def enter_room(room_no):
    if room_no == 1:
        rooms.circle_room()
    elif room_no == 2:
        rooms.square_room()
    elif room_no == 3:
        rooms.triangle_room()
    else:
        sys.exit()

def main():
    while True:
        room_no = check_room()
        enter_room(room_no)
        cont = input('Enter any key to continue\n')

if __name__ == '__main__':
    main()