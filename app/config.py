class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
    API_KEY = 'https://newsapi.org/v2/top-headlines?country/{}?apiKey={}'
    SOURCES_API_KEY = 'https://newsapi.org/v2/sources?country/{}?apiKey={}'
    SOURCES_API_KEY_API_BASE_URL = 'https://newsapi.org/v2/sources?country/{}?apiKey={}'
    error = 'https://newsapi.org/v2/everything/{}?apiKey={}'
    API_KEY = 'https://newsapi.org/v2/cartegory/{}?apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
