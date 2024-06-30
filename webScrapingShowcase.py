'''
    Author: Constantine Lekkos
    Purpose: Showcase of a simple Web Scraping that scrapes 116 products with their price and description using bs4 and requests libraries
    Created Date: 30/06/2024
'''

# Libraries
from bs4 import BeautifulSoup as bs
import requests as rq
import csv

# Class and Methods that implement the functionality of the Web Scraping task
class WebScrapeClass():
    def __init__(self, site) -> None:
        self.site = site
        # headers with User-Agent helps to not get a block and acts like a web browser in requests
        temp_site = rq.get(site, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})
        self.bsoup = bs(temp_site.text, "html.parser")
    
    def products(self) -> list:
        products = self.bsoup.findAll("a", attrs = {"class": "title"})
        return products
    
    def prices(self) -> list:
        prices = self.bsoup.findAll("h4", attrs = {"class": "price float-end card-title pull-right"})
        return prices
    
    def descriptions(self) -> list:
        descriptions = self.bsoup.findAll("p", attrs = {"class": "description card-text"})
        return descriptions


if __name__ == "__main__":
    site = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    site_to_scrape = WebScrapeClass(site)

    products = site_to_scrape.products()
    prices = site_to_scrape.prices()
    descriptions = site_to_scrape.descriptions()

    file = open("scraped_data.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Products", "Prices", "Descriptions"])

    counter = 0
    for product, price, description in zip(products, prices, descriptions):
        print(f"Product {counter}")
        print(f"Name: {product.text}\nPrice: {price.text}\nDescription: {description.text}")
        writer.writerow([product.text, price.text, description.text])
        print("***")
        counter += 1
    
    file.close()
