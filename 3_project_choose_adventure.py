#use triple single quotes to make multiple lines. Don't forget to use them at the bottom.
#print giraffe 

def shiny():
    print('As you walk towards the shiny object, you realize that it is a beautiful sword made of pure gold.')


print('''
                          _- _ , - . _
                        `,% o` ~~-_,'.'
                        % %@ - % %, -'%,
                       ,-, . _ --\ -.%
              P^=.     `'"   |+|'    `
              ||             |+|
              ||             |+|
              ||             |+|
        ______/|             |+|
       `| ___ ,/             |+|
        ||   ||              |+|
        ||   ||              |+|
________||___||___.__________/H|____
''')

print("Welcome to your safari adventure!")

intro = input("You enter the jungle and find a trail that leads three different directions. Type Left, Right, or Straight").lower()
if intro == 'left':
    print('As you start walking towards the left, a dark mist starts to surround you.')

elif intro == 'right':
    print('You start walking forward. You notice something shiny in the distance.')
    cont = input("Do you want to walk towards the shiny object? (Y/N): ").lower()
    if cont == 'y':
        shiny()
    else:
        print('Your lack of curiosity betrays you. A giraffe comes from behind and tramples you.')
        print('Game over...')
        quit()
    
      
