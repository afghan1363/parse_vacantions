import json

import requests


def hello():
    keyword = input("Введите ключевое слово названия вакансии ")
    salary = input("Введите желаемую вилку зарплаты ")
    region = input("Введите регион поиска вакансий(по умолчанию вся Россия) ")

def getAreas():
    req = requests.get('https://api.hh.ru/areas')
    data = req.content.decode()
    req.close()
    jsObj = json.loads(data)
    areas = []
    for k in jsObj:
        for i in range(len(k['areas'])):
            if len(k['areas'][i]['areas']) != 0:                      # Если у зоны есть внутренние зоны
                for j in range(len(k['areas'][i]['areas'])):
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['areas'][j]['id'],
                                  k['areas'][i]['areas'][j]['name']])
            else:                                                                # Если у зоны нет внутренних зон
                areas.append([k['id'],
                              k['name'],
                              k['areas'][i]['id'],
                              k['areas'][i]['name']])
    return areas

areas = getAreas()
city = input("Enter city ")
index = 0
for cities in areas:
    if city in cities:
        index = cities[cities.index(city) - 1]
print(index)
