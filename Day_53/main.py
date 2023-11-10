import requests
import lxml
from bs4 import BeautifulSoup

header = {
"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/601.5 (KHTML, like Gecko) Chrome/55.0.1412.243 Safari/537.6 Edge/16.26865",
"Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get('https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState={"pagination":{},"usersSearchTerm":"San Francisco, CA","mapBounds":{"west":-122.55177535009766,"east":-122.31488264990234,"south":37.69926912019228,"north":37.851235694487485},"regionSelection":[{"regionId":20330,"regionType":6}],"isMapVisible":true,"filterState":{"fr":{"value":true},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"fore":{"value":false},"pmf":{"value":false},"pf":{"value":false},"mp":{"max":3000},"price":{"max":872627},"beds":{"min":1}},"isListVisible":true,"mapZoom":12}', headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")
apt_links = soup.select(".list-card-top a")

all_links = []

for link in all_links:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links)


        

