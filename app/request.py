import urllib.request,json
from .models import Articles,Sources

# News = news.News

#Getting api api Key
api_key = None

#Getting the news base url
base_url = get_news=None


def configure_request(app):

    global api_key,base_url_source,base_url_articles
    api_key = '854b811928a24b52a41fb275bc9bb457'
    base_url_source='https://newsapi.org/v2/sources?apikey=0e0837dd5a584abf8479e5f3e49a2e3f'
    base_url_articles='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

def process_source_results(sources):
    news_sources = []
    for source in sources:
        id = source.get('id')
        name = source.get('name')
        description =source.get('description')
        url =source.get('url')
        category =source.get('category')
        sources = Sources(id,name,description,url,category)

        news_sources.append(sources)
    return news_sources

def get_articles(id):
    get_articles_details_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(get_articles_details_url)

    with urllib.request.urlopen('https://newsapi.org/v2/sources?cartegory/general?&apiKey=854b811928a24b52a41fb275bc9bb457') as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response["sources"]:
            articles_list=articles_details_response['sources']
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
            id = source.get('id')
            name = source.get(name)
            description = source.get(description)
            url = source.get(url)
            category = source.get(category)

            articles = Articles(id,name,description,url,category)
    return news_results

def get_category(category):
    get_category_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey=854b811928a24b52a41fb275bc9bb457'.format(category)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_cartegory_response['articles']
            get_category_results = process_source_results(get_category_list)

    return get_category_results

def get_sources():
    '''
    function that returns the json response from url
    :return:
    '''
    get_source_url = base_url_source.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results=process_results(source_results_list)

        # source_results=source_results[0:15]

    return source_results

    def process_results(sources_list):
    sources_results=[]
    for source_item in sources_list:
        id=source.get('id')
        name=source.get('name')
        description=source.get('description')
        url=source.get('url')
        category=source.get('category')

        if id:
            source_object = Sources(id,name,description,url,category)
            sources_results.append(source_object)
    # print(sources_results)

    return sources_results
