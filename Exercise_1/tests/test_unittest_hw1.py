import unittest
from parameterized import parameterized
from unittest.mock import patch
from Old_homework import documents as docs, directories as dirs, people, shelf, list_of_persons, delete, add_shelf, move, add


class test_hw1(unittest.TestCase):


    """Первая функция"""
    @patch('builtins.input', lambda *args: '10006')
    def test_people1(self):
        self.assertEqual(people(docs, dirs), "Аристарх Павлов")

    @patch('builtins.input', lambda *args: '5455 028765')
    def test_people2(self):
        self.assertEqual(people(docs, dirs), 'Документ с таким номером '
                                             'хранится на полках, однако'
                                             ' данные о человеке в '
                                             'базе отсутствуют.')

    @patch('builtins.input', lambda *args: "11-2")
    def test_people3(self):
        self.assertEqual(people(docs, dirs), 'Геннадий Покемонов' )

    @patch('builtins.input', lambda *args: '2207')
    def test_people4(self):
        self.assertEqual(people(docs, dirs), 'Документ с таким '
                                             'номером отсутствует в базе!')


    """Вторая функция"""
    @patch('builtins.input', lambda *args: "11-2")
    def test_shelf1(self):
        self.assertEqual(shelf(dirs), '1')

    @patch('builtins.input', lambda *args: "11")
    def test_shelf2(self):
        self.assertEqual(shelf(dirs),
            'Документ с таким номером отсутствует в базе!')


    """Третья функция"""
    def test_list_of_persons(self):
        ANSWER_OF_DEF = "passport 2207 876234 Василий Гупкин\n" \
                        "invoice 11-2 Геннадий Покемонов\n" \
                        "insurance 10006 Аристарх Павлов\n"
        self.assertEqual(list_of_persons(docs), ANSWER_OF_DEF)


    """Четвёртая функция"""
    @patch('builtins.input', side_effect=["3", "certificate", "777", "Boby Thornton"])
    def test_add1(self, mock_input):
        number_of_docs_before = len(docs)
        number_of_dirs_before = len(dirs["3"])
        expected_response = [number_of_docs_before + 1, number_of_dirs_before + 1]
        self.assertEqual(add(docs, dirs), expected_response)

    @patch('builtins.input', side_effect=["4", "passport", "999", "Nil Armstrong"])
    def test_add2(self, mock_input):
        expected_response = 'Такой полки не существует!'
        self.assertEqual(add(docs, dirs), expected_response)


    """Пятая функция"""
    @patch('builtins.input', lambda *args: "2207 876234")
    def test_delete1(self):
        number_of_docs_before = len(docs)
        number_of_dirs_before = 0
        number_of_dirs_before = sum(
            [number_of_dirs_before + len(list_docs) for id,
            list_docs in dirs.items()
            ]
            )
        expected_response = [number_of_docs_before - 1, number_of_dirs_before - 1]
        self.assertEqual(delete(docs, dirs), expected_response)
        return

    @patch('builtins.input', lambda *args: "2207")
    def test_delete2(self):
        self.assertEqual(delete(docs, dirs), 'Документ с таким номером отсутствует в базе!')


    """Шестая функция"""
    @patch('builtins.input', side_effect=["10006", "3"])
    def test_move1(self, mock_input):
        length_before = len(dirs['3'])
        self.assertEqual(move(dirs), length_before+1)

    @patch('builtins.input', side_effect=["11-2", "4"])
    def test_move2(self, mock_input):
        self.assertEqual(move(dirs), 'Такой полки не существует!')

    @patch('builtins.input', side_effect=["11", "3"])
    def test_move3(self, mock_input):
        self.assertEqual(move(dirs), 'Документ с таким номером отсутствует в базе!')


    """Седьмая функция"""
    @patch('builtins.input', lambda *args: "3")
    def test_add_shelf1(self):
        self.assertEqual(add_shelf(dirs), 'Такая полка уже существует!')

    @patch('builtins.input', lambda *args: "4")
    def test_add_shelf2(self):
        number_of_dirs_before = len(dirs)
        self.assertEqual(add_shelf(dirs), number_of_dirs_before + 1)

