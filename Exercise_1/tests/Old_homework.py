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
	result_persons = ''
	for id, person in enumerate(docs):
		data = f"{person['type']}  {person['number']}  {person['name']} "
		result_persons = result_persons + data + '\n'
	return result_persons


def add(new_type, new_number, new_name, shelf):
	new_person = {"type": new_type, "number": new_number, "name": new_name}
	documents.append(new_person)
	result = None
	while result is None:
		for position in directories:
			if shelf == position:
				directories[position].append(new_number)
				result = f'\n {documents} \n \n {directories}'
				number_of_docs = len(documents)
				number_of_dirs = 0
				number_of_dirs = sum([number_of_dirs + len(docums) for row, docums in directories.items()])
				return [number_of_docs, number_of_dirs]
		if result == None:
			return 'Такой полки не существует!'



def delete(docs, dirs):
	result = 0
	while result == 0:
		number = input('Введите номер документа для удаления: ')
		for shl, numbers in dirs.items():
			for num in numbers:
				if number == num:
					numbers.remove(num)
					result +=1
					for person in docs:
						if number == person['number']:
							docs.remove(person)
							result +=1
		if result == 0:
			return 'Документ с таким номером отсутствует в базе!'
	result_del = f'\n {docs} \n \n {dirs}'
	number_of_dirs = 0
	number_of_dirs = sum([number_of_dirs + len(docums) for row, docums in dirs.items()])
	return [len(docs), number_of_dirs]


def move(dirs, desired_shelf):
	result = 0
	result2 = 0
	while result == 0:
		number = input('Введите номер документа: ')
		for shl, numbers in dirs.items():
			for num in numbers:
				if number == num:
					numbers.remove(num)
					result += 1
		if result == 0:
			return 'Документ с таким номером отсутствует в базе!'
	while result2 == 0:
		# desired_shelf = input('Введите номер полки для перемещения: ')
		if desired_shelf in dirs:
			dirs[desired_shelf].append(number)
			result2 += 1
			str(desired_shelf)
			length = len(dirs[desired_shelf])
		else:
			return 'Такой полки не существует!'
	return length


def add_shelf(last_dirs):
	result = 0
	while result == 0:
		desired_shelf = input('Введите номер полки для создания: ')
		for shelf in last_dirs:
			if desired_shelf == shelf:
				return 'Такая полка уже существует!'
		if desired_shelf != shelf:
			last_dirs[desired_shelf] = []
			result += 1
	number_of_dirs = len(last_dirs)
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