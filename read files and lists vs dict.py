def main():
    performances = {}

    schedule_file = open('schedule.txt', 'r')

    for line in schedule_file:
        (show, time) = line.split(' - ')
        #print(show, time)
        performances[show] = time.strip()

    schedule_file.close() 

    print(performances['Ventriloquism'])

main()

# lists/arrays
l_list = [1,2,3]
print(l_list)

del l_list[0]
print(l_list)

l_list = [1,2,3]
l_list.remove(1)
print(l_list)

print('\n')
# dictionary
dict = {'1':'h','2':'j','3':'k'}
print(dict)

del dict['1']
print(dict)

dict = {'1':'h','2':'j','3':'k'}
print('dict entry for "2" is:', dict['2'])

val = dict.get('3')
print('dict entry for "3" is:', val)

print('\n')
# multi dictionary
multi_dict = {'1': ['a','b'],
              '2': ['c','d'],
              '3': ['e','f']}
print(multi_dict)
print('second list is ', multi_dict['2'])
print('second list, element 2 is', multi_dict['2'][1])