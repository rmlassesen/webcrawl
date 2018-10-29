# Description
WebCrawler, recursively scans the standard URLs on a webpage, and then continues to scan the webpages linked to by the URLs, until reaching a specified depth

# Requirements
WebCrawler requires a Python interpreter.  
It has the following dependencies:  
* pprint
* webbrowser
* threading
* flask 
* re (RegEx)
* requests
* bs4 (BeautifulSoup)
* time
* matplotlib
* networkx
* collections
* argparse

# Installation
Clone or Pull this repository

# Usage
Run from CLI
```pythion main.py url-to-start-from ```

Use ```python main.py -h``` to see additional options  
  
Example: Diplay the results in a webbrowser, and search from pythex.org to a depth of 3  
``` python main.py http://www.pythex.org -d 3 --serve ```

# Results
Default CLI execution returns a pretty printed nested dictionary of located URLs and displays a NetworkX Graph

# TODO
  1. Include workforce distribution: Pool of Workers
  2. Optimize HTTP display
