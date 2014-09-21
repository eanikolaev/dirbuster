import os

def dirbuster(site='sfera-mail.ru'):
    filenames = os.listdir('wordlists')
    for filename in filenames:
        for line in open('wordlists/'+filename):
            print line.rstrip()

if __name__ == '__main__':
    dirbuster()
