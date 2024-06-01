from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Пользовательский интерфейс для работы с ботом а именно клавиатура

startKb = InlineKeyboardBuilder().button(text='Начать работу ⛏', callback_data="prgmng")

afterStart = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text="Выбор дня: ", callback_data="changeday"),
    types.InlineKeyboardButton(text="Об авторах: ", callback_data="aboutus"),
    width=1
)

changeCinema_tonight = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text="ТРЦ РИО", callback_data="rio"),
    types.InlineKeyboardButton(text="Буревестник", callback_data="bur"),
    types.InlineKeyboardButton(text="Золотая Миля", callback_data="goldmile"),
    types.InlineKeyboardButton(text="ТРК Небо", callback_data="sky"),
    types.InlineKeyboardButton(text="ТРЦ Индиго", callback_data="indigo"),
    types.InlineKeyboardButton(text="<< Назад", callback_data="prgmng"),
    width=1
)

changeCinema_tommorow = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text="ТРЦ РИО", callback_data="rio-1"),
    types.InlineKeyboardButton(text="Буревестник", callback_data="bur-1"),
    types.InlineKeyboardButton(text="Золотая Миля", callback_data="goldmile-1"),
    types.InlineKeyboardButton(text="ТРК Небо", callback_data="sky-1"),
    types.InlineKeyboardButton(text="ТРЦ Индиго", callback_data="indigo-1"),
    types.InlineKeyboardButton(text="<< Назад", callback_data="prgmng"),
    width=1
)

aboutUs = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text="Первый 🚀", url="https://vk.com/misterigortrif"),
    types.InlineKeyboardButton(text="Второй ✅", url="https://vk.com/1oleshik1"),
    types.InlineKeyboardButton(text="<< Назад", callback_data="prgmng"),
    width=1
)

changeDayKb = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text='Сегодня ⬇️', callback_data="today"),
    types.InlineKeyboardButton(text='Завтра ⬆️', callback_data="tommorow"),
    types.InlineKeyboardButton(text='<< Назад', callback_data="prgmng"),
    width=1
)


kb = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text='<< Назад', callback_data="changekino"),
    width=1
)

kb_prev = InlineKeyboardBuilder().row(
    types.InlineKeyboardButton(text='<< Назад', callback_data="tommorow"),
    width=1
)


def afishaCinema(a):
    if a == "rio":
        return a, "Выбрано ТРЦ РИО 📖 \n", kb
    if a == "bur":
        return a, "Выбран киноткатр Буревестник 📖 \n", kb
    if a == "goldmile":
        return a, "Выбрана Золотая Миля 📖 \n", kb
    if a == "sky":
        return a, "Выбран ТРК Небо 📖 \n", kb
    if a == "indigo":
        return a, "Выбран ТРЦ Индиго 📖 \n", kb

    if a == "rio-1":
        return a, "Выбрано ТРЦ РИО 📖 \n", kb_prev
    if a == "bur-1":
        return a, "Выбран киноткатр Буревестник 📖 \n", kb_prev
    if a == "goldmile-1":
        return a, "Выбрана Золотая Миля 📖 \n", kb_prev
    if a == "sky-1":
        return a, "Выбран ТРК Небо 📖 \n", kb_prev
    if a == "indigo-1":
        return a, "Выбран ТРЦ Индиго 📖 \n", kb_prev