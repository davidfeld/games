import random, time
#noplayers = int(raw_input('How many players? '))
playername = 'initial'
playernumber = 1
playerlist = []
while playername != '':
    playername = raw_input('Player '+str(playernumber)+' name: ')
    if playername != '': playerlist.append(playername)
    playernumber += 1


class deck:
     def __init__(self):
          rank = range(13)
          suit = range(4)
          deck = [[i,j] for i in rank for j in suit]
          random.shuffle(deck)
          self.deck = deck

     def dealcards(self, ncards):
          temp = []
          for i in range(ncards):
               temp.append(self.deck[0])
               self.deck = self.deck[1:]
          return temp

class Hand:
     def __init__(self, deck, *args):
          self.rankR = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
          self.suitR = ['c','d','h','s']
          self.status = 0
          self.double = False
          if args:
               self.hand = list(args)
          else:
               self.hand = deck.dealcards(2)

     def hit(self, deck):
          self.hand += deck.dealcards(1)

     def value(self):
          val = 0
          Ace = False
          for card in self.hand:
               rank = card[0]
               if rank < 8: val += rank+2
               elif rank < 12: val += 10
               else:
                    val += 1
                    Ace = True

          if Ace:
               if val+10 > 21:
                    return str(val)
               elif val + 10 == 21:
                    return str(val+10)
               else:
                    return str(val)+'/'+str(val+10)
          else:
               return str(val)

     def display(self):
          handR = ' '.join([self.rankR[card[0]]+self.suitR[card[1]] for card in self.hand])
          return handR

     def dealerdisplay(self):
          handR = ''.join([self.rankR[card[0]]+self.suitR[card[1]] for card in self.hand][0])
          return handR
          #print '\t:', handR

class player:
     def __init__(self, name, deck):
          self.name = name
          self.bankroll = 0
          self.hands = [Hand(deck)]
 
     def splithand(self, deck, hand):
          self.hands.remove(hand)
          hand1 = Hand(deck, hand.hand[0])
          hand2 = Hand(deck, hand.hand[1])
          hand1.hit(deck)
          hand2.hit(deck)
          self.hands.append(hand1)
          self.hands.append(hand2)

class dealer:
    def __init__(self, deck):
        self.hand = Hand(deck)
        if '/' not in self.hand.value() and int(self.hand.value()) == 21:  self.BJ = True
        else: self.BJ = False

class game:
    def __init__(self, args):
        self.Deck = deck()
        self.players = []
        self.explayers = []
        self.handnumber = 0
        for arg in args:
            self.players.append(player(arg, self.Deck))
        self.newhand()

    def newhand(self):
        playOn = True
        while playOn:
            self.Deck = deck()
            self.dealer = dealer(self.Deck)
            self.play()
            x = self.nexthandaction()
            if x == 'q': playOn = False

    def nexthandaction(self):
        while True:
            x = raw_input("To add player enter (a). To remove player enter player's name. Press enter for next hand or (q) to quit: ")
            #x = ''
            names = [playa.name for playa in self.players]
            if x not in names and x not in ['a','q','']:
                print 'Not a valid response.'
            elif x == 'a':
                newname = raw_input('Enter new players name: ')
                self.players.append(player(newname,self.Deck))
            elif x in names:
                self.explayers.append(self.players[names.index(x)])
                self.players.remove(self.players[names.index(x)])
            else:
                return x


    def playbybook(hand):
        dealercard = self.dealer.hand.hand[0]
        if dealercard in [8,9,10,11]: dealercard = 8
        if dealercard == 12: dealercard = 9
        #AA =


    def PrintTable(self, curhand, status, *args):
        print '\n'.join(['' for i in range(30)])
        
        print '####### Hand '+str(self.handnumber)+' ##########'
        if status == 0:
            fakehand = Hand(self.Deck, self.dealer.hand.hand[0])
            print '\t\t\t Dealer Shows:', fakehand.display()
            print '\t\t\t Value:', fakehand.value(),  '\n\n'
        else:
            print '\t\t\t Dealer Shows:', self.dealer.hand.display()
            print '\t\t\t Value:', self.dealer.hand.value(), '\n\n'

        for player in self.players:
            print player.name+' $'+str(player.bankroll)
            for hand in player.hands:
                print '\t Hand:', hand.display()
                if curhand == hand:  print '\t Value:', hand.value(), '\t\t\t\t <---------------------------------- '
                else: print '\t Value:', hand.value()
                print '\n\n'
        #print '\n'.join(['' for i in range(30)])

    def updatebankrolls(self):
        dealerval = int( (self.dealer.hand.value()).split('/')[-1])
        for player in self.players:
            for hand in player.hands:
                if hand.double: bet = 2
                else: bet = 1
                handval = int( (hand.value()).split('/')[-1])
                if handval == 21 and len(hand.hand) == 2 and self.dealer.BJ == False:
                    player.bankroll += bet
                elif handval > 21:
                    player.bankroll -= bet
                elif dealerval > 21:
                    player.bankroll += bet
                elif handval > dealerval:
                    player.bankroll += bet
                elif dealerval > handval:
                    player.bankroll -= bet


    def play(self):
        self.handnumber += 1
        faces = [8,9,10,11]
        for player in self.players:
            player.hands = [Hand(self.Deck)]

        for player in self.players:
            if self.dealer.BJ: break
            while 0 in [hand.status for hand in player.hands]:
                for hand in player.hands:
                    while hand.status == 0:
                        actionstring = ['Hit (h)']
                        actions = ['h','']
                        curhand = hand.hand
                        if len(curhand) == 2:
                            actionstring.append('Double (d)')
                            actions.append('d')
                            if (curhand[0][0] == curhand[1][0]) or (curhand[0][0] in faces and curhand[1][0] in faces):
                                actionstring.append('Split (s)')
                                actions.append('s')

                        if '/' not in hand.value() and int(hand.value()) >= 21:
                            hand.status = 1
                            continue
                    
                        self.PrintTable(hand, 0)

                        action = raw_input('\t\t\t'+' / '.join(actionstring)+': ')
                        #action = 'h'
                        #print '\n\n\n'
                        
                        if action not in actions:
                            print 'Not a valid action.'
                        elif action == 'h':
                            hand.hit(self.Deck)
                            if '/' not in hand.value() and int(hand.value()) >= 21: hand.status = 1
                        elif action == 'd':
                            hand.hit(self.Deck)
                            hand.double = True
                            hand.status = 1
                        elif action == 's':
                            player.splithand(self.Deck, hand)
                            hand.status = 1
                        else:
                            hand.status = 1


        pausetime = 1.5
        self.PrintTable('', 0)
        time.sleep(pausetime)
        self.PrintTable('', 1)
        time.sleep(pausetime)
        
        dealerval = int( (self.dealer.hand.value()).split('/')[-1])
        while dealerval < 17:
            self.dealer.hand.hit(self.Deck)
            self.PrintTable('', 1)
            dealerval = int( (self.dealer.hand.value()).split('/')[-1])
            time.sleep(pausetime)
        
        self.updatebankrolls()
        self.PrintTable('', 1)




game(playerlist)




