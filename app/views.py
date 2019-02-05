from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/news/<int:source_id>')
def news(source_id):

    '''
    View source page function that returns the source details
    '''

    #Getting latest news highlights
    latest_news = get_news('latest')
    print(latest_news)
    title = 'Home - welcom to the best news highlight website Online'
    return render_template('news.html',title.title,id = source_id)
