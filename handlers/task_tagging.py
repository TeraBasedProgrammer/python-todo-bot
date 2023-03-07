# import asyncio
# import random
# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from db_work import parse_task, build_todo, db_executor, get_chosen_list
# from .fsm import GeneralFSM
# from invoke_bot import bot
# import config


# async def mark_task(message: types.Message, state: FSMContext):
#     task = await parse_task(message.text, message.from_user.id, 'mark')
#     if task != 1:
#         await bot.send_message(message.from_user.id, task)
#         return
#     else:
#         await bot.send_message(message.from_user.id, 'Поздравляю! Задание выполнено!')
#         flag = random.randint(0, 1)
#         if flag:
#             await bot.send_animation(message.from_user.id,
#                                      config.task_isdone_gifs[random.randint(0, len(config.task_isdone_gifs) - 1)])
#         else:
#             await bot.send_sticker(message.from_user.id,
#                                    config.task_isdone_stickers[random.randint(0, len(config.task_isdone_stickers) - 1)])
#         await asyncio.sleep(1)
#         await bot.send_message(message.from_user.id, 'Теперь ваш список выглядит так: ')
#         await bot.send_message(message.from_user.id, await build_todo(message.from_user.id), parse_mode='HTML')
#         await state.finish()
#         return


# async def mark_all_tasks(message: types.Message):
#     is_chosen = await get_chosen_list(message.from_user.id)
#     if not is_chosen:
#         await bot.send_message(message.from_user.id, 'Похоже, вы не выбрали ни одним из доступных TODO-листов. Сделайте\
#  это и повторите попытку (/chooselist)')
#         return
#     current_todo = await get_chosen_list(message.from_user.id)
#     tagged_tasks = await db_executor("""SELECT * FROM user%s WHERE is_done = false
#                                      AND todo_name = %s;""", message.from_user.id, current_todo)
#     if not tagged_tasks:
#         await bot.send_message(message.from_user.id, 'Упс, кажется, все задания уже выполненны.')
#         return
#     await db_executor("""UPDATE user%s SET is_done = true WHERE todo_name = %s;""", message.from_user.id, current_todo)
#     await bot.send_message(message.from_user.id, 'Все задания отмечены как выполненные!')
#     await bot.send_animation(message.from_user.id,
#                              'CgACAgIAAxkBAAIL4GLzepgSQEDZNuVMiFAQNfIVtineAALODwACn89pStVBA7CQ2fsTKQQ')
#     await bot.send_message(message.from_user.id, 'Теперь ваш список выглядит так: ')
#     await bot.send_message(message.from_user.id, await build_todo(message.from_user.id), parse_mode='HTML')


# def register_taskmarking_handlers(dp: Dispatcher):
#     dp.register_message_handler(mark_task, state=GeneralFSM.marktask)
#     dp.register_message_handler(mark_all_tasks, commands=['mark_all_tasks'])
