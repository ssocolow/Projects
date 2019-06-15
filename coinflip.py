import random
import time

t = time.clock()
f = 0
howmanytimes = 0
def main():
    global howmanytimes
    howmanytimes = int(input('how many times do you want to flip the coin?   '))
    flip(howmanytimes)

def flip(w):
    global howmanytimes
    yes = 0
    no = 0
    for j in range(w):
        random.seed()
        x = random.getrandbits(1)
        if x == 1:
            yes += 1
        else:
            no += 1
        #print(x)
        u = abs(yes-no)
        global f
        if u > f:
            f = u

    print()
    print('Heads: ' + str(yes))
    print('Tails: ' + str(no))
    print('The absolute value of the percent difference between heads and tails was ' + str((f/howmanytimes)*100) + '%')
    print('The difference was ' + str(abs(yes-no)))

main()
t2 = time.clock()
print('This took ' + str(t2 - t) + ' seconds')
