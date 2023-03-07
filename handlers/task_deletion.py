# import asyncio
# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from db_work import db_executor, parse_task, build_todo, get_chosen_list
# from .fsm import GeneralFSM
# from invoke_bot import bot


# async def clear_list(message: types.Message):
#     is_chosen = await get_chosen_list(message.from_user.id)
#     if not is_chosen:
#         await bot.send_message(message.from_user.id, 'Похоже, вы не выбрали ни одним из доступных TODO-листов. Сделайте\
#  это и повторите попытку (/chooselist)')
#         return
#     await db_executor("""DELETE FROM user%s WHERE todo_name = %s AND task_text IS NOT NULL;""",
#                       message.from_user.id,
#                       is_chosen)
#     await bot.send_message(message.from_user.id, 'Список успешно очищен!')


# async def delete_completed_task(message: types.Message):
#     is_chosen = await get_chosen_list(message.from_user.id)
#     if not is_chosen:
#         await bot.send_message(message.from_user.id, 'Похоже, вы не выбрали ни одним из доступных TODO-листов. Сделайте\
#  это и повторите попытку (/chooselist)')
#         return
#     current_todo = await get_chosen_list(message.from_user.id)
#     old_todo = await build_todo(message.from_user.id)
#     if not old_todo:
#         await bot.send_message(message.from_user.id, 'Упс, кажется, список пуст.\
#  Самое время добавить в него новое задание!')
#         return
#     await db_executor("""DELETE FROM user%s WHERE is_done = true AND todo_name = %s;""",
#                       message.from_user.id, current_todo)
#     new_todo = await build_todo(message.from_user.id)
#     if len(old_todo) == len(str(new_todo)):
#         await bot.send_message(message.from_user.id, 'Похоже, у вас нет выполненных заданий')
#         await bot.send_animation(message.from_user.id,
#                                  'CgACAgIAAxkBAAID4mLvsjL0lWGbKk7OJ8fPFbr4kSdGAAI3CQACsLHYSdV1s3F7JxzeKQQ')
#         return
#     else:
#         await bot.send_message(message.from_user.id, 'Выполненные задания успешно удалены!')
#         await bot.send_message(message.from_user.id, 'Теперь ваш список выглядит так: ')
#         if not new_todo:
#             await bot.send_message(message.from_user.id, 'Упс, кажется, список пуст.\
#  Самое время добавить в него новое задание!')
#         else:
#             await bot.send_message(message.from_user.id, new_todo, parse_mode='HTML')


# async def delete_task(message: types.Message, state: FSMContext):
#     task = await parse_task(message.text, message.from_user.id, 'delete')
#     if task != 1:
#         await bot.send_message(message.from_user.id, task)
#         await state.finish()
#         return
#     else:
#         await bot.send_message(message.from_user.id, 'Задание успешно удалено из списка!')
#         await asyncio.sleep(1)
#         await bot.send_message(message.from_user.id, 'Теперь ваш список выглядит так: ')
#         todo = await build_todo(message.from_user.id)
#         if not todo:
#             await bot.send_message(message.from_user.id, 'Упс, кажется, список пуст.\
#  Самое время добавить в него новое задание!')
#         else:
#             await bot.send_message(message.from_user.id, todo, parse_mode='HTML')
#         await state.finish()
#         return


# def register_taskdeletion_handlers(dp: Dispatcher):
#     dp.register_message_handler(clear_list, commands=['clearlist'])
#     dp.register_message_handler(delete_completed_task, commands=['delete_completed_tasks'])
#     dp.register_message_handler(delete_task, state=GeneralFSM.deletetask)
