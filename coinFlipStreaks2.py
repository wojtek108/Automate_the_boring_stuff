import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    flipList = []
    for i in range(100):
        toss = random.randint(0, 1)
        flipList.append(toss)

    for n in range(95):
        if flipList[n] == flipList[n+1] == flipList[n+2] == flipList[n+3] ==flipList[n+4] == flipList[n+5]:
            numberOfStreaks = numberOfStreaks + 1
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
