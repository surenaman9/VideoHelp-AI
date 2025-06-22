import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scraper import scrape_product_data

url = "https://www.amazon.in/dp/B0D1C2GS99"  # Use a clean product URL
data = scrape_product_data(url)
print("\n🔍 Scraped Product Data:")
print(data)