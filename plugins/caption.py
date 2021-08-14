import os
from config import Config

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait

CAPTION=Config.CAPTION

@Client.on_message(filters.channel & filters.media)
async def caption(client):
    button_name = os.environ.get('BUTTON_NAME')
    button_url = os.environ.get('BUTTON_URL')
    FILE_NAME = bool(os.environ.get('FILE_NAME', False))
    
    if button_name and not FILE_NAME:
        await message.edit(CAPTION,
              reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(button_name, url=f"{button_url}")]
            ]
                                           )
                      
                         )
