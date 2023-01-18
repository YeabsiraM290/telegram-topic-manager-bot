#TODO: ERROR HANDLING !!!

from telegram import Message
from telegram.ext import ContextTypes, ExtBot
from custom_messages import aprrove_decline_markup
from telegram_actions import (
    send_message,
    send_message_to_topic,
    reply_to_message,
    forward_message,
    delete_message,
)

# Bot actions


# reply to new message
async def reply_to_new_message(message: Message, username: str, text: str) -> int:

    message_body = "Hello @" + username + "\n" + text
    message_id = await reply_to_message(original_message=message, text=message_body)
    return message_id


# send new message to admin with accept/decline button
async def send_new_message_to_admin(
    admin_id: int,
    chat_id: int,
    message_thread_id: int,
    text: str,
    username: str,
    bot: ExtBot,
) -> None:

    message = "From: @" + username + "\n" + text
    markup = aprrove_decline_markup(
        chat_id=chat_id, message_thread_id=message_thread_id
    )

    await send_message(
        chat_id=admin_id,
        text=message,
        markup=markup,
        bot=bot,
    )


# delete message from group
async def delete_new_message(chat_id: int, message_id: int, bot: ExtBot) -> None:
    await delete_message(chat_id=chat_id, message_id=message_id, bot=bot)


# deletes bot greeting message
async def delete_bot_greeting_message(context: ContextTypes.DEFAULT_TYPE) -> None:

    job = context.job
    chat_id = job.data["chat_id"]
    message_id = job.data["message_id"]

    await delete_message(chat_id=chat_id, message_id=message_id, bot=context.bot)


# delete delcined message from admin
async def delete_message_from_admin(
    admin_id: int, message_id: int, bot: ExtBot
) -> None:
    await delete_message(chat_id=admin_id, message_id=message_id, bot=bot)


# post message to group
async def post_approved_message_to_group(
    chat_id: int, message_thread_id: int, text: str, bot: ExtBot
) -> None:

    if message_thread_id:

        await send_message_to_topic(
            chat_id=chat_id,
            message_threade_id=message_thread_id,
            text=text,
            bot=bot,
            markup=None,
        )

    else:
        await send_message(
            chat_id=chat_id,
            text=text,
            bot=bot,
            markup=None
        )


# forward new message to admin
async def forward_to_admin(
    from_chat_id: int, message_id: int, admin_id: int, bot: ExtBot
) -> None:
    await bot.forwardMessage(
        chat_id=admin_id,
        from_chat_id=from_chat_id,
        message_id=message_id,
    )
