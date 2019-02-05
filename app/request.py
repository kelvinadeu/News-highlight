import urllib.request,json
from .models import Articles

# News = news.News

#Getting api api Key
api_key = None

#Getting the news base url
base_url = get_news=None

def configure_request(app):
    global api_key,base_url_source,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url_source= 'https://newsapi.org/v2/sources?apikey=0e0837dd5a584abf8479e5f3e49a2e3f'
def configure_request(app):
    global api_key,base_url_source,base_url_articles
    api_key = app.config['NEWS_API_KEY']
    base_url_source='https://newsapi.org/v2/sources?apikey=0e0837dd5a584abf8479e5f3e49a2e3f'
    base_url_articles=app.config['ARTICLES_BASE_URL']
    base_url_articles=app.config['ARTICLES_BASE_URL']

def get_articles(id):
    get_articles_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(get_articles_details_url)

    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response["articles"]:
            articles_list=articles_details_response['articles']
            articles_object= process_source_results(articles_list)

    return articles_object
    news_results = process_results(news_results_list)

    def process_results(news_list):
        """
        Function that processes the sourc list of articles that contain news details

        Args:
            news_list:A list of articles that contain news details

        Returns :
               news_results:A list of article objects

        """
        news_results = []
        for news in news_list:
            id = news.get('id')
            name = news.get(name)
            description = news.get(description)
            url = news.get(url)
            category = news.get(category)

    return news_results
