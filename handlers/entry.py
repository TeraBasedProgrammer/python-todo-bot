from misc import dp, bot
from aiogram import types
from messages import MESSAGES
from settings import BAN_LIST


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # await start_db_query(message.from_user.id)
    await bot.send_message(message.from_user.id, 'Привет, я - терабазированный TODO-бот. С моей помощью вы сможете \
 компоновать ваши дела в TODO-листы, не выходя из телеграма! Доступные функции: добавление, отметка выполнения, \
 удаление и редактирование заданий. \
    \n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nЧтобы увидеть подробную инструкцию по использованию\
 бота, введите команду /help.')
    await bot.send_animation(message.from_user.id,
                             'CgACAgQAAxkBAAOiYuqe5kzSdF4GS-YJagVkKZFfPfIAApIKAAJkEIlT8NIwescPJOApBA')
    

@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Список доступных команд и их описания:\n\n\
/createlist - создать новый TODO-лист;\n\
/show_all_lists - выбрать TODO-лист из списка созданных вами ранее;\n\
/chooselist - выбрать список для дальнейшего использования;\n\
/showlist - вывести на экран выбранный туду-лист;\n\
/addtask - добавить новое задание в выбранный TODO-лист;\n\
/marktask - маркировать выполненное задание символом "🟢";\n\
/mark_all_tasks - отметить все задания в выбранном списке;\n\
/edittask - отредактировать задание в выбранном списке;\n\
/deletetask - удалить задание из текущего TODO-листа;\n\
/delete_completed_tasks - удалить все выполненные задания;\n\
/clearlist - очистить список;\n\
/deletelist - удалить выбранный TODO-лист.')




