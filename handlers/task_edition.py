# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from .fsm import EditTaskFSM
# from db_work import db_executor, parse_task, build_todo, get_chosen_list
# from invoke_bot import bot


# async def get_edittask_num(message: types.Message, state: FSMContext):
#     task = await parse_task(message.text, message.from_user.id, 'edit')
#     if type(task) != tuple:
#         if 'список пуст' in task:
#             await state.finish()
#         await bot.send_message(message.from_user.id, task)
#         return
#     else:
#         async with state.proxy() as data:
#             data['task'] = task[1]
#         await bot.send_message(message.from_user.id, 'Текущий текст задания:')
#         await bot.send_message(message.from_user.id, task[1],
#                                entities=[{"type": "code", "offset": 0, "length": len(task[1])}])
#         await bot.send_message(message.from_user.id, 'Введите новый / отредактированный текст задания:')
#         await EditTaskFSM.next()
#         return


# async def handle_edittask(message: types.Message, state: FSMContext):
#     if len(message.text) > 400:
#         await message.reply('Задание слишком длинное. Максимально допустимая длинна задания — 400 символов.\
#  Попробуйте его укоротить и повторите попытку.')
#         return
#     elif ('🕐' in message.text) or ('🟢' in message.text):
#         await bot.send_message(message.from_user.id, 'Похоже, вы использовали зарезервированные эмоджи в задании.\
#  Сформулируйте задание без них и повторите попытку.')
#         # await state.finish()
#         await bot.send_animation(message.from_user.id,
#                                  'CgACAgIAAxkBAAIC1WLuoMBO_Z5aoR_0gA9bZP36oqNPAAJhAgACB_4JS_0jTm10ch3rKQQ')
#     else:
#         old_todo = await build_todo(message.from_user.id)
#         if len(old_todo) + len(message.text) > 4096:
#             await bot.send_message(message.from_user.id, 'Упс, кажется, ваш список уже настолько большой, что даже\
#  телеграм ругается на его длинну (более 4096 символов). Попробуйте укоротить текст этого задания, укоротить или\
#  удалить часть заданий, либо удалите уже выполненые задания и повторите попытку. Кроме того, вы\
#  можете создать ещё один список (/createlist)')
#             await state.finish()
#             return
#         else:
#             async with state.proxy() as data:
#                 current_list = await get_chosen_list(message.from_user.id)
#                 try_edit = await db_executor("""UPDATE user%s SET task_text = %s, is_edited = true
#                                              WHERE task_text = %s
#                                              AND todo_name = %s;""",
#                                              message.from_user.id,
#                                              message.text,
#                                              data['task'],
#                                              current_list)
#                 if try_edit[0] == 'UniqueViolation':
#                     await bot.send_message(message.from_user.id, 'Такое задание уже есть в списке, повторите попытку')
#                     await state.finish()
#                     return
#                 await bot.send_message(message.from_user.id, 'Задание успешно отредактировано!\
#  Теперь ваш список выглядит так: ')
#                 await bot.send_message(message.from_user.id, await build_todo(message.from_user.id), parse_mode='HTML')
#                 await state.finish()


# def register_taskedition_handlers(dp: Dispatcher):
#     dp.register_message_handler(get_edittask_num, state=EditTaskFSM.edittask_num)
#     dp.register_message_handler(handle_edittask, state=EditTaskFSM.edittask)
