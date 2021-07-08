from pygooglenews import GoogleNews
import pandas as pd
import pickle

gn = GoogleNews(lang ='es',country = 'mx')

def get_news_data(search):
    news_data = []   
    search = gn.search(search)
    for item in search['entries']:
        news_metadata = {
        'title': item.title,
        'date': item.published_parsed
        }
        news_data.append(news_metadata)
    return news_data
covid19_news_list = get_news_data('covid19')

covid19_news_list_df = pd.DataFrame(covid19_news_list)

covid19_news_list_df.to_csv(path_or_buf='covid_news_list_df_mx.txt',index =False, sep='\t')

