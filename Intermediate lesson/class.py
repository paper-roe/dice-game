class MyClass:
    number = 0
    name = 'noname'

def main():
    me = MyClass()
    me.number = 1337
    me.name = 'Tom'

    friend = MyClass()
    friend.number = 3
    friend.name = 'Steve'

    empty = MyClass()

    print('Name: ' + me.name + ', Favourite Number: ' + str(me.number))
    print('Name: ' + friend.name + ', Favourite Number: ' + str(friend.number))
    print('Name: ' + empty.name + ', Favourite Number: ' + str(empty.number))

if __name__ == '__main__':
    main()