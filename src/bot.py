import time

from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message

from src import add_watermark

TOKEN = 'TOKEN'
router = Router()


@router.message(Command(commands=['start']))
async def handle_start(m: Message):
    await m.reply('Accepted')


@router.message
async def handle_photo(m: Message, bot: Bot):
    if m.text == '':
        await m.answer('Caption is required')
        return
    ts = int(time.time())
    destination = f'downloads/photo_{ts}.png'
    output_path = f'generated/photo_{ts}.png'
    await bot.download(file=m.photo[-1], destination=destination)
    add_watermark(destination, m.text, output_path)
    await m.answer_photo(output_path)


async def main():
    dp = Dispatcher()
    bot = Bot(TOKEN)
    dp.include_router(router)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
