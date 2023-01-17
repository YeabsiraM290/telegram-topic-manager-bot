# import urllib.request as request
# from urllib.error import HTTPError
# from http.client import HTTPResponse
# from typing import Dict, List, Union
# import json
# from datetime import datetime
# import signal
# import os

# signal.signal(signal.SIGINT, signal.SIG_DFL)


# class TelegramEcho:
#     def __init__(self, TG_KEY: str):
#         self.TG_URL = "https://api.telegram.org/bot{key}/{method}"
#         self.TG_KEY = TG_KEY

#         self.__last = None
#         self.__last_time = None
#         pass

#     def run(self):
#         """
#         method to handle the incoming message and the send echo message to the user
#         """
#         while True:
#             try:
#                 # getting the incoming data
#                 incoming = self.__handle_incoming()

#                 # checking if incoming message_id is same as of last, then skip
#                 if self.__last == incoming["message"]["message_id"]:
#                     continue
#                 else:
#                     self.__last = incoming["message"]["message_id"]

#                 # adding more validation to prevent messaging the last message whenever the polling starts
#                 if not self.__last_time:
#                     self.__last_time = incoming["message"]["date"]
#                     continue
#                 elif self.__last_time < incoming["message"]["date"]:
#                     self.__last_time = incoming["message"]["date"]
#                 else:
#                     continue

#                 # finally printing the incoming message
#                 self.__print_incoming(incoming)

#                 # now sending the echo message
#                 outgoing = self.__handle_outgoing(
#                     incoming["message"]["chat"]["id"],
#                     incoming["message"]["from"].get("username", ""),
#                     incoming["message"]["text"],
#                 )

#                 # finally printing the outgoing message
#                 self.__print_outgoing(outgoing)

#                 pass
#             except (HTTPError, IndexError):
#                 continue
#             pass
#         pass

#     def __handle_incoming(self) -> Dict[str, Union[int, str]]:
#         """
#         method fetch the recent messages
#         """

#         # getting all messages
#         getUpdates = request.urlopen(
#             self.TG_URL.format(key=self.TG_KEY, method="getUpdates")
#         )

#         # parsing results
#         results: List[Dict[str, Union[int, str]]] = json.loads(
#             getUpdates.read().decode()
#         )["result"]

#         # getting the last error
#         return results[-1]

#     def __print_incoming(self, incoming: Dict[str, Union[int, str]]):
#         """
#         method to print the incoming message on console
#         """
#         print(
#             "[<<<] Message Recieved on %s"
#             % datetime.fromtimestamp(incoming["message"]["date"]).strftime(
#                 "%Y-%m-%d %H:%M:%S"
#             )
#         )
#         print("\tText: %s" % incoming["message"]["text"])
#         print(
#             "\tFrom: %s" % incoming["message"]["from"].get("first_name", "")
#             + " "
#             + incoming["message"]["from"].get("last_name", "")
#         )
#         print("\t user name " + incoming["message"]["from"].get("username", ""))
#         print("\tMessage ID: %d" % incoming["message"]["message_id"])
#         print("-" * os.get_terminal_size().columns)
#         pass

#     def __handle_outgoing(
#         self, chat_id: int, username: str, message_txt: str
#     ) -> Dict[str, Union[int, str]]:
#         """
#         method to send the echo message to the same chat
#         """

#         # making the post data
#         _data: Dict[str, Union[int, str]] = {
#             "chat_id": chat_id,
#             "text": "From @"
#             + username
#             + '\n\nHe sent me "{MESSAGE_TEXT}"'.format(MESSAGE_TEXT=message_txt)
#             + "\n\nApprove \t Decline",
#         }

#         _data2: Dict[str, Union[int, str]] = {
#             "chat_id": "-1001818218873",
#             "text": "From @"
#             + username
#             + '\n"{MESSAGE_TEXT}"'.format(MESSAGE_TEXT=message_txt),
#         }

#         # creating the request
#         _request: request.Request = request.Request(
#             self.TG_URL.format(key=self.TG_KEY, method="sendMessage"),
#             data=json.dumps(_data).encode("utf8"),
#             headers={"Content-Type": "application/json"},
#         )

#         _request2: request.Request = request.Request(
#             self.TG_URL.format(key=self.TG_KEY, method="sendMessage"),
#             data=json.dumps(_data2).encode("utf8"),
#             headers={"Content-Type": "application/json"},
#         )

