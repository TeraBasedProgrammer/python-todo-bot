# import random
# from aiogram import types, Dispatcher
# from invoke_bot import bot
# import config


# Получение id стикеров  


# async def get_sticker(message: types.Message):
#     sticker_id = message.values['sticker']['file_id']
#     print(sticker_id)
#     await bot.send_message(message.from_user.id, "Получил стикер")
#     await bot.send_sticker(message.from_user.id, sticker_id)
#
#
# # Получение id гифок
#
# async def get_gif(message: types.Message):
#     print(message.values['animation']['file_id'])
#     await bot.send_message(message.from_user.id, 'Получил гифку')


# async def devel_comm_handler(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Данная функция находится в разработке💻')
#     await bot.send_animation(message.from_user.id,
#                              'CgACAgIAAxkBAAIIuWLyJIJrsv03B4no_oQfWyH6b-ihAALNGQACoduQS4C7rpJ_SdrxKQQ')


# async def wrong_command_handler(message: types.message):
#     await bot.send_message(message.from_user.id, "Я не знаю такой команды")
#     await bot.send_animation(message.from_user.id,
#                              config.command_unknown_gifs[random.randint(0, len(config.command_unknown_gifs) - 1)])


# def register_other_handlers(dp: Dispatcher):
#     # dp.register_message_handler(get_sticker, content_types='sticker')
#     # dp.register_message_handler(get_gif, content_types='animation')
#     dp.register_message_handler(devel_comm_handler, commands=[])
#     dp.register_message_handler(wrong_command_handler)
