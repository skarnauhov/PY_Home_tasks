from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
import asyncio

ACTIVITY = {'1': 1.2, '2': 1.375, '3': 1.55, '4': 1.725, '5': 1.9}
PRODUCTS = ('пусто', 'Яблоко', 'Груша', 'Апельсин', 'Хурма')

with open(file=r'..\Module_13\UrbanM13BotKey', mode='r', encoding='utf-8') as file:
    api=file.readline()

bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text = 'Норма калорий?')],
    [KeyboardButton(text = 'Купить')],
    [KeyboardButton(text = 'Информация')]
    ], resize_keyboard=True)

kb_i = InlineKeyboardMarkup(resize_keyboard=True)
b_i_1 = InlineKeyboardButton(text='Рассчитать норму калорий.', callback_data='calories')
b_i_2 = InlineKeyboardButton(text='Формулы расчета.', callback_data='formulas')
kb_i.add(b_i_1, b_i_2)

kb_i_buy = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1. Яблоко', callback_data='product_buying')],
    [InlineKeyboardButton(text='2. Груша', callback_data='product_buying')],
    [InlineKeyboardButton(text='3. Апельсин', callback_data='product_buying')],
    [InlineKeyboardButton(text='4. Хурма', callback_data='product_buying')],
], resize_keyboard=True)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    sex = State()
    activity = State()

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет, {message.from_user.first_name}! Я бот помогающий твоему здоровью. '
                         f'Используйте клавиатуру для работы.', reply_markup=kb)

@dp.message_handler(text = 'Норма калорий?')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb_i)

@dp.message_handler(text = 'Купить')
async def get_buying_list(message):
    for _ in range(1, 5):
        with open(f'{_}.png', 'rb') as photo:
            await message.answer_photo(photo, f'Название: {PRODUCTS[_]} | Описание: {_*100} ккал | Цена: {_*200} рублей за штуку.')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_i_buy)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Используется формула Миффлина-Сан Жеора,\n'
                              'которая дает более точную информацию\n'
'и учитывает степень физической активности человека:\n\n'
'для мужчин:\n(10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A;\n\n'
'для женщин:\n(10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) – 161) x A.\n\n'
'A – это уровень активности человека,\n'
'его различают обычно по пяти степеням физических нагрузок в сутки:\n\n'
'Минимальная активность: A = 1,2.\n'
'Слабая активность: A = 1,375.\n'
'Средняя активность: A = 1,55.\n'
'Высокая активность: A = 1,725.\n'
'Экстра-активность: A = 1,9\n(под эту категорию обычно подпадают люди,\nзанимающиеся, например, тяжелой атлетикой,\n'
'или другими силовыми видами спорта с ежедневными тренировками,\n'
'а также те, кто выполняет тяжелую физическую работу).'
)
    await call.answer()

@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите полное количество лет:')
    await call.answer()
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
                         'до 5 (занимаюсь спортом ежедневно):')
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
        if data['sex'].lower() == 'м':
            calories = ((10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5)
                        * ACTIVITY[data['activity']])
        elif data['sex'].lower() == 'ж':
            calories = ((10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) - 161)
                        * ACTIVITY[data['activity']])
        else:
            calories = 0
    except:
            calories = 0
    await message.answer(f'Ваша суточная норма килокалорий: {calories} ')
    if calories == 0:
        await message.answer('Вы ввели некорректные данные, попробуйте ещё раз. Введите: Норма калорий?')
    elif calories > 10000:
        await message.answer('К сожалению, для инопланетных существ подсчет может быть не точным. Обратитесь к доктору.')
    await state.finish()

@dp.message_handler(text = 'Информация')
async def send_info(message):
    await message.answer('Одна из функций бота, расчет нормы калорий. '
                         'Для этого необходимо отправить сообщение: Норма калорий? '
                         'Или нажать на кнопку. '
                         'А также доступна формула Миффлина-Сан Жеора по которой происходит расчёт.')

@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)