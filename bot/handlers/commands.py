from aiogram import types

from dispatcher import dispatcher, bot
from handlers import keyboards
#from handlers import functions

from time import time
@dispatcher.message_handler(commands=["start"], commands_prefix="/")
async def start_command(message: types.Message):
    #if message.chat.type =="private":
        await message.bot.send_message(chat_id=message.chat.id,
        text = "start text", parse_mode="HTML")
    #else: return


@dispatcher.message_handler(commands= ["mute"], commands_prefix="/")
async def mute(message: types.Message):
    if message.reply_to_message is not None:
        await message.reply_to_message.reply(text=f"Выдать мут пользователю id: {message.reply_to_message.from_user.id}?", reply_markup=keyboards.mute_keyboard())
    else:
        await message.reply("Нужен реплай на сообщение!")


@dispatcher.message_handler(commands= ["unmute"], commands_prefix="/")
async def mute(message: types.Message):
    if message.reply_to_message is not None:
        user = await message.bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
        if user.status == "administrator" or user.status == "creator":
            await message.bot.restrict_chat_member(chat_id = message.chat.id, user_id=message.reply_to_message.from_user.id, 
            permissions=types.ChatPermissions( can_send_messages = True, can_send_games = True, 
            can_send_polls = True, can_use_inline_bots = True, can_send_media_messages = True, 
            can_invite_users = True, can_add_web_page_previews = True, can_send_stickers = True, 
            can_send_animations = True) )
        await message.reply("С пользователя {message.reply_to_message.from_user.id} сняты ограничения!")    
    else:
        await message.reply("Нужен реплай на сообщение!")


@dispatcher.message_handler(commands=["fao"], commands_prefix="/")
async def fao_command(message: types.Message):
    if message.chat.type !="private":
        return
    await message.bot.send_message(chat_id=message.chat.id, text="text", reply_markup=keyboards.fao_keyboard())



@dispatcher.message_handler(content_types=[types.ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message: types.Message):
    new_member = message.new_chat_members[0]
    print(new_member)
    await message.reply(f"Добро пожаловать, {new_member.mention}.\nЭто чат для помощи и взаимообучения в программировании!", reply_markup=keyboards.welcome_keyboard())
    await bot.restrict_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)