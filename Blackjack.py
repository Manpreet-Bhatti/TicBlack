
# coding: utf-8

# In[11]:

class Player(object):
    
    def __init__(self, bank = 1000):
        self.bank = bank
    
    def addbet(self, bet):
        self.bank += bet*2
    
    def minusbet(self, bet):
        self.bank -= bet
        
    def __str__(self):
        return "Your bank is currently at %x" %(self.bank)


# In[12]:

game = Player()


# In[13]:

game.addbet(20)


# In[14]:

game.bank


# In[74]:

import random

class Player(object):
    
    def __init__(self, bank = 1000):
        self.bank = bank
    
    def addbet(self, bet):
        self.bank += bet*2
    
    def minusbet(self, bet):
        self.bank -= bet
        
    def __str__(self):
        return "Your bank is currently at %s" %(self.bank)

l = Player()

def start():
    
    print l
    
    while True:
        
        howmuchbet = raw_input("How much would you like to bet? Please either input: 1, 5, 10, 25, or 100 ")
        
        if howmuchbet != 1 or howmuchbet != 5 or howmuchbet != 10 or howmuchbet != 25 or howmuchbet != 100:
            
            print "Dealing..."
            for x in range(1):
                print "You have been dealt a " ,random.randint(1,11)
            break
            
        else:
            print "Try again - Input either: 1, 5, 10, 25, 100 "
            continue
    
    while True:
        
        standorhit = raw_input("Now, would you like to stand or hit? ").lower()
        
        if standorhit == 'stand':
            break
        
        elif standorhit == 'hit':
            for x in range(1):
                print 'You have been dealt a ' ,random.randint(1,11)
                break
        else:
            print 'Try again - Would you like to stand or hit?'
            continue


# In[75]:

start()


# In[ ]:




# In[ ]:



