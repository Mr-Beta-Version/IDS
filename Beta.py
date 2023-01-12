__import__('os').system('git pull')
__import__('os').system('clear')

try:all_id = open(input('Input File Path > '),'r').read().splitlines()
except:exit('File Not Valid')

for id in all_id:
    try:
        uid,password,cookie = id.split('|')
        print(uid + '|' + password)
        open('/sdcard/IDS.txt','a').write(uid+'|'+password+'\n')
        open('/sdcard/cookies','a').write(cookie+'\n')
    except:
        pass
