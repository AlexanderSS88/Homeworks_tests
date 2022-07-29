import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = 'AQAAAAA5Ju1YAADLW-ELZgMfgEo6l_OWPBRKflo'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {TOKEN}'}


def create_folder(name):
    path_folder = requests.put(f'{URL}?path={name}', headers=headers)
    return path_folder






