import random
di = range(1,7)

pointOn = False
point = 0
go = True
points = [4,5,6,8,9,10]
craps = [2,3,12]
betnames = ['pass', 'odds', 'field', '4','5','6','8','9','10']
bets = [10 for i in betnames]
bankroll = 1000

def rolldice():
    di1 = random.choice(di)
    di2 = random.choice(di)
    roll = di1+di2
    return roll



def payout(roll, pointOn, point, bankroll):
    if pointOn:
        if roll == point:
            bankroll += bets[ betnames.index('pass') ]
            if roll == 4 or roll == 10: bankroll += 2*bets[ betnames.index('odds') ]
            if roll == 5 or roll == 9: bankroll += 1.5 * bets[ betnames.index('odds') ]
            if roll == 6 or roll == 8: bankroll += 1.2 * bets[ betnames.index('odds') ]
        elif roll == 7:
            bankroll -= bets[ betnames.index('pass') ]
    elif roll == 7 or roll == 11:
        bankroll += bets[ betnames.index('pass') ]
    elif roll in craps:
        bankroll -= bets[ betnames.index('pass') ]

    return bankroll

maxBR, count, maxroll = 0, 0, 0

while bankroll > 0:
    count += 1
    roll = rolldice()

    if pointOn: 
        if bets[ betnames.index('odds') ] == 0: bankroll -= 20
        bets[ betnames.index('odds') ] = 20
    else: bets[ betnames.index('odds') ] = 0 

    bankroll = payout(roll, pointOn, point, bankroll)
    if bankroll > maxBR: 
        maxBR = bankroll
        maxroll = count
    if pointOn:
        if roll == point or roll == 7:
            pointOn = False
            point = 0

    elif roll in points:
        pointOn = True
        point = roll

    if point == 0: pointstr = 'Off'
    else: pointstr = str(point)

    print '------------------------------------    Roll # '+str(count)+'  ---------------------------------------\n' 


    
    print '\t'.join(betnames)
    print '\t'.join([str(i) for i in bets])
    print '\n\n\n'

    print 'Roll: ', roll, '\t\t\t\t', 'Point: ',  pointstr
    print 'Bankroll: ', bankroll
    print '\n\n\n\n'
    
    
    #for i in range(len(betnames)):
    #    print betnames[i], ' - ', i
    #bet = raw_input('Bets?')
    roll_now = raw_input('Hit enter to roll:')
    print '\n\n\n\n'


#print maxBR, maxroll
