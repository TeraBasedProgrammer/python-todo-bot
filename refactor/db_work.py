# import os
# import psycopg2
# from aiogram.types import KeyboardButton
# from keyboards import lists_keyboard

# # Функция подключения к БД и отправки запроса


# async def db_executor(query: str, *args):
#     connection = psycopg2.connect(host=os.getenv('DB_HOST'),
#                                   user=os.getenv('DB_USER'),
#                                   password=os.getenv('DB_PASS'), 
#                                   database=os.getenv('DB_NAME'))
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query, args)
#         result = cursor.fetchall()
#     except Exception as ex:
#         return [type(ex).__name__, str(ex)]
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#     return result


# # Создание таблицы в БД (если её нет) при получении команды /start

# async def start_db_query(user_id: int):
#     await db_executor("""CREATE TABLE IF NOT EXISTS user%s(
#     id serial primary key,
#     todo_name TEXT,
#     task_text TEXT,
#     is_done BOOL,
#     is_edited BOOL,
#     UNIQUE(task_text));""", user_id)

#     await db_executor("""CREATE TABLE IF NOT EXISTS usercurrentlist(
#     user_id int primary key,
#     todo_name varchar(200)
#     )
#     """)

#     await db_executor("INSERT INTO usercurrentlist (user_id, todo_name) VALUES (%s, null)", user_id)


# # Получение выбранного TODO-листа

# async def get_chosen_list(user_id: int):
#     data = await db_executor("SELECT todo_name FROM usercurrentlist WHERE user_id = %s", user_id)
#     return data[0][0]


# # Функция построения туду-листа в виде красивой строки

# async def build_todo(user_id: int):
#     current_todo = await get_chosen_list(user_id)
#     data = await db_executor("SELECT * FROM user%s WHERE todo_name = %s ORDER BY id;", user_id, current_todo)
#     todo_list = f'TODO-лист "{current_todo}": \n\n'
#     iterator = 0
#     for i in range(0, len(data)):
#         if not data[i][2]:
#             continue
#         if data[i][3]:
#             todo_list += f'🟢 {iterator + 1}) {data[i][2]}\n'
#             iterator += 1
#         else:
#             todo_list += f'🕐 {iterator + 1}) {data[i][2]}\n'
#             iterator += 1
#         if data[i][4]:
#             todo_list = todo_list[:-1] + ' <i>(изм.)</i>\n'
#     if todo_list == f'TODO-лист "{current_todo}": \n\n':
#         return False
#     return todo_list


# # Функция формирования списка TODO-листов

# async def build_todos_list(user_id: int):
#     lists = await db_executor("""SELECT DISTINCT todo_name 
#                                  FROM user%s 
#                                  ORDER BY todo_name;""", user_id)
#     if not lists:
#         return 'Похоже, у вас нет ни одного TODO-листа. Создайте новый\
#  список (/createlist) и повторите попытку', False
#     listof_lists = 'Доступные списки:\n\n'
#     for i in range(len(lists)):
#         listof_lists += f'{i + 1}) {lists[i][0]}\n'
#     return listof_lists, True


# # Функция вытягивания задания из туду-листа по номеру для его дальнейшей обработки

# async def parse_task(task_num, user_id: int, command: str):
#     if not task_num.isdigit():
#         return 'Похоже, вы ввели отрицательное число, или вовсе не число, повторите попытку.'
#     elif int(task_num) <= 0:
#         return 'Похоже, вы ввели некорректное число. Минимально возможное число — "1". Повторите попытку'

#     # Попробовать сделать SQL-запрос только на таски
#     current_todo = await get_chosen_list(user_id)
#     data = await db_executor('SELECT * FROM user%s WHERE todo_name = %s ORDER BY id;', user_id, current_todo)
#     if len(data[1:]) == 0:
#         return 'Этот список пуст. Добавьте новое задание (/addtask) и повторите попытку'

#     else:
#         try:
#             task = data[1:][int(task_num) - 1][2]
#             if command == 'mark':
#                 is_done = await db_executor("""SELECT is_done FROM user%s WHERE task_text = %s 
#                                             AND todo_name = %s;""", user_id, task, current_todo)
#                 if is_done[0][0]:
#                     return 'Кажется, это задание уже выполнено'
#                 else:
#                     await db_executor("""UPDATE user%s SET is_done = true WHERE task_text = %s
#                                        AND todo_name = %s;""", user_id, task, current_todo)
#                     return 1
#             elif command == 'delete':
#                 await db_executor("""DELETE FROM user%s WHERE task_text = %s
#                                   AND todo_name = %s;""", user_id, task, current_todo)
#                 return 1
#             else:
#                 return 1, task
#         except IndexError:
#             return 'Задания с таким номером нет в списке, повторите попытку'


# async def parse_list(list_num, user_id):
#     if not list_num.isdigit():
#         return 'Похоже, вы ввели отрицательное число, или вовсе не число, повторите попытку.'
#     elif int(list_num) <= 0:
#         return 'Похоже, вы ввели некорректное число. Минимально возможное число — "1". Повторите попытку'
#     lists = await db_executor('SELECT DISTINCT todo_name FROM user%s ORDER BY todo_name;', user_id)
#     if len(lists) == 0:
#         return 'Упс, кажется, у вас нет ни одного TODO-листа.\
#     Самое время создать новый!'
#     else:
#         try:
#             list_name = lists[int(list_num) - 1][0]
#             return list_name, True
#         except IndexError:
#             return 'Списка под таким номером нет, повторите попытку'


# # Проверка на превышение количества заданий в списке

# async def taskcount_is_valid(user_id: int) -> bool:
#     current_todo = await get_chosen_list(user_id)
#     data = await db_executor("SELECT COUNT(*) FROM user%s WHERE task_text IS NOT NULL AND todo_name = %s;",
#                              user_id, current_todo)
#     if data[0][0] > 49:
#         return False
#     return True


# async def fill_keyboard(user_id: int):
#     if lists_keyboard.keyboard:
#         return
#     else:
#         data = await db_executor("""SELECT DISTINCT COUNT(*) FROM user%s
#                                     WHERE task_text IS NULL;""", user_id)
#         for i in range(data[0][0]):
#             lists_keyboard.add(KeyboardButton(f'{int(i + 1)}'))
