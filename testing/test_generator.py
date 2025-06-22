import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from generator import generate_ad_script

# Sample product data
product_data = {
    "title": "Sony Bravia Theatre Quad (HT-A9M2) Premium Soundbar",
    "price": "1,99,990.",
    "image": "https://m.media-amazon.com/images/I/31nojZI6L6L._SX300_SY300_QL70_ML2_.jpg",
    "description": "360 Spatial Sound Mapping, Dolby Atmos, Hi-Res Audio, IMAX Enhanced, Bluetooth, Wi-Fi",
    "features": [
        "360 Spatial Sound Mapping",
        "Dolby Atmos",
        "IMAX Enhanced",
        "Bluetooth Connectivity"
    ]
}

script, benefits = generate_ad_script(product_data)

print("📝 Generated Script:")
print(script)
print("\n✨ Key Benefits:")
for benefit in benefits:
    print("-", benefit)