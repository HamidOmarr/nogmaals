import random
ronde = 0
win = 0
verlies = 0
tries = 0
while ronde <= 19:
    ronde = ronde + 1
    tries = 0
    randomcijfer = random.randrange(1,1000)
    print (randomcijfer)
    print('Ronde:' , ronde)
    print ('Win:' , win)
    print ('verlies:' ,verlies)
    print ('tries:' ,tries)

    while tries <= 9:
        tries = tries + 1
        gokvraag = int(input('Gok de getal tussen 1,1000'))
        if gokvraag != randomcijfer:
            print ('Je hebt het niet geraden, Probeer het nog een keer.')
            print (randomcijfer)
            print ('tries:' ,tries)
            if (gokvraag - randomcijfer) < 50 and (gokvraag - randomcijfer) > -50 :
                print ('Je bent warm.')
            if (gokvraag - randomcijfer) < 20 and (gokvraag - randomcijfer) > -20 :
                print ('Je bent heel warm.')


        elif gokvraag == randomcijfer:
            print ('Geweldig, je hebt het geraden.')
            win = win + 1
            tries = 10
            verdergaan = input('Nog een getal raden?')
            if verdergaan == "ja" :
                continue
            else:
                exit()

        elif gokvraag != randomcijfer and tries >= 9:
            print ('Helaas, deze ronde heb je niet geraden.')
            verlies = verlies + 1
            verdergaan = input('Nog een getal raden?')
            if verdergaan == 'ja':
                continue
            else:
                exit()