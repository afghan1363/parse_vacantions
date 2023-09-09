import requests
import json

API_SJ = "v3.h.4525045.ed10e2c364a8b30ec575f46690cd3eb9519ed323.3032a7eabfb8d5c94df31d600f62a208445dfd98"

url_hh = "https://api.hh.ru/vacancies"
url_sj = "https://api.superjob.ru/2.0/vacancies"

headers_sj = {
    "X-Api-App-Id": "v3.h.4525045.ed10e2c364a8b30ec575f46690cd3eb9519ed323.3032a7eabfb8d5c94df31d600f62a208445dfd98"
}

params_hh = {
    "text": "врач",
    'id': None,  # ID вакансии
    'name': None,  # назввние должности
    'salary': 100000,  # зарплата from и to
    'type': None, #id open name Открытая
    'employer_name': None, #ID работодателя Яндекс
    'experience': None,  #нет опыта
    'employment': None,  #занятость полная_неполная
    'responsibility': None, #описание
    'requirement' : None, #требования
    "per_page": 50
}
params_sj = {
    "keyword": "Python разработчик"
}

r = requests.get(url_hh, params=params_hh)
data = r.content.decode()
# vacant = json.loads(data)
# for vacan in vacant:
#     print(vacant['items'][0]['name'])
#     print(vacant['items'][0]['employer']['name'])
#     print(vacant['items'][0]['snippet']['requirement'])
#     print(vacant['items'][0]['salary']['from'])
#     print(vacant['items'][0]['snippet']['responsibility'])
#     print(vacant)
print(data)

