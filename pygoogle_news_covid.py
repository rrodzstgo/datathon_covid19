from pygooglenews import GoogleNews

gn = GoogleNews(lang ='es',country = 'MX')

covid_gn = gn.search('COVID-19')

print(covid_gn)