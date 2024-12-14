from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

with open(file='UrbanM13BotKey', mode='r', encoding='utf-8') as file:
    api=file.readline()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text = 'Норма калорий?')
b2 = KeyboardButton(text = 'Информация')
kb.add(b1, b2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    activity = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот помогающий твоему здоровью. ',
                         reply_markup=kb)

@dp.message_handler(text = 'Норма калорий?')
async def set_age(message):
    await message.answer('Введите полное количество лет:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост в сантиметрах:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async  def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес в килограммах:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def set_activity(message, state):
    await state.update_data(weight = message.text)
    await message.answer('Введите насколько вы активны по шкале от 1 (в основном лежу на диване) '
                         'до 5 (занимаюсь спортом несколько раз в неделю):')
    await UserState.activity.set()

@dp.message_handler(state = UserState.activity)
async def set_sex(message, state):
    await state.update_data(activity = message.text)
    await message.answer('Введите свой пол (М/Ж):')
    await UserState.sex.set()

@dp.message_handler(state = UserState.sex)
async def send_calories(message, state):
    await state.update_data(sex = message.text)
    data = await state.get_data()
    #print(data)
    try:
        if data['sex'] == 'М':
            calories = ((10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5)
                        * float(data['activity']))
        elif data['sex'] == 'Ж':
            calories = ((10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161)
                        * float(data['activity']))
        else:
            calories = 0
    except:
            calories = 0
    await message.answer(f'Ваша норма калорий: {calories}')
    if calories == 0:
        await message.answer('Вы ввели некорректные данные, попробуйте ещё раз. Введите: Норма калорий?')
    await state.finish()

@dp.message_handler(text = 'Информация')
async def send_info(message):
    await message.answer('Одна из функций бота, расчет нормы калорий. '
                         'Для этого необходимо отправить сообщение: Норма калорий? '
                         'Или нажать на кнопку.')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)