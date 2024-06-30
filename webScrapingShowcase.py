'''
    Author: Constantine Lekkos
    Purpose: Showcase of a simple Web Scraping that scrapes 116 products with their prices and descriptions using bs4 and requests libraries.
    After that, data are saved in a csv file.
    Created Date: 30/06/2024
'''

# Libraries
from bs4 import BeautifulSoup as bs
import requests as rq
import csv

# Class and Methods that implement the functionality of the Web Scraping task
class WebScrapeClass():
    def __init__(self, site) -> None:
        self.site = site # Saves the url into the variable
        # headers with User-Agent helps to not get a block and acts like a web browser in requests
        # With the requests library a get request in the server takes place
        temp_site = rq.get(site, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0'})
        # Saved the content of web page as html in the variable
        self.bsoup = bs(temp_site.text, "html.parser")
    
    # Method to save in a list the elements with <a></a> tag and class specific attibute
    def products(self) -> list: # Returns a list
        products = self.bsoup.findAll("a", attrs = {"class": "title"})
        return products
    
    # Method to save in a list the elements with <h4></h4> tag and class specific attibute
    def prices(self) -> list: # Returns a list
        prices = self.bsoup.findAll("h4", attrs = {"class": "price float-end card-title pull-right"})
        return prices
    
    # Method to save in a list the elements with <p></p> tag and class specific attibute
    def descriptions(self) -> list: # Returns a list
        descriptions = self.bsoup.findAll("p", attrs = {"class": "description card-text"})
        return descriptions

# Main program is indicated with the below if statement
if __name__ == "__main__":
    site = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" # Actual site
    site_to_scrape = WebScrapeClass(site) # Object of relative Class

    products = site_to_scrape.products() # Call of Methods and assigned it in a variable
    prices = site_to_scrape.prices() # Call of Methods and assigned it in a variable
    descriptions = site_to_scrape.descriptions() # Call of Methods and assigned it in a variable

    file = open("scraped_data.csv", "w") # Opens a file to save the data a forge the data set
    writer = csv.writer(file) # Writes the data i na csv format
    writer.writerow(["Products", "Prices", "Descriptions"]) # Index of rows, Column names

    counter = 0 # Counter
    for product, price, description in zip(products, prices, descriptions): # Iterates in 3 lists
        print(f"Product {counter}") # Prints
        print(f"Name: {product.text}\nPrice: {price.text}\nDescription: {description.text}") # Prints
        writer.writerow([product.text, price.text, description.text]) # Writes the actual data into the csv
        print("***") # Prints
        counter += 1 # Counting...
    
    file.close() # Closes the file
