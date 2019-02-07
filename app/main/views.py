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
    return render_template('index.html',general=new_sources)

@main.route('/business')
def business():

    '''
    my index page
    :return:
    '''
    new_articles=  get_sources('business')
    return render_template('business.html',source = new_articles)


@main.route('/health')
def health():

    '''
    my index page
    :return:
    '''
    new_articles=  get_sources('health')
    return render_template('health.html',source = new_articles)


@main.route('/politics')
def politics():

    '''
    my index page
    :return:
    '''
    new_articles=  get_sources('entertainment')
    return render_template('politics.html',source = new_articles)

@main.route('/sports')
def sports():

    '''
    my index page
    :return:
    '''
    new_articles=  get_sources('sports')
    return render_template('sports.html',source = new_articles)

@main.route('/technology')
def technology():

    '''
    my index page
    :return:
    '''
    new_articles=  get_sources('technology')
    return render_template('technology.html',source = new_articles)











# ViewsBy=relevancy&apiKey={}'.format(category, api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)

        get_category_results = None

        if get_category_response['articles']:
            get_category_list = get_cartegory_response['articles']
            get_category_results = process_source_results(get_category_list)

    return get_category_results
