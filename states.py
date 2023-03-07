from aiogram.dispatcher.filters.state import State, StatesGroup


class ListsManagementFSM(StatesGroup):
    createlist = State()
    choose_after_creation = State()
    chooselist = State()
    deletelist = State()


class GeneralFSM(StatesGroup):
    deletetask = State()
    marktask = State()


class AddTaskFSM(StatesGroup):
    addtask = State()
    repeat_addition = State()


class EditTaskFSM(StatesGroup):
    edittask_num = State()
    edittask = State()
