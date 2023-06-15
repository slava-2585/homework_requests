import requests


def intelligence_heroes(spisok_heroes=['Hulk', 'Captain America', 'Thanos']):
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    all_heroes = response.json()
    list_intelligence = []
    for heroes in all_heroes:
        if heroes['name'] in spisok_heroes:
            rezult = []
            rezult.append(heroes['powerstats']['intelligence'])
            rezult.append(heroes['name'])
            list_intelligence.append(rezult)
    list_intelligence.sort(reverse=True)
    return (f'Самый интелектуальный герой {list_intelligence[0][1]} с интелектом {list_intelligence[0][0]}')

if __name__ == "__main__":
    print(intelligence_heroes())