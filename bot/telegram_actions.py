from telegram import InlineKeyboardMarkup, Message
from telegram.ext import ExtBot
from helpers import print_error

# TODO: CHANGE TO CLASS !!!

# send telegram message
async def send_message(
    chat_id: int, text: str, bot: ExtBot, markup: InlineKeyboardMarkup
) -> None:

    """
    chat_id = message reciver id (group, person)
    text = message content to be sent
    bot = bot instance
    markup = markup to be sent (buttons,....), can be None if not any
    """

    try:
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=markup)

    except Exception as error:
        print_error(
            error_source=" telegram_actions.py, send_message() )", error_message=error
        )


# post telegram message to a topic
async def send_message_to_topic(
    chat_id: int,
    message_threade_id: int,
    text: str,
    markup: InlineKeyboardMarkup,
    bot: ExtBot,
) -> None:

    """
    chat_id = group id
    message_threade_id = topic id
    text = message content to be sent
    bot = bot instance
    markup = markup to be sent (buttons,....), can be None if not any
    """

    try:
        await bot.send_message(
            chat_id=chat_id,
            text=text,
            message_thread_id=message_threade_id,
            reply_markup=markup,
        )

    except Exception as error:
        print_error(
            error_source=" telegram_actions.py, send_message_to_topic() )",
            error_message=error,
        )


# reply to message
async def reply_to_message(original_message: Message, text: str) -> int:

    """
    original_message = the message you want to reply to
    text = message content to be sent

    """

    try:
        replyed_message = await original_message.reply_text(text)
        return replyed_message.message_id

    except Exception as error:
        print_error(
            error_source=" telegram_actions.py, reply_to_message() )",
            error_message=error,
        )


# forward telegram message
async def forward_message(
    from_chat_id: int, message_id: int, chat_id: int, bot: ExtBot
) -> None:

    """
    from_chat_id = group id or person id the message to be forwarded is found
    message_id = id of the message to be forwarded
    chat_id = message reciver id (group, person)
    bot = bot instance
    """

    try:
        await bot.forwardMessage(
            chat_id=chat_id,
            from_chat_id=from_chat_id,
            message_id=message_id,
        )

    except Exception as error:
        print_error(
            error_source=" telegram_actions.py, forward_message() )",
            error_message=error,
        )


# delete telegram message
async def delete_message(chat_id: int, message_id: int, bot: ExtBot) -> None:

    """
    chat_id = group id or person id the message to be deleted is found
    message_id = id of the message to be deleted
    bot = bot instance
    """

    try:
        await bot.delete_message(
            chat_id=chat_id,
            message_id=message_id,
        )

    except Exception as error:
        print_error(
            error_source=" telegram_actions.py, delete_message() )",
            error_message=error,
        )
