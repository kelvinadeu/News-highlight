class Sources:
    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category


class Articles:
    def __init__(self,id,name,description,url,category):
        self.id = news.get('id')
        self.name = news.get(name)
        self.description = news.get(description)
        self.url = news.get(url)
        self.category = news.get(category)
