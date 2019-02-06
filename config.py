import os
class Config:

    '''
    General configuration parent class

    '''
    # pass
    SOURCE_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'

    NEWS_API_SOURCE_URL='https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_BASE_URL='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    # CATEGORIES_URL='https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY=os.environ.get('SECRET_KEY')

    DEBUG = True

class ProdConfig(Config):

    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''



class DevConfig(Config):

    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''




config_options = {
'development':DevConfig,
'production':ProdConfig
}
