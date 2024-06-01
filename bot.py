import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from handlers.user_private import user_private_router
from common.botCmdsList import private

# Точка входа

# В дальнейшем для правильной работы на сервере!
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())
#-----------------------------------------------



bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp.include_router(user_private_router)

# Допустимые к обработке события --------------
ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']
#----------------------------------------------

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())