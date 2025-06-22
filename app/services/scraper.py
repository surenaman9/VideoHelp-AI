import requests
from bs4 import BeautifulSoup

def scrape_product_data(url: str):
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch product page: {response.status_code}")

        soup = BeautifulSoup(response.content, 'html.parser')

        title = soup.find('span', {'id': 'productTitle'})
        price = soup.find('span', {'class': 'a-price-whole'})
        image = soup.find('img', {'id': 'landingImage'})
        bullets = soup.find('div', {'id': 'feature-bullets'})

        description = ' '.join(
            bp.get_text().strip()
            for bp in bullets.find_all('span', class_='a-list-item') if bp.get_text().strip()
        ) if bullets else "No description available"

        return {
            "title": title.get_text().strip() if title else "No title found",
            "price": price.get_text().strip() if price else "Price not listed",
            "image": image['src'] if image and 'src' in image.attrs else None,
            "description": description
        }

    except Exception as e:
        raise RuntimeError(f"Scraping error: {str(e)}")