#-*- coding: utf-8 -*-

my_age = 18
counter = 0
for i in range(10):
    if counter < 3:
        guess_age = int(raw_input('please enter your guess age:'))
        if guess_age == my_age:
            print 'Congratulation, you got it!~'
            break
        elif guess_age > my_age:
            print 'please think smaller.'
        else:
            print 'please think bigger'
    else:
        continue_confirmation = raw_input(
            'You exceed the maximum tries, do you want to continue(y/n): '
        )
        if continue_confirmation == 'y':
            counter = 0
            continue
        else:
            print 'bye'
            break
    counter += 1

print 'Sorry, you use out of all chances!'
