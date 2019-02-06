from flask import render_template
from . import main
from ..request import get_sources
from ..models import Sources



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    new_sources=  get_sources('general')
    return render_template('index.html',general = new_sources)

# @main.route('/index')
# def index():
#
#     '''
#     View source page function that returns the source details
#     '''
#
#     #Getting latest news highlights
#     latest_news = get_news('general')
#     print(latest_news)
#     title = 'Home - welcome to the best news highlight website Online'
#     return render_template('index.html',title=title,id = source_id, general=latest_news)
#     # @app.route('/article/')
@main.route('/articles/<id>')
def articles(id):

    '''
    View  page function that returns the details page and its data
    '''
    name="Adeu"
    articles=get_articles(id)
    # print(articles)
    # title=f'{articles.title}'
    return render_template('articles.html', articles=articles, name=name,name_source=id)

# @main.route('/categories/<category_name>')
# def categories(category_name):
#
#     '''
#     View  page function that returns the details page and its data
#     '''
#     category="Phoebe"
#     category=get_category(category_name)


# ViewsBy=relevancy&apiKey={}'.format(category, api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_cartegory_response['articles']
            get_category_results = process_source_results(get_category_list)

    return get_category_results
