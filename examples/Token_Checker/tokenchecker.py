import threading
from wrapper import *

threads = []
f = open('valid.txt', 'a+')

def checker(token):
    dc = Discord(str(token.rstrip()))
    output = dc.check_token()

    print(output)
    
    if output['status'] == 'Valid': 
        f.write('{token}\n'.format(token=output['token']))

def main():
    for token in open('tokens.txt', 'r').readlines():
        threads.append(
            threading.Thread(target=checker, args=(token.strip(),))
        )

    for t in threads: t.start()
    for t in threads: t.join()

    f.close()

if __name__ == '__main__':
    main()