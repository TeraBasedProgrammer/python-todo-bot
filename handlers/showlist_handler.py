# from aiogram import types, Dispatcher
# from invoke_bot import bot
# from db_work import build_todos_list, build_todo, get_chosen_list


# async def show_todolist(message: types.Message):
#     is_chosen = await get_chosen_list(message.from_user.id)
#     if not is_chosen:
#         await bot.send_message(message.from_user.id, 'Похоже, вы не выбрали ни одним из доступных TODO-листов. Сделайте\
#  это и повторите попытку (/chooselist)')
#         return
#     todo = await build_todo(message.from_user.id)
#     if not todo:
#         await bot.send_message(message.from_user.id, 'Упс, кажется, список пуст.\
#  Самое время добавить в него новое задание!')
#     else:
#         await bot.send_message(message.from_user.id, todo, parse_mode='HTML')


# async def show_all_lists(message: types.Message):
#     result = await build_todos_list(message.from_user.id)
#     await bot.send_message(message.from_user.id, result[0])


# def register_handlers(dp: Dispatcher):
#     dp.register_message_handler(show_all_lists, commands=['show_all_lists'])
#     dp.register_message_handler(show_todolist, commands=['showlist'])
