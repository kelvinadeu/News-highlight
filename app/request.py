from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api api Key
Api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_news(category):
    """
    Function that gets the json reponse to our url request
    """
    get__news__url = base_url.format(category,Api_key)
