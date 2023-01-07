name = input('Hello, what is your name?')
print(f'Welcome to the INTERGALACTIC Escape Room, {name}!')
#password puzzle + description message
print('You enter an empty dark room...')
print() #this is another way to skip a line 
print('There is something glowing in the corner')

direction = input('There are 4 doors in front of you one of them leads to the exit the other 3 leads to your demise which one are you choosing? (Door 1, Door 2, Door 3, or Door 4')

if direction == 'Door 1':
  print('You walk through Door 1 there you fall into hot lava you have died :(')

if direction == 'Door 2':
  print('You walk through Door 2 there are a pit of venomous snakes that attack you. Unfortunately you soon succumb to your injuries you have died :(')
if direction == 'Door 3':
 print('You walk through Door 3 there is a exit, you run out the door and you have successfully escaped the maze, congratulations you survived through the escape room :)')
if direction == 'Door 4':
 print('You walk through Door 4 everything is pitch black and you cannot see anything, you continue walking until you fall into a bottomless pit that never and your stuck there for all eternity :(')

#password puzzle
