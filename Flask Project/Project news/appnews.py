from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = '2cdffea5867142739eb61619303e7b78'  # Replace with your actual News API key

def fetch_news():
    try:
        news_url=f'https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}'
        response = requests.get(news_url)

        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        news_data = response.json()
        articles = news_data.get('articles', [])

        return [article for article in articles if 'title' in article]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None

@app.route('/')
def index():
    # Fetch real-time news data from News API
    news = fetch_news()

    if news is None:
        # Use sample news if there is an issue with the API request
        news = [{"title": "News 1"}, {"title": "News 2"}, {"title": "News 3"}]

    return render_template('index.html', articles=news)

if __name__ == '__main__':
    app.run(debug=True)
