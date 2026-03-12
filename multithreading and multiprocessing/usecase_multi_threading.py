'''
Real-World Examples: Multithreading for I/O-bound Tasks
Scenario : Web Scraping
Web scraping often involves making numerous network requests to fetch web pages. These tasks are I/O-bound because they spend a lot of time waiting for 
response form the servers. Multithreading can significantly imporve the performance by allowing multiple web pages to be fetched concurrently.
'''

'''
https://en.wikipedia.org/wiki/The_Buddha
https://en.wikipedia.org/wiki/Gurkha
https://en.wikipedia.org/wiki/Mount_Everest
'''
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://en.wikipedia.org/wiki/The_Buddha',
    'https://en.wikipedia.org/wiki/Gurkha',
    'https://en.wikipedia.org/wiki/Mount_Everest'
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f'Fetched {len(soup.text)} characters form {url}')

threads = []

for url in urls:
    thread = threading.Thread(target = fetch_contents, args = [url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All threads are fetched')