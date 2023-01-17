from email import message
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
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, Message

from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
    ExtBot,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

new_message_reply_text = (
    "Please wait a moment, your message is being reviewd by an admin"
)
admin_id = 555486710
delete_pending_messages = []
topics_to_monitor = [229]


# Handlers

# called when new message is sent, forward message to admin and reply to the message
async def new_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:

    chat_id = update.message.chat_id
    message_id = update.message.message_id
    username = update.message.from_user.username
    text = update.message.text
    markup = aprrove_decline_markup(chat_id=chat_id, message_thread_id=None)

    # await forward_to_admin(
    #     from_chat_id=chat_id, message_id=message_id, admin_id=admin_id, bot=context.bot
    # )

    is_message_from_topic = update.message["is_topic_message"]
    message_topic = 0

    if is_message_from_topic:

        message_topic = update.message.message_thread_id
        markup = aprrove_decline_markup(
            chat_id=chat_id, message_thread_id=message_topic
        )

    if message_topic in topics_to_monitor:

        await send_markup_message_to_admin(
            admin_id=admin_id,
            text=text,
            username=username,
            bot=context.bot,
            markup=markup,
        )

        bot_message_id = await reply_to_message(
            message=update.message, username=username, text=new_message_reply_text
        )

        await delete_message(chat_id=chat_id, message_id=message_id, bot=context.bot)

        context.job_queue.run_once(
            schedule_bot_message,
            10,
            data={"message_id": bot_message_id},
        )



async def accept_decline_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:

    button_selected_data = update.callback_query.data
    message_id = update.callback_query.message.message_id
    text = update.callback_query.message.text

    if button_selected_data == "0":
        await delete_message_from_admin(
            chat_id=admin_id, message_id=message_id, bot=context.bot
        )

    else:
        message_threade_id = button_selected_data.split(":")[1]

        if message_threade_id != "None":
            await post_message_to_group(
                chat_id=int(button_selected_data.split(":")[0]),
                message_threade_id=message_threade_id,
                text=text,
                bot=context.bot,
            )
        else:
            await post_message_to_group(
                chat_id=int(button_selected_data.split(":")[0]),
                text=text,
                bot=context.bot,
            )


# Helpers

# reply to new message
async def reply_to_message(message: Message, username: str, text: str) -> int:
    bot_message = await message.reply_text("Hello @" + username + "\n" + text)
    return bot_message.message_id


# send markup_message to admin
async def send_markup_message_to_admin(
    admin_id: int, text: str, username: str, bot: ExtBot, markup: InlineKeyboardMarkup
) -> None:
    message = "From: @" + username + "\n" + text

    await bot.send_message(chat_id=admin_id, text=message, reply_markup=markup)


def aprrove_decline_markup(
    chat_id: int, message_thread_id: int
) -> InlineKeyboardMarkup:

    keyboard = [
        [
            InlineKeyboardButton(
                "Accept", callback_data=str(chat_id) + ":" + str(message_thread_id)
            ),
            InlineKeyboardButton("Decline", callback_data="0"),
        ]
    ]

    return InlineKeyboardMarkup(keyboard)


# forward new message to admin
async def forward_to_admin(
    from_chat_id: int, message_id: int, admin_id: int, bot: ExtBot
) -> None:
    await bot.forwardMessage(
        chat_id=admin_id,
        from_chat_id=from_chat_id,
        message_id=message_id,
    )


# schedule bot message deletion
async def schedule_bot_message(context: ContextTypes.DEFAULT_TYPE) -> None:

    job = context.job
    chat_id = job.chat_id
    message_id = job.data["message_id"]
    await context.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )


# delte message from group
async def delete_message(chat_id: int, message_id: int, bot: ExtBot) -> None:
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id,
    )


# post message to group
async def post_message_to_group(
    chat_id: int, message_threade_id: int, text: str, bot: ExtBot
) -> None:

    if message_threade_id:
        await bot.send_message(
            chat_id=chat_id, text=text, message_thread_id=message_threade_id
        )

    else:
        await bot.send_message(chat_id=chat_id, text=text)


# delete delcined message from admin
async def delete_message_from_admin(chat_id: int, message_id: int, bot: ExtBot) -> None:
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


def main() -> None:

    application = (
        Application.builder()
        .token("5639106247:AAHkgBicbi_-5uR-U3ot9L2poNg4LrEjV9A")
        .build()
    )

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, new_message_handler)
    )
    application.add_handler(CallbackQueryHandler(accept_decline_handler))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