#         # sending HTTP request, for sending message to the user
#         sendMessage: HTTPResponse = request.urlopen(_request)
#         result: Dict[str, Union[int, str]] = json.loads(sendMessage.read().decode())[
#             "result"
#         ]
#         sendMessage2: HTTPResponse = request.urlopen(_request2)

#         return result

#     def __print_outgoing(self, outgoing):
#         """
#         method to print outgoing data on the console
#         """
#         print(
#             "[>>>] Message Send on %s"
#             % datetime.fromtimestamp(outgoing["date"]).strftime("%Y-%m-%d %H:%M:%S")
#         )
#         print("\tText: %s" % outgoing["text"])
#         print("\tFrom: %s" % outgoing["from"]["first_name"])
#         print("\tMessage ID: %d" % outgoing["message_id"])
#         print("-" * os.get_terminal_size().columns)
#         pass

#     pass


# if __name__ == "__main__":
#     tg = TelegramEcho("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A")
#     tg.run()

# # from aiogram import Bot, Dispatcher, executor, types
# # from aiogram.types import (
# #     ReplyKeyboardMarkup,
# #     KeyboardButton,
# # )  # for reply keyboard (sends message)

# # from time import sleep


# # bot = Bot(token="5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A")
# # dp = Dispatcher(bot)

# # answers = []  # store the answers they have given


# # ### add stuff here


# # # this is the last line
# # executor.start_polling(dp)

# # # language selection
# # lang1 = KeyboardButton("English 👍")
# # lang2 = KeyboardButton("українська 💪")
# # lang3 = KeyboardButton("Other language 🤝")
# # lang_kb = (
# #     ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# #     .add(lang1)
# #     .add(lang2)
# #     .add(lang3)
# # )


# # # sends welcome message after start
# # @dp.message_handler(commands=["start"])
# # async def welcome(message: types.Message):
# #     await message.answer(
# #         "Hello! Please select your language.\nивт! Виберіть мову.",
# #         reply_markup=lang_kb,
# #     )


# # # sends help message
# # @dp.message_handler(commands=["help"])
# # async def help(message: types.Message):
# #     await message.answer(
# #         "We are a team of LGBT organizations from across Europe. We help you get into safety, provide support and answer any questions you may have. Press /start to get started. \nМи — команда ЛГБТ-організацій з усієї Європи. Ми допомагаємо вам увійти в безпеку, надаємо підтримку та відповідаємо на будь-які ваші запитання. Натисніть /start, щоб почати."
# #     )

# # # options selection: English
# # en_options1 = KeyboardButton('Psychological support 🧠')
# # en_options2 = KeyboardButton('Supplies: food, medicine, hormones, ... 🍇')
# # en_options3 = KeyboardButton('Border crossing 🏇')
# # en_options4 = KeyboardButton('Other help 📚')
# # en_options_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(en_options1).add(en_options2).add(en_options3).add(en_options4)

# # #### selecting what you need
# # @dp.message_handler(regexp='English 👍')
# # async def english(message: types.Message):
# #     answers.append(message.text)
# #     await message.answer('What do you need?', reply_markup = en_options_kb)

# # if __name__ == '__main__':
# #     executor.start_polling(dp, skip_updates=True)


# """
# This is a echo bot.
# It echoes any incoming text messages.
# """

# # import logging

# # from aiogram import Bot, Dispatcher, executor, types

# # API_TOKEN = '5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A'

# # # Configure logging
# # logging.basicConfig(level=logging.INFO)

# # # Initialize bot and dispatcher
# # bot = Bot(token=API_TOKEN)
# # dp = Dispatcher(bot)


# # @dp.message_handler(commands=['start', 'help'])
# # async def send_welcome(message: types.Message):
# #     """
# #     This handler will be called when user sends `/start` or `/help` command
# #     """
# #     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# # @dp.message_handler()
# # async def echo(message: types.Message):
# #     # old style:
# #     # await bot.send_message(message.chat.id, message.text)

# #     await message.answer(message.text)


# # if __name__ == '__main__':
# #     executor.start_polling(dp, skip_updates=True)


# # import telebot
# # from telebot import types

# # bot = telebot.TeleBot("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A")


# # @bot.message_handler(commands=["alter_visibility"])
# # def alter_visibility(message):
# #     chat_id = message.chat.id
# #     message_id = message.message_id

# #     markup = withdraw()
# #     bot.edit_message_reply_markup(chat_id, message_id, reply_markup=markup)

# #     # get roles list
# #     permissions = {"admin": ["view", "edit"], "editor": ["view"]}

