from utils import *
from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

# URL of the image to be used
IMAGE_URL = "https://telegra.ph/file/c05c0889dcd0c1054de3f.jpg"

@Client.on_message(filters.command("start") & ~filters.channel)
async def start(bot, message):
    await add_user(message.from_user.id, message.from_user.first_name)
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=script.START.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕', 
                        url='https://t.me/MS_Post_Finder_Bot?startgroup=true'
                    )
                ],
                [
                    InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help"),
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about")
                ]
            ]
        )
    )

@Client.on_message(filters.command("help"))
async def help(bot, message):
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=script.HELP,
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("about"))
async def about(bot, message):
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=script.ABOUT.format((await bot.get_me()).mention),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("stats"))
async def stats(bot, message):
    g_count, g_list = await get_groups()
    u_count, u_list = await get_users()
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=script.STATS.format(u_count, g_count)
    )

@Client.on_message(filters.command("id"))
async def id(bot, message):
    text = f"Current Chat ID: `{message.chat.id}`\n"
    if message.from_user:
       text += f"Your ID: `{message.from_user.id}`\n"
    if message.reply_to_message:
       if message.reply_to_message.from_user:
          text += f"Replied User ID: `{message.reply_to_message.from_user.id}`\n"
       if message.reply_to_message.forward_from:
          text += f"Replied Message Forward from User ID: `{message.reply_to_message.forward_from.id}`\n"
       if message.reply_to_message.forward_from_chat:
          text += f"Replied Message Forward from Chat ID: `{message.reply_to_message.forward_from_chat.id}`\n"
    await message.reply_photo(
        photo=IMAGE_URL,
        caption=text
    )

@Client.on_callback_query(filters.regex(r"^misc"))
async def misc(bot, update):
    data = update.data.split("_")[-1]
    if data == "home":
       await update.message.edit_media(
           media=InputMediaPhoto(
               media=IMAGE_URL,
               caption=script.START.format(update.from_user.mention)
           ),
           reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("ʜᴇʟᴘ", callback_data="misc_help"),
                       InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="misc_about")
                   ]
               ]
           ),
           disable_web_page_preview=True
       ) 
    elif data == "help":
       await update.message.edit_media(
           media=InputMediaPhoto(
               media=IMAGE_URL,
               caption=script.HELP
           ),
           reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton("⬅️ Back", callback_data="misc_home")
                   ]
               ]
           ),
           disable_web_page_preview=True
       ) 
    elif data == "about":
        await update.message.edit_media(
            media=InputMediaPhoto(
                media=IMAGE_URL,
                caption=script.ABOUT.format((await bot.get_me()).mention)
            ),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⬅️ Back", callback_data="misc_home")
                    ]
                ]
            ),
            disable_web_page_preview=True
        ) 
