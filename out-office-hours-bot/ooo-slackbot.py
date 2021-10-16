from calendar import SATURDAY
import os
from dotenv import load_dotenv, find_dotenv
import slack


# Reply to new messages
# Reply to new messages within specific time windows


load_dotenv(find_dotenv())
client = slack.WebClient(token=os.getenv('SLACK_BOT_USER_OAUTH_TOKEN'))


def message(*channels):
    """Post message to a list of channels"""
    for c in channels:
        client.chat_postMessage(channel=c, text='Testing bot message')

def main():
    message(*['#general', '#random'])


if __name__ == '__main__':
    main()
