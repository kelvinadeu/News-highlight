from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api api Key
Api_key = app.config['SOURCES_API_KEY']

#Getting the news base url
base_url = app.config["SOURCES_API_KEY_API_BASE_URL"]

def get_news(category):
    """
    Function that gets the json reponse to our url request
    """
    get__news__url = base_url.format(category,Api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = none

        if get_news_response['result']:
            news_results_list = get_news_response['results']
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
        for news_articles in news_list:
            id = news_articles.get('id')
            overview = news_articles.get(overview)

    return news_results
