# import random
# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.types import ReplyKeyboardRemove
# from .fsm import AddTaskFSM
# from db_work import db_executor, build_todo, get_chosen_list, taskcount_is_valid
# from invoke_bot import bot
# from config import ok_stickers
# from keyboards import answear_keyboard


# async def handle_addtask(message: types.Message, state: FSMContext):
#     if len(message.text) > 400:
#         await message.reply('Задание слишком длинное. Максимально допустимая длинна задания — 400 символов.\
#  Попробуйте его укоротить и повторите попытку.')
#         return
#     elif ('🕐' in message.text) or ('🟢' in message.text):
#         await bot.send_message(message.from_user.id, 'Похоже, вы использовали зарезервированные эмоджи в задании.\
#  Сформулируйте задание без них и повторите попытку.')
#         await bot.send_animation(message.from_user.id,
#                                  'CgACAgIAAxkBAAIC1WLuoMBO_Z5aoR_0gA9bZP36oqNPAAJhAgACB_4JS_0jTm10ch3rKQQ')
#     else:
#         old_todo = await build_todo(message.from_user.id)
#         if len(str(old_todo)) + 6 + len(message.text) > 4096:
#             await bot.send_message(message.from_user.id, 'Упс, кажется, ваш список уже настолько большой,\
#  что даже телеграм ругается на его длинну (более 4096 символов). Попробуйте текст этого задания, укоротить или удалить\
#  часть заданий, либо удалите уже выполненые задания и повторите попытку. Кроме того, вы можете создать ещё один список\
# (/createlist))')
#             await state.finish()
#             return
#         else:
#             current_todo = await get_chosen_list(message.from_user.id)
#             try_add = await db_executor("""INSERT INTO user%s (todo_name, task_text, is_done, is_edited) 
#                                            VALUES(%s, %s, False, False);""",
#                                         message.from_user.id, current_todo, message.text)
#             if try_add[0] == 'UniqueViolation':
#                 await bot.send_message(message.from_user.id, f'Такое задание уже есть в списке, повторите попытку')
#                 return
#             todo = await build_todo(message.from_user.id)
#             await bot.send_message(message.from_user.id, 'Список успешно дополнен, теперь он выглядит так:')
#             await bot.send_message(message.from_user.id, todo, parse_mode='HTML')
#             await bot.send_message(message.from_user.id, 'Желаете добавить ещё одно задание? ("Да", "Нет")',
#                                    reply_markup=answear_keyboard)
#             await AddTaskFSM.next()


# async def handle_repeat_add(message: types.Message, state: FSMContext):
#     if message.text == 'Да':
#         if not await taskcount_is_valid(message.from_user.id):
#             await bot.send_message(message.from_user.id, 'Похоже, количество заданий в списке достигло максимума (50).\
#         Удалите часть заданий и повторите попытку', reply_markup=ReplyKeyboardRemove())
#             await state.finish()
#         else:
#             await AddTaskFSM.addtask.set()
#             await bot.send_message(message.from_user.id, 'Введите текст задания:', reply_markup=ReplyKeyboardRemove())
#             return
#     elif message.text == 'Нет':
#         await bot.send_message(message.from_user.id, 'Ок', reply_markup=ReplyKeyboardRemove())
#         await bot.send_sticker(message.from_user.id,
#                                ok_stickers[random.randint(0, len(ok_stickers) - 1)])
#         await state.finish()
#     else:
#         await bot.send_message(message.from_user.id, 'Некорректный ответ, введите либо "Да", либо "Нет".')
#         return


# def register_taskaddition_handlers(dp: Dispatcher):
#     dp.register_message_handler(handle_addtask, state=AddTaskFSM.addtask)
#     dp.register_message_handler(handle_repeat_add, state=AddTaskFSM.repeat_addition)
