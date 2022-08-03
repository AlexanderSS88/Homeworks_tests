documents = [
	{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
directories = {
	'1': ['2207 876234', '11-2', '5455 028765'],
	'2': ['10006'],
    '3': []
    }


def people(docs, dirs):
	result = 'Документ с таким номером отсутствует в базе!'
	number = str(input('Введите номер документа: '))
	for shl, numbers in dirs.items():
		for num in numbers:
			if number == num:
				for person in docs:
					if number == person['number']:
						result = person['name']
						return result
					else:
						result = 'Документ с таким номером хранится ' \
								 'на полках, однако данные о человеке ' \
								 'в базе отсутствуют.'
	return result


def shelf(dirs):
	result = 0
	needed_shelf_number = ''
	while result == 0:
		number = input('Введите номер документа: ')
		for shl, numbers in dirs.items():
			for num in numbers:
				if number == num:
					needed_shelf = f'Документ находится на полке № {shl}'
					needed_shelf_number = shl
					result += 1
		if result == 0:
			needed_shelf_number = 'Документ с таким номером отсутствует в базе!'
			return needed_shelf_number
	return needed_shelf_number


def list_of_persons(docs):
	string_for_test = ""
	for id, person in enumerate(docs):
		string_for_test += person['type'] + " " + \
						   person['number'] + " " + \
						   person['name'] + "\n"
	return string_for_test


def add(docs, dirs):
	docs_after_add = docs.copy()
	dirs_after_add = {'1': dirs['1'].copy(), '2': dirs['2'].copy(), '3': dirs['3'].copy()}
	result = None
	while result is None:
		shelf = input('Введите номер полки, куда положить документ: ')
		for position in dirs_after_add:
			if shelf == position:
				new_type = input('Введите тип документа: ')
				new_number = input('Ведите номер документа : ')
				new_name = input('Введите имя и фамилию: ')
				new_person = {"type": new_type, "number": new_number, "name": new_name}
				docs_after_add.append(new_person)
				dirs_after_add[position].append(new_number)
				result = f'\n {docs_after_add} \n \n {dirs_after_add}'
				number_of_docs = len(docs_after_add)
				number_of_dirs = len(dirs_after_add[shelf])
				return [number_of_docs, number_of_dirs]
		if result == None:
			return 'Такой полки не существует!'
		return result


def delete(docs, dirs):
	docs_after_del = docs.copy()
	dirs_after_del = {'1': dirs['1'].copy(), '2': dirs['2'].copy(), '3': dirs['3'].copy()}
	result = 0
	number = input('Введите номер документа для удаления: ')
	for shl, numbers in dirs_after_del.items():
		for num in numbers:
			if number == num:
				numbers.remove(num)
				result += 1
				for person in docs_after_del:
					if number == person['number']:
						docs_after_del.remove(person)
						result += 1
						number_of_docs = len(docs_after_del)
						number_of_dirs = 0
						number_of_dirs = sum(
							[number_of_dirs + len(list_docs) for id,
							list_docs in dirs_after_del.items()
							]
							)
	if result == 0:
		result_del = f'\n {docs_after_del} \n \n {dirs_after_del}'
		return 'Документ с таким номером отсутствует в базе!'
	else:
		return [number_of_docs, number_of_dirs]


def move(dirs):
	dirs_after_move = {'1': dirs['1'].copy(), '2': dirs['2'].copy(), '3': dirs['3'].copy()}
	result = 0
	result2 = 0
	while result == 0:
		number_doc = input('Введите номер документа: ')
		for shl, numbers in dirs_after_move.items():
			for num in numbers:
				if number_doc == num:
					shelf = shl
					numbers.remove(num)
					result += 1
		if result == 0:
			return 'Документ с таким номером отсутствует в базе!'
	while result2 == 0:
		desired_shelf = input('Введите номер полки для перемещения: ')
		if desired_shelf in dirs_after_move:
			dirs_after_move[desired_shelf].append(number_doc)
			result2 += 1
			str(desired_shelf)
			length = len(dirs_after_move[desired_shelf])
		elif desired_shelf == shelf:
			return 'Документ уже находится здесь'
		else:
			return 'Такой полки не существует!'
	return length


def add_shelf(dirs):
	dirs_after_adds = {'1': dirs['1'].copy(), '2': dirs['2'].copy(), '3': dirs['3'].copy()}
	result = 0
	while result == 0:
		desired_shelf = input('Введите номер полки для создания: ')
		for shelf in dirs_after_adds:
			if desired_shelf == shelf:
				return 'Такая полка уже существует!'
		if desired_shelf != shelf:
			dirs_after_adds[desired_shelf] = []
			result += 1
	number_of_dirs = len(dirs_after_adds)
	return number_of_dirs


def user_control(docs, dirs):
	while True:
		print()
		print('===========================')
		user_in = input('Введите команду: ')
		if user_in == 'p':
			print(people(documents, directories))
		elif user_in == 's':
			print(shelf(directories))
		elif user_in == 'l':
			print(list_of_persons(documents))
		elif user_in == 'a':
			print(add(documents, directories))
		elif user_in == 'd':
			print(delete(documents, directories))
		elif user_in == 'm':
			print(move(directories))
		elif user_in == 'as':
			print(add_shelf(directories))
		elif user_in == 'q':
			break


# user_control(documents, directories)