from bs4 import BeautifulSoup, SoupStrainer
from collections import defaultdict

urldict = defaultdict(int)

filelist = ['yt-historyp1-2021.html', 'yt-historyp2-2021.html']

for fname in filelist:
    with open(fname, encoding='utf-8') as fcurr:
        all_links = BeautifulSoup(fcurr, 'html.parser', parse_only=SoupStrainer('a'))
        for link in all_links:
            if link.has_attr('href') and not '/channel/' in link['href'] and not 'myaccount.google' in link['href']:
                urldict[link['href']] += 1

    
top100 = sorted(urldict.items(), key=lambda kv: kv[1], reverse=True)[:100]
for rank in top100:
    print(f'{rank[0]} - {rank[1]} views')