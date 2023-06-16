
#  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
#  телефона - данные, которые должны находиться в файле.
#       1. Программа должна выводить данные
#       2. Программа должна сохранять данные в текстовом файле
#       3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
#       4. Использование функций. Ваша программа не должна быть линейной
#       5. Дополнить телефонный справочник возможностью изменения и удаления данных. 
#          Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


import csv
phonebook = []

# search for all contacts:
def search_result():
    if len(phonebook) == 0:
        print('Phonebook is empty')
    else:
        for contact in phonebook:
            print(contact)


# search the contact by surname:
def search_by_name(last_name):
    result = []
    for contact in phonebook:
        if contact[0].lower() == last_name.lower():
            result.append(contact)
    if len(result) == 0:
        print("Phonebook hasn't", last_name,  "contact")
    else:
        print(result)


# search the contact by phonenumber:
def search_by_number(number):
    result = []
    for contact in phonebook:
        if number in contact[2]:
            result.append(contact)
    if len(result) == 0:
        print("Phonebook doesn't include", number, "number") 
    else:
        print(*result)


# add a new contact:
def add_contact():
    last_name = input('Insert your surname: ').title()
    first_name = input('Insert your name: ').title()
    phonenumber = input('Insert your phonenumber: ')
    phonebook.append([last_name, first_name, phonenumber])
    print(*phonebook, sep='\n')


# delete a contact:
def delete_contact():
    last_name = input('Insert surname: ')
    for contact in phonebook:
        if contact[0].lower() == last_name.lower():
            phonebook.remove(contact)
            print(last_name, 'was deleted')
            return True
    print(last_name, "wasn't found in phonebook")
    return False


# save the phonebook in file:
def save_file():
    file_name = input('Insert name file: ')
    with open(file_name, 'a', encoding='utf-8') as file:
        for contact in phonebook:
            file.write(contact[0] + ' ' + contact[1] + ' ' + contact[2] + '\n')


# download the phonebook from file:
def download_file():
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            phonebook.append(row)
            print(row)

# main menu:
while True:
    print('1. Show all contacts')
    print('2. Search the contact by surname')
    print('3. Search the contact by phonenumber')
    print('4. Add a new contact')
    print('5. Delete a contact')
    print('6. Save phonebook in file')
    print('7. Download phonebook from file')
    print('8. Exit')
    choise = int(input('Choose a command from menu: '))
    if choise == 1:
        search_result() 
    elif choise == 2:
        search_by_name(input('Insert the surname: '))
    elif choise == 3:
        search_by_number(input('Insert phone number: '))
    elif choise == 4:
        add_contact()
    elif choise == 5:
        delete_contact()
    elif choise == 6:
        save_file()
    elif choise == 7:
        download_file()
    elif choise == 8:
        break
    else:
        print('Wrong input')
    
    
