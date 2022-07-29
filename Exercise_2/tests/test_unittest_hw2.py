from yadi_directory import create_folder, headers
from parameterized import parameterized
import unittest
import time
import requests
import json


class test_create_dir(unittest.TestCase):

    FIXTURE_NEW_DIR_NAMES = [
        'jersey', 'oxford', 'trinidad', 'amsterdam', 'toronto'
        ]
    FIXTURE_NAME_STATUSCODE = [
        ('nitro', 201), ('testik', 201),
        ('nitro', 409), ('bagapsh', 201),
        ('testik', 409), ('jack', 201)
        ]

    @parameterized.expand(FIXTURE_NAME_STATUSCODE)
    def test_create_folder(self, name, result):
        time.sleep(0.5)
        status = create_folder(name).status_code
        print(name, status, result)
        self.assertEqual(status, result)

    @parameterized.expand(FIXTURE_NEW_DIR_NAMES)
    def test_new_name_and_number_of_dirs(self, new_dir_name):
        number_before = 0
        number_after = 0
        names_before = ''
        get_info_catalogs_before = (requests.get(
            f'https://cloud-api.yandex.net/v1/disk/resources?path=/',
            headers=headers)).json()
        for position in get_info_catalogs_before['_embedded']['items']:
            if position['type'] == 'dir':
                number_before += 1
                names_before += " " + position['name']
        path_folder = create_folder(new_dir_name)
        href = path_folder.json()['href']
        get_name_catalog_after = ((requests.get(href, headers=headers)).json())['name']
        regex = f"{(get_name_catalog_after)}"
        self.assertNotRegex(names_before, regex, msg=None)
        get_info_catalogs_after = (requests.get(
            f'https://cloud-api.yandex.net/v1/disk/resources?path=/',
            headers=headers)).json()
        for position in get_info_catalogs_after['_embedded']['items']:
            if position['type'] == 'dir':
                number_after += 1
        self.assertEqual(number_before+1, number_after)
