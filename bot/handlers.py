# TODO: ERROR HANDLING !!!
import os
from telegram import Update
from telegram.ext import ContextTypes


from helpers import extract_topic_name, get_topics_from_file, add_topics, remove_topics
# from settings import ADMIN_ID
from bot_actions import (
    send_new_message_to_admin,
    reply_to_new_message,
    delete_bot_greeting_message,
    delete_new_message,
    delete_message_from_admin,
    post_approved_message_to_group,
)


new_message_reply_text = (
    "Please wait a moment, your message is being reviewd by an admin"
)

admin_id = os.getenv('ADMIN_ID')
topics_file_path = os.path.join(os.getenv('FILE_PATH'), "topics.json")

# Event handlers

# called when new message is sent, forward message to admin and reply to the message then delete the message
async def new_message_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:



    if update.message["is_topic_message"] and extract_topic_name(
        message=str(update.message)
    ) in get_topics_from_file(file_name=topics_file_path):

        chat_id = update.message.chat_id
        message_id = update.message.message_id
        username = update.message.from_user.username
        text = update.message.text
        message_topic = update.message.message_thread_id

        # Reply to new message
        bot_message_id = await reply_to_new_message(
            message=update.message, username=username, text=new_message_reply_text
        )

        # send new message to admin
        await send_new_message_to_admin(
            admin_id=admin_id,
            chat_id=chat_id,
            text=text,
            username=username,
            message_thread_id=message_topic,
            bot=context.bot,
        )

        # delete new message
        await delete_new_message(
            chat_id=chat_id, message_id=message_id, bot=context.bot
        )

        # Add bot greeting message to deletion queue
        context.job_queue.run_once(
            delete_bot_greeting_message,
            5,
            data={"chat_id": chat_id, "message_id": bot_message_id},
        )


# Posts message if admin pressed accept or deletes the message if declined
async def accept_decline_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:

    button_selected_data = update.callback_query.data
    message_id = update.callback_query.message.message_id
    text = update.callback_query.message.text

    if button_selected_data == "0":
        await delete_message_from_admin(
            admin_id=admin_id, message_id=message_id, bot=context.bot
        )

    else:
        message_threade_id = button_selected_data.split(":")[1]

        await post_approved_message_to_group(
            chat_id=int(button_selected_data.split(":")[0]),
            message_thread_id=message_threade_id,
            text=text,
            bot=context.bot,
        )


# add new topic/s to restricted topics
async def add_topic_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    if update.message.chat_id == admin_id:
        if context.args:
            topics_file_path = os.path.join(topics_file_path, "topics.json")
            add_topics(file_name=topics_file_path, new_topics=context.args)


# remove topic/s from restricted topics
async def remove_topic_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:

    if update.message.chat_id == admin_id:
        if context.args:
            topics_file_path = os.path.join(topics_file_path, "topics.json")
            remove_topics(file_name=topics_file_path, removed_topics=context.args)
