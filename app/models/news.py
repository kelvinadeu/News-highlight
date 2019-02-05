class News:
    """
    News class to define News Objects
    """
    def __init__(self,id,source,country,language,cartegory,headlines):
        self.id = id 
        self.headlines = headlines
        self.source = source
        self.country = country
        self.language = language
        self.cartegory = cartegory
