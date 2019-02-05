class Config:
    '''
    General configuration parent class
    '''

    API_BASE_URL = 'https://newsapi.org/v2/sources?cartegory/{}?&apiKey={}'

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