# #     # check with permissions
# #     if message.text in permissions:
# #         bot.restrict_chat_member(
# #             chat_id, message.from_user.id, permissions[message.text]
# #         )


# # def withdraw():

# #     markup = types.InlineKeyboardMarkup()

# #     item1 = types.InlineKeyboardButton("Admin", callback_data="Admin")
# #     item2 = types.InlineKeyboardButton("Editor", callback_data="Editor")

# #     # add buttons to markup
# #     markup.add(item1, item2)

# #     return markup


# # bot.infinity_polling()

#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# import logging

# from telegram import __version__ as TG_VER

# try:
#     from telegram import __version_info__
# except ImportError:
#     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#     )
# from telegram import ForceReply, Update
# from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# # Enable logging
# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )
# logger = logging.getLogger(__name__)


# # Define a few command handlers. These usually take the two arguments update and
# # context.
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /start is issued."""
#     user = update.effective_user
#     await update.message.edit
#     await update.message.reply_html(
#         rf"Hi {user.mention_html()}!",
#         reply_markup=ForceReply(selective=True),
#     )


# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Send a message when the command /help is issued."""
#     await update.message.reply_text("Help!")


# async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Echo the user message."""
#     await update.message.reply_text(update.message.text)


# def main() -> None:
#     """Start the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A").build()

#     # on different commands - answer in Telegram
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("help", help_command))

#     # on non command i.e message - echo the message on Telegram
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

#     # Run the bot until the user presses Ctrl-C
#     application.run_polling()


# if __name__ == "__main__":
#     main()

#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to handle '(my_)chat_member' updates.
Greets new users & keeps track of which chats the bot is in.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# import logging
# from typing import Optional, Tuple

# from telegram import __version__ as TG_VER

# try:
#     from telegram import __version_info__
# except ImportError:
#     __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# if __version_info__ < (20, 0, 0, "alpha", 1):
#     raise RuntimeError(
#         f"This example is not compatible with your current PTB version {TG_VER}. To view the "
#         f"{TG_VER} version of this example, "
#         f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
#     )
# from telegram import Chat, ChatMember, ChatMemberUpdated, Update
# from telegram.constants import ParseMode
# from telegram.ext import Application, ChatMemberHandler, CommandHandler, ContextTypes

# # Enable logging

# logging.basicConfig(
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
# )

# logger = logging.getLogger(__name__)


# def extract_status_change(chat_member_update: ChatMemberUpdated) -> Optional[Tuple[bool, bool]]:
#     """Takes a ChatMemberUpdated instance and extracts whether the 'old_chat_member' was a member
#     of the chat and whether the 'new_chat_member' is a member of the chat. Returns None, if
#     the status didn't change.
#     """
#     status_change = chat_member_update.difference().get("status")
#     old_is_member, new_is_member = chat_member_update.difference().get("is_member", (None, None))

#     if status_change is None:
#         return None

#     old_status, new_status = status_change
#     was_member = old_status in [
#         ChatMember.MEMBER,
#         ChatMember.OWNER,
#         ChatMember.ADMINISTRATOR,
#     ] or (old_status == ChatMember.RESTRICTED and old_is_member is True)
#     is_member = new_status in [
#         ChatMember.MEMBER,
#         ChatMember.OWNER,
#         ChatMember.ADMINISTRATOR,
#     ] or (new_status == ChatMember.RESTRICTED and new_is_member is True)

#     return was_member, is_member


# async def track_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Tracks the chats the bot is in."""
#     result = extract_status_change(update.my_chat_member)
#     if result is None:
#         return
#     was_member, is_member = result

#     # Let's check who is responsible for the change
#     cause_name = update.effective_user.full_name

#     # Handle chat types differently:
#     chat = update.effective_chat
#     if chat.type == Chat.PRIVATE:
#         if not was_member and is_member:
#             logger.info("%s started the bot", cause_name)
#             context.bot_data.setdefault("user_ids", set()).add(chat.id)
#         elif was_member and not is_member:
#             logger.info("%s blocked the bot", cause_name)
#             context.bot_data.setdefault("user_ids", set()).discard(chat.id)
#     elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
#         if not was_member and is_member:
#             logger.info("%s added the bot to the group %s", cause_name, chat.title)
#             context.bot_data.setdefault("group_ids", set()).add(chat.id)
#         elif was_member and not is_member:
#             logger.info("%s removed the bot from the group %s", cause_name, chat.title)
#             context.bot_data.setdefault("group_ids", set()).discard(chat.id)
#     else:
#         if not was_member and is_member:
#             logger.info("%s added the bot to the channel %s", cause_name, chat.title)
#             context.bot_data.setdefault("channel_ids", set()).add(chat.id)
#         elif was_member and not is_member:
#             logger.info("%s removed the bot from the channel %s", cause_name, chat.title)
#             context.bot_data.setdefault("channel_ids", set()).discard(chat.id)


