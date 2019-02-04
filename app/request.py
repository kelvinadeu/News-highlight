from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api api Key
Api_key = app.config['NEWS_API_KEY']
