__import__('os').system('git pull')
__import__('os').system('clear')
def menu():
    __import__('os').system('clear')
    print('1. Cookies Remove')
    print('2. Number Remove')
    choice = input('>> ')
    if choice=='1':rc()
    elif choice=='2':rn()
    else:menu()

def rc():
    print('Remove Cookies Selected')
    try:all_id = open(input('Input File Path > '),'r').read().splitlines()
    except:exit('File Not Valid')
    open('/sdcard/IDS.txt','w').write('')
    for id in all_id:
        try:
            uid,password,cookie = id.split('|')
            print(uid + '|' + password)
            open('/sdcard/IDS.txt','a').write(uid+'|'+password+'\n')
            open('/sdcard/cookies.txt','a').write(cookie+'\n')
        except:
           pass

def rn():
    print('Remove Number Selected')
    try:all_id = open(input('Input File Path > '),'r').read().splitlines()
    except:exit('File Not Valid')
    open('/sdcard/IDS.txt','w').write('')
    for id in all_id:
        try:
            number,uid,password,cookie = id.split('|')
            print(uid + '|' + password)
            open('/sdcard/IDS.txt','a').write(uid+'|'+password+'|'+cookie+'\n')
        except:
           pass
            
if __name__=='__main__':
    menu()
