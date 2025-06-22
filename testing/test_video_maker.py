import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import scrape_product_data
from video_maker import create_ad_video
from generator import generate_ad_script
import uuid


# Use any valid Amazon product URL for testing
test_url = "https://www.amazon.in/Sony-Soundbar-Wireless-Dimensional-Surround/dp/B0D1C2GS99"

product_data = scrape_product_data(test_url)

if "image" in product_data:
    product_data["images"] = [product_data["image"]]

script, benefits = generate_ad_script(product_data)
filename = f"video_{uuid.uuid4()}.mp4"
video_path = create_ad_video(product_data, script, benefits, filename)

print("Video generated at:", video_path)