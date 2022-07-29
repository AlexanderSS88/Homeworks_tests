import unittest
from parameterized import parameterized
from unittest.mock import patch
from ..Old_homework import documents as docs, directories as dirs, \
    people, shelf, list_of_persons, add, delete, move, add_shelf, user_control


class test_hw1(unittest.TestCase):

    @patch('builtins.input.return_value', "2207 876234")
    def test_people(self):
        # number = input('Введите номер документа: ')
        self.assertEqual(people(docs, dirs), "Василий Гупкин")

    def test_shelf(self):
        shelf(dirs)
        # number = input('Введите номер документа: ')

    def test_list_of_persons(self):
       list_of_persons(docs)

    def test_add(self):
        add(docs, dirs)
        # new_type = input('Введите тип документа: ')
        # new_number = input('Ведите номер документа : ')
        # new_name = input('Введите имя и фамилию: ')
        # shelf = input('Введите номер полки, куда положить документ: ')

    def test_delete(self):
        delete(docs, dirs)
        # number = input('Введите номер документа для удаления: ')

    def test_move(self):
        move(dirs)
        # number = input('Введите номер документа: ')
        # desired_shelf = input('Введите номер полки для перемещения: ')

    def test_add_shelf(self):
        add_shelf(dirs)
        # desired_shelf = input('Введите номер полки для создания: ')

    def test_user_control(self):
        user_control(docs, dirs)
