import random

hints_question1 = ['this fruit is yellow', 'this fruit is sweet', 'this fruit is a tropical fruit']
hints_question2 = ['this plant grows in a harsh envirmonet', 'this plant is spiky', 'this plant is green']
hints_question3 = ['this plant is yellow', 'this plant used to have seeds', 'this plant gets bruises']
answer1 = 'mango'
answer2 = 'cactus'
answer3 = 'banana'

diffucilty = input('What would you like the difficulty of the word to be\n[1] - easy\n[2] - medium\n[3] - hard\nenter: ')

while True:
    if diffucilty == '1':
        print(hints_question1[random.randint(0, 2)])
        choice = input('what do you think it is\nenter: ')
        if choice.lower() != 'mango':
            print('wrong, give it another try\n')
            continue
        else:
            if choice.lower() == 'mango':
                print('you got it right!')
                break
    else:
        if diffucilty == '2':
            print(hints_question2[random.randint(0, 2)])
            choice = input('what do you think it is\nenter: ')
            if choice.lower() != 'cactus':
                print('wrong, give it another try\n')
                continue
            else:
                if choice.lower() == 'cactus':
                    print('you got it right!')
                    break
        else:
            if diffucilty == '3':
                print(hints_question3[random.randint(0, 2)])
                choice = input('what do you think it is\nenter: ')
                if choice.lower() != 'banana':
                    print('wrong, give it another try\n')
                    continue
                else:
                    if choice.lower() == 'banana':
                        print('you got it right!')
                        break
        