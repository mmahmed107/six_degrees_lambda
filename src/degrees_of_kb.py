'''Web scraper for wikipedia url'''
import re
import random
import json
import urllib3
from bs4 import BeautifulSoup


class KevinBacon6Degrees:
    '''screen scraping for Kevin bacon'''

    def __init__(self, url):
        '''Constructor'''
        if (url is None or url == ""):
            raise ValueError("Please enter a URL")

        self.url = f'https://en.wikipedia.org{url}'
        self.urls = []

    def generate_6_degrees(self):
        '''generate url links'''
        self.urls = []

        if "/wiki/" not in self.url:
            raise ValueError("Please enter a valid wiki url")

        http = urllib3.PoolManager()
        counter = 0

        while counter <= 5:
            try:
                doc = http.request('GET', self.url)
            except urllib3.exceptions.HTTPError as ex:
                print("The URL could not be opened, " + str(ex))

            if doc.status > 299 or doc.status < 200:
                print("unable to retrieve the document at the URL provided: "
                      + self.url)
                return

            soup = BeautifulSoup(doc.data, 'html.parser')
            all_urls = []
            attrs = {'href': re.compile('^(/wiki/[a-zA-Z_.0-9()%-:]*)$')}
            for tag in soup.body.find_all('a', attrs):
                url = f"https://en.wikipedia.org{format(tag.get('href'))}"
                all_urls.append(url)

            self.url = all_urls[random.randint(0, len(all_urls)-1)]
            self.urls.append(self.url)
            counter += 1

    def get_summary_as_list(self):
        '''get summary info'''
        print(f'URLs discovered and explored: {self.urls}')

    def get_summary_as_json(self):
        '''get summary info'''
        print(f'URLs discovered and explored: {json.dumps(self.urls)}')

    def return_summary_as_string(self):
        '''get summary info'''
        return (f'URLs discovered and explored: {json.dumps(self.urls)}')

    def get_urls(self):
        '''get urls'''
        return self.urls
