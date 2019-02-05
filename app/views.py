from flask import render_template
from . import main
from .request import get_news



@main.route('/')
def index():
    '''
    my index page
    :return:
    '''
    sources=  get_sources()
    print(sources)
    return render_template('index.html', sources = sources)


# Views
@app.route('/index')
def index():

    '''
    View source page function that returns the source details
    '''

    #Getting latest news highlights
    latest_news = get_news('general')
    print(latest_news)
    title = 'Home - welcome to the best news highlight website Online'
    return render_template('index.html',title=title,id = source_id, general=latest_news)
