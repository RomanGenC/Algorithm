import requests
import os
from datetime import datetime

current_directory = os.getcwd()
new_directory_name = 'tasks'
new_directory_path = os.path.join(current_directory, new_directory_name)

url = "https://json.medrocket.ru/todos"
response_data = requests.get(url)

new_directory_path = os.path.join(current_directory, new_directory_name)
if not os.path.exists(new_directory_path):
    os.makedirs(new_directory_path)

dict_user_info = {}

if response_data.status_code == 200:
    data = response_data.json()
    for task in data:
        if 'userId' in task:
            if task['userId'] not in dict_user_info:
                dict_user_info[task['userId']] = {'count_tasks': 1, False: 0, True: 0, 'True_list': [],
                                                  'False_list': []}
                if task['completed'] == False:
                    dict_user_info[task['userId']][False] += 1
                    dict_user_info[task['userId']]['False_list'].append(task['title'])
                else:
                    dict_user_info[task['userId']][True] += 1
                    dict_user_info[task['userId']]['True_list'].append(task['title'])
            else:
                dict_user_info[task['userId']]['count_tasks'] += 1
                dict_user_info[task['userId']][task['completed']] += 1
                if task['completed'] == False:
                    dict_user_info[task['userId']]['False_list'].append(task['title'])
                else:
                    dict_user_info[task['userId']]['True_list'].append(task['title'])
url_1 = 'https://json.medrocket.ru/users'

response_user = requests.get(url_1)
time_file = {}
counter = 0
if response_user.status_code == 200:
    data = response_user.json()
    for user in data:
        txt_name = user['username'] + '.txt'
        file_path = new_directory_path + '\\' + txt_name
        if os.path.isfile(file_path):
            old = new_directory_path + '\\' + txt_name
            time_for_name = ''
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                second_line = lines[1]  # Чтение второй строки файла
                time_for_name = second_line[-17:-1]
                print(time_for_name)
            new = new_directory_path + '\\' + 'old_'+ txt_name[0:-4] + '_' + time_for_name.replace('.', '-').replace(' ', 'T').replace(':', '-') + '.txt'
            os.rename(old, new)

        file_path = os.path.join(new_directory_path, txt_name)
        with (open(file_path, 'w', encoding='utf-8') as file):
            counter += 1
            current_time = datetime.now()
            text_to_txt = "#Отчет для " + user['company']['name'] + '.' + '\n'
            text_to_txt += user['username'] + ' ' + user['name'] + ' <' + user['email'] + '> ' + current_time.strftime("%Y.%m.%d %H:%M") + '\n'
            text_to_txt += "Всего задач: " + str(dict_user_info[counter]['count_tasks']) + '\n\n'
            text_to_txt += '## Актуальные задачи' + '(' + str(dict_user_info[counter][False]) + '):' + '\n'
            for i in dict_user_info[counter]['False_list']:
                if len(i) > 46:
                    i = i[:46] + '...'
                text_to_txt += '- ' + i + '\n'
            text_to_txt += '\n' + '## Завершенные задачи (' + str(dict_user_info[counter][True]) + '):' + '\n'
            for i in dict_user_info[counter]['True_list']:
                if len(i) > 46:
                    i = i[:46] + '...'
                text_to_txt += '- ' + i + '\n'
            file.write(text_to_txt)


# for root, dirs, files in os.walk(new_directory_path, topdown=False):
#     for file in files:
#         file_path = os.path.join(root, file)
#         # Удаляем файл
#         os.remove(file_path)
#     for dir_name in dirs:
#         dir_path = os.path.join(root, dir_name)
#         # Удаляем поддиректорию
#         os.rmdir(dir_path)
#
# os.rmdir(new_directory_path)

# if not os.path.exists(new_directory_path):
#     os.makedirs(new_directory_path)
#     print(f"Директория '{new_directory_name}' успешно создана в {current_directory}.")
# else:
#     print(f"Директория '{new_directory_name}' уже существует в {current_directory}.")