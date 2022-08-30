import requests
import json
import time
import random
from config import config

# TO DO: if someone makes a listing and then deletes it instantly, it will send the last listing because the last listing id is replaces by the new one that is removed (make list of last_listings and check if new one is not in there yet)

class TweedehandsScraper:
    def __init__(self, url):
        self.url = url
        self.last_listing = ''

    def get_source_from_url(self):
        source = str(requests.get(self.url).text)
        return source

    def get_listings_from_source(self, source):
        json_data = json.loads(source)
        listings = json_data['listings']
        #sort listings by itemid
        listings.sort(key=lambda x: x['itemId'], reverse=True)
        return listings

    def update(self):
        listings = self.get_listings_from_source(self.get_source_from_url())
        if listings[0]['itemId'] != self.last_listing:
            self.last_listing = listings[0]['itemId']
            self.notify(listings[0])
        
        random_time = random.randint(40,60)
        time.sleep(random_time)

    def notify(self, listing):
        if listing['priceInfo']['priceType'] == 'FAST_BID':
            price = 'Bieden'
        if listing['priceInfo']['priceType'] == 'NOTK':
            price = 'NOTK'
        if listing['priceInfo']['priceType'] == 'RESERVED':
            price = 'Gereserveerd'
        else:
            price = str(listing['priceInfo']['priceCents'] / 100) + ' euro'

        # TO DO: escape special characters
        message = "New listing: " + listing['title'] + ". " + price + ". https://2dehands.be/" + listing['itemId']
        response = requests.post(
            url='https://api.telegram.org/bot{0}/sendPhoto'.format(token),
            data={'chat_id': chat_id, 'photo': listing['pictures'][0]['extraExtraLargeUrl'], 'caption': message}
        ).json()
        print(response)

if __name__ == '__main__':
    token = config['token']
    chat_id = config['chat_id']
    url = config['url']

    scraper = TweedehandsScraper(url)
    scraper.last_listing = scraper.get_listings_from_source(scraper.get_source_from_url())[0]['itemId']
    while True:
        scraper.update()
