import random

numberOfStreaks = 0
for experimentNumber in range(10000):
    tossList = []
    for t in range(1, 101):
        toss = random.randint(0, 1)
        tossList.append(toss)

    for i in range(0, 95):
        streakList = []
        for n in range(0, 6):
            streakList.append(tossList[n+i])
        if sum(streakList) == 0 or sum(streakList) == 6:
            numberOfStreaks = numberOfStreaks + 1

print('Number of streaks = ' + str(numberOfStreaks))
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
