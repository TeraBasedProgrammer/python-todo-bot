# import random
# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ReplyKeyboardRemove, KeyboardButton
# from invoke_bot import bot
# from db_work import db_executor, build_todos_list, parse_list, build_todo
# from .fsm import ListsManagementFSM
# from config import ok_stickers
# from keyboards import answear_keyboard, lists_keyboard


# async def create_list(message: types.Message, state: FSMContext):
#     listof_lists = await db_executor("""SELECT DISTINCT todo_name FROM user%s ORDER BY todo_name;""",
#                                      message.from_user.id)
#     if len(listof_lists) > 9:
#         await bot.send_message(message.from_user.id, 'Похоже, допустимое количество списков достигло максимума (10).\
#  Удалите часть списков и повторите попытку')
#         await state.finish()
#         return
#     for lst in listof_lists:
#         if message.text == lst[0]:
#             await bot.send_message(message.from_user.id, 'Такой список уже существует, введите другое название')
#             return
#     if len(message.text) > 100:
#         await bot.send_message(message.from_user.id, 'Слишком длинное название списка.\
#  Укоротите его и повторите попытку')
#         return
#     await db_executor("INSERT INTO user%s(todo_name, task_text, is_done, is_edited) VALUES (%s, null, null, null)",
#                       message.from_user.id, message.text)
#     await bot.send_message(message.from_user.id, 'Список TODO-листов обновлён')
#     lists_keyboard.add(KeyboardButton(f'{int(len(listof_lists) + 1)}'))
#     result = await build_todos_list(message.from_user.id)
#     await bot.send_message(message.from_user.id, result[0])
#     await bot.send_message(message.from_user.id, 'Желаете сразу выбрать этот список для дальнейшей работы?',
#                            reply_markup=answear_keyboard)
#     await ListsManagementFSM.next()
#     async with state.proxy() as data:
#         data['list'] = message.text


# async def handle_cac_answear(message: types.Message, state: FSMContext):
#     if message.text == 'Да':
#         async with state.proxy() as data:
#             await db_executor("""UPDATE usercurrentlist SET todo_name = %s
#                                  WHERE user_id = %s""", data['list'], message.from_user.id)
#             await bot.send_message(message.from_user.id, f'Вы успешно выбрали список "{data["list"]}".',
#                                    reply_markup=ReplyKeyboardRemove())
#             await state.finish()
#     elif message.text == 'Нет':
#         await bot.send_message(message.from_user.id, 'Ок', reply_markup=ReplyKeyboardRemove())
#         await bot.send_sticker(message.from_user.id,
#                                ok_stickers[random.randint(0, len(ok_stickers) - 1)])
#         await state.finish()
#     else:
#         await bot.send_message(message.from_user.id, 'Некорректный ответ, введите либо "Да", либо "Нет".')
#         return


# async def delete_list(message: types.Message, state: FSMContext):
#     current_todo = await parse_list(message.text, message.from_user.id)
#     if type(current_todo) != tuple:
#         await bot.send_message(message.from_user.id, current_todo)
#         return
#     else:
#         await db_executor("DELETE FROM user%s WHERE todo_name = %s;", message.from_user.id, current_todo[0])
#         await db_executor("UPDATE usercurrentlist SET todo_name = null WHERE user_id = %s ", message.from_user.id)
#         lists_keyboard.keyboard = lists_keyboard.keyboard[:-1]
#         await bot.send_message(message.from_user.id, 'Список TODO-листов обновлён', reply_markup=ReplyKeyboardRemove())
#         result = await build_todos_list(message.from_user.id)
#         await bot.send_message(message.from_user.id, result[0])
#         await state.finish()


# async def choose_list(message: types.Message, state: FSMContext):
#     current_todo = await parse_list(message.text, message.from_user.id)
#     if type(current_todo) != tuple:
#         await bot.send_message(message.from_user.id, current_todo)
#         return
#     else:
#         await db_executor("UPDATE usercurrentlist SET todo_name = %s WHERE user_id = %s",
#                           current_todo[0],
#                           message.from_user.id)
#         await bot.send_message(message.from_user.id, f'Вы успешно выбрали список "{current_todo[0]}".',
#                                reply_markup=ReplyKeyboardRemove())
#         todo = await build_todo(message.from_user.id)
#         if not todo:
#             await bot.send_message(message.from_user.id, 'Упс, кажется, список пуст.\
#  Самое время добавить в него новое задание!')
#             await state.finish()
#         else:
#             await bot.send_message(message.from_user.id, todo, parse_mode='HTML')
#             await state.finish()


# def register_lm_handlers(dp: Dispatcher):
#     dp.register_message_handler(create_list, state=ListsManagementFSM.createlist)
#     dp.register_message_handler(handle_cac_answear, state=ListsManagementFSM.choose_after_creation)
#     dp.register_message_handler(delete_list, state=ListsManagementFSM.deletelist)
#     dp.register_message_handler(choose_list, state=ListsManagementFSM.chooselist)
