from abc import ABC, abstractmethod

class BaseScraper(ABC):

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers or  {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    @abstractmethod
    def fetch(self):
        """Fetch raw HTML or data."""
        pass

    @abstractmethod
    def parse(self, html):
        """Parse the raw HTML and return structured job data."""
        pass