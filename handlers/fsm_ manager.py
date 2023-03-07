from aiogram import types
from aiogram.dispatcher import FSMContext
from misc import dp, bot
# from db_work import build_todos_list, get_chosen_list, taskcount_is_valid, fill_keyboard
# from keyboards import lists_keyboard


@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('Операция отменена')


# Refactor (get rid of 'ifs' and separate big handlers into single command' ones)

#     async def invoke_fsm(message: types.Message):
#     is_chosen = await get_chosen_list(message.from_user.id)
#     if not is_chosen:
#         await bot.send_message(message.from_user.id, 'Похоже, вы не выбрали ни одним из доступных TODO-листов. Сделайте\
#  это и повторите попытку (/chooselist)')
#         return
#     elif message.text == '/addtask':
#         if not await taskcount_is_valid(message.from_user.id):
#             await bot.send_message(message.from_user.id, 'Похоже, количество заданий в списке достигло максимума (50).\
#  Удалите часть заданий и повторите попытку')
#             return
#         await AddTaskFSM.addtask.set()
#         await bot.send_message(message.from_user.id, 'Введите текст задания:')
#     elif message.text == '/deletetask':
#         await GeneralFSM.deletetask.set()
#         await bot.send_message(message.from_user.id, 'Введите номер задания, которое хотите удалить:')
#     elif message.text == '/marktask':
#         await GeneralFSM.marktask.set()
#         await bot.send_message(message.from_user.id,
#                                'Введите номер задания, которое вы хотите пометить как выполненное:')
#     elif message.text == '/edittask':
#         await EditTaskFSM.edittask_num.set()
#         await bot.send_message(message.from_user.id, 'Введите номер задания, которое хотите отредактировать:')
#     else:
#         return


# def register_fsm_handlers(dp: Dispatcher):
#     dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
#     dp.register_message_handler(invoke_lm_fsm, commands=['createlist', 'deletelist', 'chooselist'])
#     dp.register_message_handler(invoke_fsm, commands=['addtask', 'marktask', 'edittask', 'deletetask'], state=None)
