# This code helps to play the game and find number. Game should be played between 2 people, one of them entering them number and another one guessing itimport randomprint('''Game started !Please enter your number and ask your friend to find it :''')while True:    try:        a=int(input())        break    except ValueError:        print('Please enter integer value')print('\n'*100)c=random.randint(5,500)i=1if a>0:    print('Please guess the number, it is between 0 and '+str(a+c)+' you will have 10 chances to find it :')if a<=0:    print('Please guess the number, it is between 0 and '+str(a-c)+' you will have 10 chances to find it :')while i<=10:    b=int(input())    if b!=a and i==10:        print('Please contact with administrator')    elif b>a:        print('Lower, '+str(10-i)+' chances left')    elif b<a:        print('Higer, '+str(10-i)+' chances left')    else:        print('Congratulations ! In '+str(i)+' attempts you found it, it was '+str(b))        break    i+=1input('Press enter to close the program')