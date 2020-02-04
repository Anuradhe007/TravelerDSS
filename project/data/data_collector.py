import requests
from bs4 import BeautifulSoup


class DataCollector:

    def get_hotel_reviews(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        reviews = soup.find_all('div', class_='review_item_review_content')
        for review in reviews:
            print(review.get_text())


if __name__ == "__main__":
    dc = DataCollector()
    # api-endpoint
    URL = 'https://www.booking.com/hotel/lk/gamagedara-resort.html?label=gen173nr-1DCAEoggI46AdIM1gEaIUBiAEBmAEKuAEXyAEM2AED6AEBiAIBqAIDuAKByuTxBcACAQ;sid=e1eabdfeb703aafbdeaa1cee87ff5ee1;all_sr_blocks=103046408_184396335_2_1_0;checkin=2020-02-08;checkout=2020-03-08;dest_id=-2215119;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=103046408_184396335_2_1_0;hpos=1;no_rooms=1;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=103046408_184396335_2_1_0__57220;srepoch=1580803368;srpvid=88f2389355540157;type=total;ucfs=1&#tab-reviews'
    dc.get_hotel_reviews(URL)
