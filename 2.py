
import urllib.request
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
from collections import Counter

def get_soup(url):
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response.read(), 'lxml')
        return soup
    except:
        return None
   
    

def all_links(soup):
    foundUrls = [link["href"]  for link in soup.find_all("a", href=lambda href: href and not href.startswith("#"))]
    return foundUrls

def get_text(soup):
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text().replace(',', '').replace(' ', '').replace('\n', '').lower()
    return text


def get_all_words(soup):
      for script in soup(["script", "style"]):
          script.extract()
      words = Counter(soup.get_text().replace(',', '').split())
      return words

def get_length_wordt(soup):
    for script in soup(["script", "style"]):
          script.extract()
    words = soup.get_text().replace(',', '').split()
    mass = [];
    for word in words:
        mass.append(len(word))
    return Counter(mass)


def draw_plot(values, lbx='xplot', lby='yplot'):
    plt.bar(range(len(values)), list(values.values()))
    plt.xlabel(lby)
    plt.ylabel(lbx)
    plt.xticks(range(len(values)), list(values.keys()))
    plt.show()

all_l = 0
all_s =0
all_w = Counter()
all_leng = Counter()
    
def dypth_url(url, dypth):
    global all_l
    global all_s
    global all_w
    global all_leng
    if dypth == -1:
        return None
    else:   
        soup_l = get_soup(url)
        dypth -=1
        if soup_l is not None :
            print('count links =', len(all_links(soup_l)))
            all_l = all_l + len(all_links(soup_l))
            print('count symbols on page = ', len(get_text(soup_l)))
            all_s = all_s + len(get_text(soup_l))
            all_w = all_w + get_all_words(soup_l)
            all_leng = all_leng + get_length_wordt(soup_l)
            for li in all_links(soup_l):
                dypth_url(li, dypth)
            
    
    
    
      
def main():

    url = 'http://unrealinteractive.com/'
    dypth_url(url, 0)
    plt.figure(figsize=(40,10))
    plt.bar(all_w.keys(), all_w.values())
    plt.figure(figsize=(40,10))
    plt.bar(all_leng.values(), all_leng.keys())
    print('count links on ALL PAGE =',all_l)
    print('count symbols on page ALL PAGE = ', all_s)
    
if __name__ == '__main__':
    main()
    

