#전체코드

import requests
from bs4 import BeautifulSoup
import urllib.request

URL = 'https://www.coupang.com/vp/products/5647481827?itemId=9231892317&vendorItemId=76517595808&sourceType=CAMPAIGN&campaignId=82&categoryId=0&isAddedCart='

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
res = requests.get(URL, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml") 

product_img_url = "http:"+ soup.select_one('#repImageContainer > img')['src']

urllib.request.urlretrieve(product_img_url, "이미지.jpg")