import re

# TODO: improve regex, error handling

def extract_topic_name(message: str) -> str:
    match = re.search(r"forum_topic_created=ForumTopicCreated(.*)", message)

    return match[0].split(",")[1].split("=")[1].split('\'')[1]


def print_error(error_source, error_message):
    print("...... ERROR IN " + error_source + " ......")
    print(error_message)
    print("." * 30)
