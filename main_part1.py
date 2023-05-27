from bs4 import BeautifulSoup
import requests
import time


def find_products():
    x = 1
    html_text = requests.get(
        'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1').text

    soup = BeautifulSoup(html_text, "html.parser")
    products = soup.find_all('div', class_='a-section a-spacing-none puis-padding-right-small s-title-instructions-style')

    # Products URL
    for product in products:
        urls = product.find_all('a')
        product_name = product.find('span', class_='a-size-medium a-color-base a-text-normal').text.replace(' ', '')
        product_price = product.find('span', class_='a-price a-text-price')
        if product_price:
            product_price = product_price.text.strip()
        product_rating = product.find('span', class_='a-size-medium a-color-base a-text-beside-button a-text-bold')
        total_ratings  = product.find('span', class_='a-size-base a-color-secondary totalRatingCount')
        print(x)
        for url in urls:
            print("https://www.amazon.in/" + url.get('href'))
        print('Product_name : ',product_name, )
        print('Product_price : ',product_price, ' (Dyanmic scraping cannot be possible with BeautifulSoup)')
        print('Product rating : ',product_rating, ' (Dyanmic scraping cannot be possible with BeautifulSoup)')
        print('Total ratings : ', total_ratings, ' (Dyanmic scraping cannot be possible with BeautifulSoup)')
        print(' ')

        x = x+1
        if x > 20:
            break



if __name__ == '__main__':
    while True:
        find_products()

