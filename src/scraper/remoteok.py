import requests
from bs4 import BeautifulSoup
from basescraper import BaseScraper


class RemoteOkScraper(BaseScraper):

    def fetch(self):
        response = requests.get(self.base_url, self.headers)
        response.raise_for_status()
        return response.text
    
    def parse(self, html):
        soup = BeautifulSoup(html, "lxml")