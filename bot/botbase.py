from aiogram import Bot, Dispatcher, types, executor

bot = Bot(token= "6098589211:AAH3ACx1eBKC8cdOhatg8LrG0uqnrDwFbfw")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text = message.text)

if __name__ == "__main__":
    executor.start_polling(dp)
