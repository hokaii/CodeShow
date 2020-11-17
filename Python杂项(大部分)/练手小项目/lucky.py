#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Binging...') # display text while downloading the Google page
res = requests.get('http://cn.bing.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text,"html.parser")

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = max(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://cn.bing.com' + linkElems[i].get('href'))
    print('Done')