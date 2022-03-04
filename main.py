import json

import requests as requests


def kc_data_url(path):
    return 'http://kcwikizh.github.io/kcdata/{}/all.json'.format(path)


def get_json(url):
    return requests.get(url).json()


# "type": "extra" if i["id"] % 10 >= 5 and i["id"] // 10 <= 7 else "normal" if i["id"] // 10 <= 7 else "event"

if __name__ == '__main__':
    map_list = [{
        "area": i["id"] // 10,
        "id": i["id"] % 10,
        "name": i["name"],
        "type": "event" if i["id"] // 10 > 7 else "extra" if i["id"] % 10 >= 5 else "normal"
    } for i in get_json(kc_data_url('map'))]
    with open('json/map.json', 'w+', encoding='utf8') as f:
        f.write(json.dumps(map_list, ensure_ascii=False, indent=1))
    area_list = [
        {
            "id": i["id"],
            "name": i["name"],
            "event":i["event"]
        }
        for i in get_json(kc_data_url('maparea'))
    ]
    with open('json/area.json', 'w+', encoding='utf8') as f:
        f.write(json.dumps(area_list, ensure_ascii=False, indent=1))
