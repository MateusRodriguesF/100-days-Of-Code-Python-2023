import requests
import lxml
from bs4 import BeautifulSoup
class BsoupZillow():
    def bsoup_get_link_list(self):
        self.url ='https://www.zillow.com/homes/for_rent/?searchQueryState={"pagination":{},"mapBounds":{"west":-122.83501662207031,"east":-122.03164137792969,"south":37.552434287743424,"north":37.99747886057563},"mapZoom":11,"isMapVisible":false,"filterState":{"price":{"max":872627},"beds":{"min":1},"fore":{"value":false},"mp":{"max":3000},"auc":{"value":false},"nc":{"value":false},"fr":{"value":true},"fsbo":{"value":false},"cmsn":{"value":false},"fsba":{"value":false}},"isListVisible":true}'
        self.header = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/601.5 (KHTML, like Gecko) Chrome/55.0.1412.243 Safari/537.6 Edge/16.26865",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }
        self.response = requests.get(self.url, headers=self.header)
        self.response.raise_for_status()
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.apt_tags = self.soup.find_all(class_="property-card-link")
        print(self.apt_tags)

        

