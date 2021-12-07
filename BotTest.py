from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "5092093907:AAFrUzQcx_K3OLV0Xp2u3dN6OwqGxLWT9_4"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    markup = InlineKeyboardMarkup()
    but_1 = InlineKeyboardButton("Как дела?", callback_data="but_1")
    but_2 = InlineKeyboardButton("Как настроение?", callback_data="but_2")
    markup.add(but_1, but_2)

    await bot.send_message(message.chat.id, "Привет!", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "but_1")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Дела нормально")

@dp.callback_query_handler(lambda c: c.data == "but_2")
async def button_reaction(call: types.callback_query):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, "Настроение нормально")


@dp.message_handler(content_types=['text'])
async def text_answer(message: types.Message):
    if message.text.lower() == "стоп":
        await message.reply("Пока, пока")


executor.start_polling(dp)

