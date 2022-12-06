import requests

search_url = "https://search.wb.ru/exactmatch/ru/common/v4/search"

# query = {
#     'appType': 1,
#     'couponsGeo': '12,7,3,6,18,22,21',
#     'curr': 'rub',
#     'dest': '-1075831,-79374,-367666,-2133452',
#     'emp': 0,
#     'lang': 'ru',
#     'locale': 'ru',
#     'page': 1,
#     'pricemarginCoeff' : 1.0,
#     'query' : "adn12316",
#     'reg' : 0,
#     'regions' : "80,64,83,4,38,33,70,82,69,68,86,30,40,48,1,22,66,31",
#     'resultset' : 'catalog',
#     'sort' : 'popular',
#     'spp' : 0,
#     'suppressSpellcheck' : "false",
#     'xsubject': '6728;2013'
# }
query = {
    'resultset' : 'catalog',
    'query' : 'adn12316'
}
response = requests.get(search_url, params=query)

print(response.text)
