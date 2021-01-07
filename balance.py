import os
import time
import cd
secs = 0.0

def add(number):
    File = open(f'{cd.files}Balance.txt', 'r')
    bob = (File.read())
    bob_int = float(bob)
    add = bob_int + number
    os.remove(f'{cd.files}Balance.txt', 'r')
    time.sleep(secs)
    new = open(f'{cd.files}Balance.txt', 'r')
    new.write(f'{add}')
    File.close()
    new.close()
    
    return(f'Balance: {add}')
    


def subcract(number):
    File = open(f'{cd.files}Balance.txt', 'r')
    bob = (File.read())
    bob_int = float(bob)
    add = bob_int - number
    if add >= 0:
        os.remove(f'{cd.files}Balance.txt', 'r')
        time.sleep(secs)
        new = open(f'{cd.files}Balance.txt', 'r')
        new.write(f'{add}')
        File.close()
        new.close()
        
        return(f'Balance: {add}')
    else:
        
        return('Not Enough Funds')

def starting(number):
    file = open(f'{cd.files}Balance.txt', 'r')
    file.write(f'{number}')
    file.close()


def Balance():
    File = open(f'{cd.files}Balance.txt', 'r')
    bob = (File.read())
    bob_int = float(bob)
    File.close()
    return bob_int

