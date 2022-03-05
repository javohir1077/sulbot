from unicodedata import category
from aiogram.dispatcher.filters.state import State,StatesGroup
from numpy import product

class kafe(StatesGroup):
    category = State()
    product = State()
    amount = State()