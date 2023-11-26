import sys
import json
import logging
import asyncio
import keyboards

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart


dp = Dispatcher()
MAPPING = {
    1: keyboards.first_task,
    2: keyboards.second_task,
    3: keyboards.third_task,
    4: keyboards.fourth_task,
    5: keyboards.fifth_task,
    6: keyboards.sixth_task,
    7: keyboards.seventh_task,
    8: keyboards.eighth_task,
    9: keyboards.ninth_task,
    10: keyboards.tenth_task,
    11: keyboards.eleventh_task,
    12: keyboards.twelfth_task,
    13: keyboards.thirteenth_task,
    14: keyboards.fourteenth_task,
    15: keyboards.fifteenth_task,
}

REPLIES: dict[str, dict[str, str]] = json.load(open("replies.json", "r+", encoding="UTF-8"))


@dp.message(CommandStart())
async def beginning(message: types.Message):
    await message.answer("Выберите одну категорию заданий из предложенных", reply_markup=keyboards.initial_keyboard())


@dp.callback_query(F.data.startswith("task_"))
async def on_task_callback_query(callback: types.CallbackQuery):
    task_id = int(callback.data.replace("task_", ""))
    keyboard = MAPPING[task_id]()
    await callback.message.edit_text("Выберите один вариант из предложенных", reply_markup=keyboard)


@dp.callback_query(F.data.startswith("test_"))
async def on_test_callback_query(callback: types.CallbackQuery):
    task_id = callback.data.split("_")[1]
    variation_id = callback.data.split("_")[3]
    reply = REPLIES[task_id][variation_id]

    if reply["image"] != "None":
        await callback.message.delete()
        await callback.bot.send_photo(
            parse_mode="HTML",
            caption=reply["text"],
            chat_id=callback.message.chat.id,
            photo=types.FSInputFile(reply["image"]),
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Назад", callback_data=f"return_back_{task_id}_false")]])
        )
    else:
        await callback.message.edit_text(
            text=reply["text"],
            parse_mode="HTML",
            reply_markup=types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text="Назад", callback_data=f"return_back_{task_id}_true")]])
        )


@dp.callback_query(F.data.startswith("return_back"))
async def on_return_back_callback_query(callback: types.CallbackQuery):
    task_id = int(callback.data.split("_")[2])
    reply = callback.data.split("_")[3]

    keyboard = MAPPING[task_id]()
    if reply == "true":
        await callback.message.edit_text("Выберите один вариант из предложенных", reply_markup=keyboard)
    else:
        await callback.message.delete()
        await callback.bot.send_message(
            chat_id=callback.message.chat.id,
            text="Выберите один вариант из предложенных",
            reply_markup=keyboard
        )


async def main():
    with open("config.json", "r+", encoding="UTF-8") as file:
        config = json.load(file)
        API_TOKEN = config["token"]

    bot = Bot(token=API_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
