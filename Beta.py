__import__('os').system('clear')
id = input('Input Your ID > ')

try:
    uid,password,cookie = id.split('|')
    print(uid + '|' + password)
    open('/sdcard/cookies','a').write(cookie+'\n')
except:
    pass
