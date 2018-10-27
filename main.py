from lib import *
from pprint import pprint

if __name__ == '__main__':
    args = usage.parser.parse_args()
    fsizes = args.figuresize.split(',')
    figuresize = (int(fsizes[0]), int(fsizes[1]))

    crawler = webcrawl.Crawl(args.url, args.depth)

    progression.o.extend({'pretty': pprint})
    progression.monitor(crawler, crawler.crawl, 'pretty')

    crawler.graph(figuresize).show()