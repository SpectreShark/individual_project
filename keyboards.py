from aiogram import types


def initial_keyboard():
    buttons = [[types.InlineKeyboardButton(text=f"Задание {i}", callback_data=f"task_{i}")] for i in range(1, 16)]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons, row_width=3)


def first_task():
    buttons = [
        [types.InlineKeyboardButton(text="Кодировка, в которой каждый символ кодируется 8 битами", callback_data="test_1_variation_1")],
        [types.InlineKeyboardButton(text="Кодировка, в которой каждый символ кодируется 16 битами", callback_data="test_1_variation_2")],
        [types.InlineKeyboardButton(text="Кодировка, в которой каждый символ кодируется 32 битами", callback_data="test_1_variation_3")],
        [types.InlineKeyboardButton(text="Разные задачи", callback_data="test_1_variation_4")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def second_task():
    buttons = [
        [types.InlineKeyboardButton(text="Шифр, состоящий из символов", callback_data="test_2_variation_1")],
        [types.InlineKeyboardButton(text="Шифр, состоящий из цифр", callback_data="test_2_variation_2")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def third_task():
    buttons = [
        [types.InlineKeyboardButton(text="Поиск наибольшего значения переменной", callback_data="test_3_variation_1")],
        [types.InlineKeyboardButton(text="Поиск наименьшего значения переменной", callback_data="test_3_variation_2")],
        [types.InlineKeyboardButton(text="Поиск неизвестного числа", callback_data="test_3_variation_3")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def fourth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Анализ схемы", callback_data="test_4_variation_1")],
        [types.InlineKeyboardButton(text="Анализ таблицы", callback_data="test_4_variation_2")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def fifth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Получение большего числа из меньшего", callback_data="test_5_variation_1")],
        [types.InlineKeyboardButton(text="Получение меньшего числа из большего", callback_data="test_5_variation_2")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)

def sixth_task():
    buttons = [[types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_6_variation_1")]]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def seventh_task():
    buttons = [
        [types.InlineKeyboardButton(text="Восстановление IP-адреса", callback_data="test_7_variation_1")],
        [types.InlineKeyboardButton(text="Кодировка адреса почтового ящика", callback_data="test_7_variation_2")],
        [types.InlineKeyboardButton(text="Кодировка адреса файла", callback_data="test_7_variation_3")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def eighth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Запрос, состоящий из двух слов", callback_data="test_8_variation_1")],
        [types.InlineKeyboardButton(text="Запрос, состоящий из одного слова", callback_data="test_8_variation_2")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def ninth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Поиск путей из одного города в другой", callback_data="test_9_variation_1")],
        [types.InlineKeyboardButton(text="Поиск путей из одного города в другой, проходящих, или не проходящих через определенный пункт", callback_data="test_9_variation_2")],
        [types.InlineKeyboardButton(text="Поиск путей из одного города в другой, проходящих, или не проходящих через определенный пункт продолжение", callback_data="test_9_variation_3")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def tenth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Перевод чисел из одной системы счисления в другую", callback_data="test_10_variation_1")],
        [types.InlineKeyboardButton(text="Поиск наименьшего или наибольшего числа", callback_data="test_10_variation_2")],
        [types.InlineKeyboardButton(text="Сумма и количество цифр в записи числа в различных системах счисления", callback_data="test_10_variation_3")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def eleventh_task():
    buttons = [[types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_11_variation_1")]]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def twelfth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Количество файлов с определенным расширением", callback_data="test_12_variation_1")],
        [types.InlineKeyboardButton(text="Количество файлов с определенным расширением необходимого объема", callback_data="test_12_variation_2")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def thirteenth_task():
    buttons = [[types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_13_variation_1")]]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def fourteenth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_14_variation_1")],
        [types.InlineKeyboardButton(text="Задания для подготовки продолжение", callback_data="test_14_variation_2")]
        ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def fifteenth_task():
    buttons = [
        [types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_15_variation_1")],
        [types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_15_variation_2")],
        [types.InlineKeyboardButton(text="Задания для подготовки", callback_data="test_15_variation_3")]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
