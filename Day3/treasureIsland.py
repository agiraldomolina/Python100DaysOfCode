import os
os.system('cls')
print('Welcome to Treasure Island.')
print('Your mission is to find the treasure.')
print("You're at a cross road. Where do you want to go? Type \"left\" or \"right\".")
if input().lower() != 'left':
    print("You fall into a hole.\n")
    msg='Game over'
else:
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if input().lower() != 'wait':
        print("You were attacked by a trout.\n")
        msg='Game over'
    else:
        color = input('You arrived at the island underharmed. There is a house with three doors. One red, one yellow and one blue. Which color do you choose? Type "red" or "yellow" or "blue".\n').lower()
        if color=='red':
            print('You were burned by fire.\n')
            msg='Game over'
        elif color=='yellow':
            print('You were eaten by beasts.\n')
            msg = 'Game over'
        elif color=='blue': 
            print('You found the treasure. Congratulations!\n')
            msg=' You win!'
        else:
            print("Game over.")
            msg='Game over'

print('                              ,-----.')
print('                            ('+ msg +')                        .-.')

print('''                             `------' _                         \ \ 
                                     (_)                         \ \ 
                                         O                       | |
                    |\ /\                  o                     | |
    __              |,\(_\_                  . /\---/\   _,---._ | |
   ( (              |\,`   `-^.               /^   ^  \,'       `. ;
    \ \             :    `-'   )             ( O   O   )           ;
     \ \             \        ;               `.=o=__,'            \ 
      \ \             `-.   ,'                  /         _,--.__   \ 
       \ \ ____________,'  (                   /  _ )   ,'   `-. `-. \ 
        ; '                ;                  / ,' /  ,'        \ \ \ \ 
        \                 /___,-.            / /  / ,'          (,_)(,_)
         `,    ,_____|  ;'_____,'           (,;  (,,)     
       ,-" \  :      | :
      ( .-" \ `.__   | |
       \__)  `.__,'  |__)  




''')