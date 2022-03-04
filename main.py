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