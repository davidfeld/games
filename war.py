import random
import time

#slow = True
slow = False

player1 = raw_input('Player 1 name: ')
player2 = raw_input('Player 2 name: ')
rank = range(13)
suit = range(4)
rankR = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suitR = ['c','d','h','s']

deck = [[i,j] for i in rank for j in suit]
deckR = [[i,j] for i in rankR for j in suitR]

def printcards(card1, card2):
    ind1 = deck.index(card1)
    ind2 = deck.index(card2)
    print deckR[ind1][0]+deckR[ind1][1]+'  vs.   '+deckR[ind2][0]+deckR[ind2][1]

def printwarchest():
    #warRind = [deck.index(i) for i in warchest]
    #for i in warRind:
        #print deckR[i][0]+deckR[i][1]
    print ', '.join([deckR[deck.index(i)][0]+deckR[deck.index(i)][1] for i in warchest])

p1, p2 = [], []
while len(p1) < len(deck)/2:
    card = random.choice(deck)
    if card not in p1: 
        p1.append(card)
for i in deck:
    if i not in p1:
        p2.append(i)
random.shuffle(p2)

warchest = []
#print p1
print ""
#print p2
count = 1
while (len(p1) != 0 and len(p1) != len(deck)):
    print '-------------------------------------------------------'
    print 'Hand #: '+str(count)
    count += 1
    p1card = p1[0]
    p2card = p2[0]
    printcards(p1card, p2card)
    if p1card[0] > p2card[0]:
        p1.append(p2card)
        p1.append(p1card)
        p1.remove(p1card)
        p2.remove(p2card)
        print player1+' takes it.'

    elif p2card[0] > p1card[0]:
        p2.append(p1card)
        p2.append(p2card)
        p2.remove(p2card)
        p1.remove(p1card)
        print player2+' takes it.'

    else:
        warchest.append(p1card)
        warchest.append(p2card)
        p1.remove(p1card)
        p2.remove(p2card)

        while len(warchest) > 0:
            print 'WAR!!!!!'
            if slow: time.sleep(5)
            if len(p1) <= 4 or len(p2) <= 4:
                ncard = min(len(p1), len(p2))
                p1card, p2card = p1[ncard-1], p2[ncard-1]
                printcards(p1card, p2card)

                for i in range(ncard):
                    warchest.append(p1[i])
                    warchest.append(p2[i])
                for i in range(ncard):
                    p1.remove(p1[0])
                    p2.remove(p2[0])
                if len(p1) > len(p2) and p1card[0] >= p2card[0]: 
                    p1= range(len(deck))
                elif len(p2) > len(p1) and p2card[0] >= p1card[0]: 
                    p2 = range(len(deck))
                elif p1card[0] > p2card[0]:
                    for i in warchest:
                        p1.append(i)
                    printwarchest()
                    print player1+' takes it!!'
                elif p2card[0] > p1card[0]:
                    for i in warchest:
                        p2.append(i)
                    printwarchest()
                    print player2+' takes it!!'
                warchest = []

            else:
                p1card, p2card = p1[3], p2[3]
                printcards(p1card, p2card)

                for i in range(4):
                    warchest.append(p1[i])
                    warchest.append(p2[i])
                for i in range(4):
                    p1.remove(p1[0])
                    p2.remove(p2[0])

                if p1card[0] > p2card[0]:
                    for i in warchest:
                        p1.append(i)
                    printwarchest()
                    print player1+' takes it!!'
                    warchest = []
                elif p2card[0] > p1card[0]:
                    for i in warchest:
                        p2.append(i)
                    printwarchest()
                    print player2+' takes it!!'
                    warchest = []
    print player1+' has',len(p1), player2+' has', len(p2)
    #time.sleep(5)

    if slow: blah = raw_input('')
    print ''


if len(p2) == 52: print player2+' WINS!!!!!'
else: print player1+' WINS!!!!!'
print '\n\n\n\n'
