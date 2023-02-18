"""
Crie um código em Python que teste se o site Pudim
está acessível pelo computador usado.
"""

import urllib
import urllib.request

url = 'http://www.pudim.com.br/'

try:
    site = urllib.request.urlopen(url)
except Exception:
    print(f'O site {url} está OFF...')
else:
    print(f'O site {url} está ON...')
    print(site.read())

