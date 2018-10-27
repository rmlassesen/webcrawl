import re, requests
from bs4 import BeautifulSoup
from lib.graph import make_graph as mg

class Crawl:
    def __init__(self, url, depth):
        self.starturl = url
        self.depth = depth

        self.visited = []
        self.spun = {url: None}

        self.progress = 'Idle'

    def crawl(self):
        self.progress = 'Initiating Crawl on ' + self.starturl
        self.spun, self.visited = getList(self, self.spun, -1)
        self.progress = None


    def graph(self, figuresize):
        self.graphplot, self.url_list, self.unique_urls = mg(self.spun,figuresize)
        return self.graphplot





def request_soup(url):
    try:
        request = requests.get(url)
    except:
        return None


    if request.status_code != 200:
        return None

    soup = BeautifulSoup(request.content,'html5lib')
    return soup


def getLinks(url):
    soup = request_soup(url)
    if not soup:
        return None

    links = {}
    reg = re.compile(r'^(http://)')

    for link in soup.select('a'):
        url = str(link.get('href'))
        if reg.match(url):
            links[url] = None


    return links


def getList(object, templist, deep):
    visited, depth = object.visited, object.depth

    deep += 1
    if templist:
        for url in templist:
            if url not in visited:
                templist[url] = getLinks(url)
                visited.append(url)
                object.progress = 'Visited: ' + url + ' in depth ' + str(deep)

                if deep < depth:
                    templist[url], visited = getList(object, templist[url], deep)


    return templist, visited
