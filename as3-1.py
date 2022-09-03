import random

num=random.randint(1,30)
for i in range (6):
    n=int(input('enter your number : '))
    if n==num :
        print ('Its true')
        break
    else:
        print('its false . Try agin') 
else:
    print( 'Number is : ',num , ' looooossser ')           

