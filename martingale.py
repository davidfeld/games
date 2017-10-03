import numpy as np
import random
import matplotlib.pyplot as plt

winlist = []
ntrials = 2000
for i in range(ntrials):
    initial = 2**10-1
    bankroll = 2**10-1
    bet = 1
    threshold = (18./38.)
    wincount = 1

    while bankroll > 0:
    #print bankroll, bet
        roll = random.random()
        if roll > threshold:
            bankroll = bankroll - bet
            bet  *= 2
            #print 'Loss'
        else:
        #bankroll = bankroll + bet
            bankroll = initial
            bet = 1
            wincount += 1
        #print 'Win'
    #x = raw_input('')
    winlist.append(wincount)


winlist.sort()
#print winlist
#print winlist[1000]
print np.mean(winlist), np.median(winlist)
nbins = (max(winlist) - min(winlist))/50
plt.hist(winlist, bins = nbins)
plt.show()

