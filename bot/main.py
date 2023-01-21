# TODO: ERROR HANDLING !!!

import logging

from settings import BOT_TOKEN

from handlers import (
    new_message_handler,
    accept_decline_handler,
    add_topic_handler,
    remove_topic_handler,
)
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    MessageHandler,
    CommandHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def main() -> None:

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, new_message_handler)
    )
    application.add_handler(CallbackQueryHandler(accept_decline_handler))

    application.add_handler(CommandHandler("add", add_topic_handler))

    application.add_handler(CommandHandler("remove", remove_topic_handler))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
