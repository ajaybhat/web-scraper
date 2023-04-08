import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def scrape_by_tag(self, tag, attrs=None):
        """
        Scrape data from the website based on the provided tag and optional attributes.

        Args:
            tag (str): HTML tag to search for and extract data.
            attrs (dict, optional): Dictionary of attributes and their values to filter the search (default: None).

        Returns:
            list: List of dictionaries containing the extracted data.
        """
        extracted_data = []
        for element in self.soup.find_all(tag, attrs=attrs):
            data = {}
            if 'text' in attrs:
                data['text'] = element.text.strip()
            if 'href' in attrs:
                data['href'] = element['href']
            if 'src' in attrs:
                data['src'] = element['src']
            extracted_data.append(data)
        return extracted_data

