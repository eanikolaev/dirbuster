# coding: utf-8
import os, requests


def get_not404(site='sfera-mail.ru', proto='http'):
    filenames = os.listdir('wordlists')
    for filename in filenames:
        for line in open('wordlists/'+filename):
            path = line.rstrip()
            url = proto + '://' + site + '/' + path
            r = requests.get(url)
            if r.status_code != 404:
                print r.status_code, url


def get_subdomains(site='sfera-mail.ru', proto='http'):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    for f in chars:
        for s in chars:
            for t in chars:
		url = proto + '://' + f + s + t + '.' + site
                try:
      		    r = requests.get(url)
   		    if r.status_code != 404:
		        print r.status_code, url

                except requests.exceptions.ConnectionError:
                    pass


def get_unusual(inp_name, site='sfera-mail.ru', proto='http'):
    for line in open(inp_name):
        url = line.split(' ')[1]
        r = requests.get(url)
        text = r.text.encode('utf-8')
        if not '<strong>404</strong>' in text and not '<strong>403</strong>' in text:
            print '--------------------'
            print url
            print r.status_code
#            print text


if __name__ == '__main__':
#    get_not404()
#    get_subdomains()
    get_unusual('not404urls')
