import asyncio
import logging
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message,KeyboardButton,ReplyKeyboardMarkup
from deep_translator import GoogleTranslator
from aiogram.filters import Command
from dotenv import load_dotenv
import os
load_dotenv()
API_TOKEN=os.getenv("API_TOKEN")
bot=Bot(token=API_TOKEN)
dp=Dispatcher()
@dp.message(Command('start'))
async def start_cmd(message:Message):
    await message.reply(f"""
 Assalomu alaykum {message.from_user.full_name}
 Translator botimizga xush kelibsiz 
 O'zbekchha so'z yozing inglizchasini chiqaraman
 """)
@dp.message(F.text)
async def translator_bot(message:Message):
    try:
        text=message.text
        translator=GoogleTranslator(source="auto",target="ru").translate(text)
        await message.reply(f"{text} so'zi inglizchada -> {translator} deyiladi")
    except Exception as error:
        await message.answer(f"Botda xatolik {error}")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())