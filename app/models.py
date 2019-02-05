class Articles:
    def __init__(self,id,name,description,url,category):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        

class Sources:
    def __init__(self,id,name,description,url,category):
        id = news.get('id')
        name = news.get(name)
        description = news.get(description)
        url = news.get(url)
        category = news.get(category)
