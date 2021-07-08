from pygooglenews import GoogleNews

gn = GoogleNews(lang ='es',country = 'PR')

def get_news_data(search):
    news_data = []   
    search = gn.search(search, from_ = '2020-03-08')
    for item in search['entries']:
        news_metadata = {
        'title': item.title,
        'date': item.published_parsed
        }
        news_data.append(news_metadata)
    return news_data

print(get_news_data('covid'))

