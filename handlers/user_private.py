from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery

from keyboards import reply
from common.parsing import playbill

user_private_router = Router()


@user_private_router.message(CommandStart())
async def startCommand(message: types.Message):
    await message.answer(
        text=f"Привет ,{message.from_user.first_name}, я - виртуальный помощник (🤖)! Помогу узнать актуальную афишу для некоторых кинотеатров Нижегородской области.",
        reply_markup=reply.startKb.as_markup())


@user_private_router.callback_query(lambda query: query.data == "prgmng")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text("Выберите действие 🤔", reply_markup=reply.afterStart.as_markup())


@user_private_router.callback_query(lambda querry: querry.data == "aboutus")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text="Программысты 💻", reply_markup=reply.aboutUs.as_markup())


@user_private_router.callback_query(lambda querry: querry.data == "changeday")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text="Выберите день  🔀", reply_markup=reply.changeDayKb.as_markup())

@user_private_router.callback_query(lambda querry: querry.data == "changekino")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text="Выбирайте с умом 🧠...: ", reply_markup=reply.changeCinema_tonight.as_markup())


@user_private_router.callback_query(lambda querry: querry.data == "tommorow")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text="Выбирайте с умом 🧠...: ", reply_markup=reply.changeCinema_tommorow.as_markup())


@user_private_router.callback_query(lambda querry: querry.data == "today")
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text="Выбирайте с умом 🧠...: ", reply_markup=reply.changeCinema_tonight.as_markup())


@user_private_router.callback_query(lambda querry: querry.data)
async def my_callback_foo(query: CallbackQuery):
    await query.message.delete_reply_markup()
    await query.message.edit_text(text=reply.afishaCinema(query.data)[1] + "\n" + playbill(reply.afishaCinema(query.data)[0]), reply_markup=reply.afishaCinema(query.data)[2].as_markup())
