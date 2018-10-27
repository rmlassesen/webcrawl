import argparse

parser = argparse.ArgumentParser(description='WebCrawler: Crawl the Web')
parser.add_argument('url', metavar='URL', type=str  ,
                    help='the URL/webpage from where to initiate the WebCrawler')
parser.add_argument('-d','--depth', metavar='N', dest='depth', nargs='?', type=int,
                    help='depth of the WebCrawl - default is 2', default=2)
parser.add_argument('-f','--figuresize', metavar='N,N', dest='figuresize', nargs='?', type=str,
                    help='size of the NetworkX graph - default is 12,12', default='12,12')
