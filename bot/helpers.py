import re
from typing import List
import json

# TODO: improve regex, error handling


def extract_topic_name(message: str) -> str:
    match = re.search(r"forum_topic_created=ForumTopicCreated(.*)", message)

    return match[0].split(",")[1].split("=")[1].split("'")[1]


def get_topics_from_file(file_name: str) -> List[str]:
    with open(file_name, "r") as fp:
        return json.load(fp)["topics"]


def add_topics(file_name: str, new_topics: List[str]):
    with open(file_name, "r+") as fp:
        file_data = json.load(fp)

        for topic in new_topics:
            file_data["topics"].append(topic)

        fp.seek(0)
        json.dump(file_data, fp, indent=4)


def remove_topics(file_name: str, removed_topics: List[str]):

    with open(file_name, "r") as fp:
        data = json.load(fp)

    for topic in removed_topics:
        data["topics"].remove(topic)

    with open(file_name, "w") as fp:
        json.dump(data, fp, indent=4)


def print_error(error_source, error_message):
    print("...... ERROR IN " + error_source + " ......")
    print(error_message)
    print("." * 30)
