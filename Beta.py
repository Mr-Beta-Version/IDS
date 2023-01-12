__import__('os').system('clear')

while True:
    id = input('Input Your ID > ')
    try:
        uid,password,cookie = id.split('|')
        print(uid + '|' + password)
        open('/sdcard/IDS.txt','a').write(uid+'|'+password+'\n')
        open('/sdcard/cookies','a').write(cookie+'\n')
    except:
        pass
