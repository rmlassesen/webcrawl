from lib import *
from pprint import pprint
from server import Server
import threading

global server
server = Server()

def set_progress(setas):
    global server
    server.progress = setas

    return True


if __name__ == '__main__':
    args = usage.parser.parse_args()
    fsizes = args.figuresize.split(',')
    figuresize = (int(fsizes[0]), int(fsizes[1]))

    crawler = webcrawl.Crawl(args.url, args.depth)
    plots = html.Plot_Handler()

    progression.o.extend({'pretty': pprint})
    progression.o.extend({'progress': set_progress})

    if not args.serve:
        progression.monitor(crawler, crawler.crawl, 'pretty')
        crawler.graph(figuresize).show()
        pprint(crawler.spun)

    else:

        class Thread_1(threading.Thread):
            def __init__(self, name):
                threading.Thread.__init__(self)
                self.name = name

            def run(self):
                global server
                progression.monitor(crawler, crawler.crawl, 'progress')
                graph_div = plots.new_plot(crawler.graph(figuresize))
                server.html_add = graph_div

        class Thread_2(threading.Thread):
            def __init__(self, name):
                threading.Thread.__init__(self)
                self.name = name

            def run(self):
                server.app.run()


        thread1 = Thread_1("thread_1")
        thread2 = Thread_2("thread_2")

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

