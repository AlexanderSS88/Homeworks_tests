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
	result = 0
	while result == 0:
		# number = input('Введите номер документа: ')
		for shl, numbers in dirs.items():
			for num in numbers:
				if number == num:
					for person in docs:
						if number == (person['number']):
							final_result = person['name']
							result += 1
					if result == 0 and number == num:
						final_result = 'Документ с таким номером хранится' \
									   ' на полках, однако данные о ' \
									   'человеке в базе отсутствуют.'
						result += 1
		if result == 0:
			print('Документ с таким номером отсутствует '
				  'в базе! Повторите ввод ')
	return final_result


def shelf(dirs):
	result = 0
	while result == 0:
		number = input('Введите номер документа: ')
		for shl, numbers in dirs.items():
			for num in numbers:
				if number == num:
					needed_shelf = f'Документ находится на полке № {shl}'
					result += 1
		if result == 0:
			print('Документ с таким номером отсутствует в базе! Повторите ввод ')
	return needed_shelf


def list_of_persons(docs):
	result_persons = ''
	for id, person in enumerate(docs):
		data = f"{person['type']}  {person['number']}  {person['name']} "
		result_persons = result_persons + data + '\n'
	return result_persons


def add(docs, dirs):
	new_type = input('Введите тип документа: ')
	new_number = input('Ведите номер документа : ')
	new_name = input('Введите имя и фамилию: ')
	new_person = {"type": new_type, "number": new_number, "name": new_name}
	docs.append(new_person)
	result = None
	while result is None:
		shelf = input('Введите номер полки, куда положить документ: ')
		for position in dirs:
			if shelf == position:
				dirs[position].append(new_number)
				result = f'\n {docs} \n \n {dirs}'
		if result == None:
			print('Такой полки не существует! Повторите ввод ')
	return result


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
			print('Документ с таким номером отсутствует '
				  'в базе! Повторите ввод.')
	result_del = f'\n {docs} \n \n {dirs}'
	return result_del


def move(dirs):
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
			print('Документ с таким номером отсутствует в базе! Повторите ввод')
	while result2 == 0:
		desired_shelf = input('Введите номер полки для перемещения: ')
		if desired_shelf in dirs:
			dirs[desired_shelf].append(number)
			result2 += 1
		else:
			print('Такой полки не существует! Повторите ввод ')
			result2 = 0
	return dirs


def add_shelf(last_dirs):
	result = 0
	while result == 0:
		desired_shelf = input('Введите номер полки для создания: ')
		for shelf in last_dirs:
			if desired_shelf == shelf:
				print('Такая полка уже существует! Повторите ввод')
				break
		if desired_shelf != shelf:
			last_dirs[desired_shelf] = []
			result += 1
	return last_dirs


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
user_control(documents, directories)