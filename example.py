from scraper import WebScraper
from utils import sanitize_text

# Define the URL to scrape
url = 'https://example.com/news'  # Replace with the URL of the website you want to scrape

# Initialize the web scraper
web_scraper = WebScraper(url)

# Extract news article titles and URLs using 'h2' tag
news_articles = web_scraper.scrape_by_tag('h2', attrs={'text': True, 'href': True})

# Extract social media posts using 'div' tag and 'post' class
social_media_posts = web_scraper.scrape_by_tag('div', attrs={'class': 'post'})

# Extract product information using 'div' tag and 'product' class
product_information = web_scraper.scrape_by_tag('div', attrs={'class': 'product'})

# Sanitize extracted text data
for article in news_articles:
    article['text'] = sanitize_text(article['text'])

for post in social_media_posts:
    post['text'] = sanitize_text(post['text'])

# Print the extracted and sanitized data
print('News articles:')
for article in news_articles:
    print(article)

print('Social media posts:')
for post in social_media_posts:
    print(post)

print('Product information:')
for product in product_information:
    print(product)
