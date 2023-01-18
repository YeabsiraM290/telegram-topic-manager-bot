from telegram import InlineKeyboardButton, InlineKeyboardMarkup


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
