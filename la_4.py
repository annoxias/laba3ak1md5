from random import randint

i=0
while i<3:
    a=randint(1, 100)
    b=randint(1, 100)
    print(a,"+",b, "=")
    res = int(input())
    if a + b != res:
        i=i+1

    if i==3:
        print('game over')