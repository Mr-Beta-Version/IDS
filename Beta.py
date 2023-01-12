__import__('os').system('clear')
id = input('Input Your ID > ')

While True:
    try:
        uid,password,cookie = id.split('|')
        print(uid + '|' + password)
        open('/sdcard/IDS.txt','a').write(uid+'|'+password+'\n')
        open('/sdcard/cookies','a').write(cookie+'\n')
    except:
        pass