# async def show_chats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Shows which chats the bot is in"""
#     user_ids = ", ".join(str(uid) for uid in context.bot_data.setdefault("user_ids", set()))
#     group_ids = ", ".join(str(gid) for gid in context.bot_data.setdefault("group_ids", set()))
#     channel_ids = ", ".join(str(cid) for cid in context.bot_data.setdefault("channel_ids", set()))
#     text = (
#         f"@{context.bot.username} is currently in a conversation with the user IDs {user_ids}."
#         f" Moreover it is a member of the groups with IDs {group_ids} "
#         f"and administrator in the channels with IDs {channel_ids}."
#     )
#     await update.effective_message.reply_text(text)


# async def greet_chat_members(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     """Greets new users in chats and announces when someone leaves"""
#     result = extract_status_change(update.chat_member)
#     if result is None:
#         return

#     was_member, is_member = result
#     cause_name = update.chat_member.from_user.mention_html()
#     member_name = update.chat_member.new_chat_member.user.mention_html()

#     if not was_member and is_member:
#         await update.effective_chat.send_message(
#             f"{member_name} was added by {cause_name}. Welcome!",
#             parse_mode=ParseMode.HTML,
#         )
#     elif was_member and not is_member:
#         await update.effective_chat.send_message(
#             f"{member_name} is no longer with us. Thanks a lot, {cause_name} ...",
#             parse_mode=ParseMode.HTML,
#         )


# def main() -> None:
#     """Start the bot."""
#     # Create the Application and pass it your bot's token.
#     application = Application.builder().token("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A").build()

#     # Keep track of which chats the bot is in
#     application.add_handler(ChatMemberHandler(track_chats, ChatMemberHandler.MY_CHAT_MEMBER))
#     application.add_handler(CommandHandler("show_chats", show_chats))

#     # Handle members joining/leaving chats.
#     application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))

#     # Run the bot until the user presses Ctrl-C
#     # We pass 'allowed_updates' handle *all* updates including `chat_member` updates
#     # To reset this, simply pass `allowed_updates=[]`
#     application.run_polling(allowed_updates=Update.ALL_TYPES)


# if __name__ == "__main__":
#     main()

#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
Basic example for a bot that uses inline keyboards. For an in-depth explanation, check out
 https://github.com/python-telegram-bot/python-telegram-bot/wiki/InlineKeyboard-Example.
"""
import logging
from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data="1"),
            InlineKeyboardButton("Option 2", callback_data="2"),
        ],
        [InlineKeyboardButton("Option 3", callback_data="3")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Please choose category:", reply_markup=reply_markup
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with three inline buttons attached."""

    keyboard = [
        [
            InlineKeyboardButton(
                "Category 1",
                callback_data="message_id:"
                + str(update.message.message_id)
                + ":chat_id:"
                + str(update.message.chat_id),
            ),
            InlineKeyboardButton(
                "Category 2",
                callback_data="message_id:"
                + str(update.message.message_id)
                + ":chat_id:"
                + str(update.message.chat_id),
            ),
        ],
        [
            InlineKeyboardButton(
                "Category 3",
                callback_data="message_id:"
                + str(update.message.message_id)
                + ":chat_id:"
                + str(update.message.chat_id),
            ),
            InlineKeyboardButton(
                "Category 4",
                callback_data="message_id:"
                + str(update.message.message_id)
                + ":chat_id:"
                + str(update.message.chat_id),
            ),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if not update.message["is_topic_message"]:
        await update.message.reply_text(
            "Please choose Message Category:", reply_markup=reply_markup
        )

    # await context.bot.delete_message(
    #     chat_id=update.message.chat_id,
    #     message_id=update.message.message_id,
    # )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    # if type(query.data) == str:
    #     await query.edit_message_text(text=f"Selected option: {query.data}")

    m_id = query.data.split(":")[1]
    c_id = query.data.split(":")[3]

    await context.bot.delete_message(
        chat_id=c_id,
        message_id=m_id,
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = (
        Application.builder()
        .token("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A")
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
