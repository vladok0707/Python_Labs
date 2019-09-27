import collections
import re
import urllib.request
from bs4 import BeautifulSoup
from requests import request
import matplotlib.pyplot as plt
from collections import Counter

def get_soup(url):
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), 'lxml')
    return soup

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

def main():
    url = 'http://unrealinteractive.com/'
    print('count links =', len(all_links(get_soup(url))))
    all_l = len(all_links(get_soup(url)))
    print('count symbols on page = ', len(get_text(get_soup(url))))
    all_s = len(get_text(get_soup(url)))
    #plt.figure(figsize=(40,10))
    #plt.bar(get_all_words(get_soup(url)).keys(), get_all_words(get_soup(url)).values())
    all_w = get_all_words(get_soup(url))
    #plt.figure(figsize=(40,10))
    #plt.bar(get_length_wordt((get_soup(url))).values(), get_length_wordt((get_soup(url))).keys())
    all_leng = get_length_wordt((get_soup(url)))
    for number in range(5):
        l = all_links(get_soup(url))[number]
        print('count links =', len(all_links(get_soup(l))))
        all_l = all_l + len(all_links(get_soup(l)))
        print('count symbols on page = ', len(get_text(get_soup(l))))
        all_s = all_s + len(get_text(get_soup(l)))
        all_w = all_w + get_all_words(get_soup(l))
        all_leng = all_leng + get_length_wordt((get_soup(l)))
    plt.figure(figsize=(40,10))
    plt.bar(all_w.keys(), all_w.values())
    plt.figure(figsize=(40,10))
    plt.bar(all_leng.values(), all_leng.keys())
    print('count links on ALL PAGE =',all_l)
    print('count symbols on page ALL PAGE = ', all_s)
    
if __name__ == '__main__':
    main()
    

