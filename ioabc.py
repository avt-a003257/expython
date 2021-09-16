import sys

filename = input('Input a filename: ')
print('output to ', filename)
file = open(filename, 'w')
#file = open(filename, 'a')

name = input('Input your name: ')
print('Your name: ', name)
file.write(name + '\n')

height = input('Input your height: ')
print('Your height: ', height)
file.write(height + '\n')

file.close()
