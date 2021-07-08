from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

googlenews = GoogleNews(start='07/03/2020', end='07/07/2021')
googlenews.search('covid')
result = googlenews.result()
df = pd.DataFrame(result)
print(result)

#for i in range(2,20):
 #   googlenews.getpage(i)
  #$  result = googlenews.result()
    #df = df.append(result)
    #df = pd.DataFrame(df)